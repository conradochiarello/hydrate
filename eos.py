import numpy as np
import pandas as pd
from scipy.optimize import minimize, Bounds
import properties

# Set bounds for flash excluding trivial solution (V = 1)
bnds = Bounds(0, 1-1e-12)

# Constants
R = 8.31446261815324   # cm3.MPa/(mol.K)

# Inputs
# Binary interaction parameter
#kij = np.array([[0, 0.033], [0.033, 0]])
#kij = np.array([[0, -0.003, 0.016, 0.026, 0.03, 0.09, 0.08, 0.033], [-0.003, 0, 0.001, -0.007, 0.044, 0.13, 0.086, 0.089], 
#[0.016, 0.001, 0, -0.007, 0.078, 0.12, 0.08, 0.007], [0.026, -0.007, -0.007, 0, 0.1, 0.13, 0.047, -0.014],
#[0.03, 0.044, 0.078, 0.1, 0, -0.2, 0.17, 0.09], [0.09, 0.13, 0.12, 0.13, -0.02, 0, 0.097, 0.093],
#[0.08, 0.086, 0.08, 0.047, 0.17, 0.097, 0, 0.08], [0.033, 0.089, 0.007, -0.014, 0.09, 0.093, 0.08, 0]])

def get_kij(valid):
    kij = np.array([[0, -0.003, 0.016, 0.026, 0.03, 0.09, 0.08, 0.033], [-0.003, 0, 0.001, -0.007, 0.044, 0.13, 0.086, 0.089], 
    [0.016, 0.001, 0, -0.007, 0.078, 0.12, 0.08, 0.007], [0.026, -0.007, -0.007, 0, 0.1, 0.13, 0.047, -0.014],
    [0.03, 0.044, 0.078, 0.1, 0, -0.2, 0.17, 0.09], [0.09, 0.13, 0.12, 0.13, -0.02, 0, 0.097, 0.093],
    [0.08, 0.086, 0.08, 0.047, 0.17, 0.097, 0, 0.08], [0.033, 0.089, 0.007, -0.014, 0.09, 0.093, 0.08, 0]])

    k = kij[valid*np.transpose(valid[:][np.newaxis])]
    k = np.reshape(k, [np.sum(valid), np.sum(valid)])
    return k

# Get properties according to the component and given state (P, T)
def get_props(comps, P, T):

    Tc = np.array([properties.criticalTemperature(comp) for comp in comps])
    Pc = np.array([properties.criticalPressure(comp) for comp in comps])
    omega = np.array([properties.acentricFactor(comp) for comp in comps])
    kappa = 0.37464 + 1.54226*omega - 0.26992*omega**2
    a = 0.45724*R**2*Tc**2/Pc*(1 + kappa*(1 - np.sqrt(T/Tc)))**2
    b = 0.07780*R*Tc/Pc
    A = a*P/(R*T)**2
    B = b*P/(R*T)
    
    return Tc, Pc, omega, kappa, A, B, a, b

# Mixing rule
def mix_rule(z, A, B):
    kij = get_kij(z>0)
    z = z[z > 0]
    AT = np.transpose(np.array(A)[np.newaxis])
    zT = np.transpose(np.array(z)[np.newaxis])
    A_mix = z*zT*(1 - kij)*np.sqrt(A*AT)
    A_mix = np.sum(A_mix)
    B_mix = np.sum(z*B)
    return A_mix, B_mix

# Cubic EOS routine
# PR is implemented, but other EoSs are welcome to be implemented as needed
def get_Z(comps, z, P, T):
    Tc, Pc, omega, kappa, A, B, a, b = get_props(comps, P, T)
    Tr = [T/Tcrit for Tcrit in Tc]

    # Conditional to other EoS, when they're available
    #if eqn == 'PR':
    #    sigma = 1 + np.sqrt(2)
    #    epsilon = 1 - np.sqrt(2)
    #    Omega = 0.07780
    #    Psi = 0.45724
    #    alpha = [(1 + (0.37464 + 1.54225*omega[i] - 0.26992*omega[i]**2)*(1 - np.sqrt(Tr[i])))**2 for i in range(len(comps))]
    
    A_mix, B_mix = mix_rule(z, A, B)
    
    # Get the coefficients and solve the cubic equation
    coeff = [1, -(1 - B_mix), A_mix - 2*B_mix - 3*B_mix**2, -(A_mix*B_mix - B_mix**2 - B_mix**3)]
    Z = np.roots(coeff)

    # Get real roots
    Z = np.real(Z[np.isreal(Z)])

    # Define Z of vapor and liquid phases
    ZL = np.amin(Z)
    ZV = np.amax(Z)

    return ZV, ZL

def get_phi(comps, z, P, T):
    
    # Get compressibility factors
    ZV, ZL = get_Z(comps, z, P, T)

    # and properties
    Tc, Pc, omega, kappa, A, B, a, b = get_props(comps, P, T)

    # Apply mixing rules
    A_mix, B_mix = mix_rule(z, A, B)

    lnphiL = [None]*len(comps)
    lnphiV = [None]*len(comps)
    phiL = [None]*len(comps)
    phiV = [None]*len(comps)

    # Define additional constants to make calculations simpler
    Ai = np.zeros(len(comps))
    for i in range(len(comps)):
        for j in range(len(comps)):
            Ai[i] = Ai[i] + z[j]*np.sqrt(a[i]*a[j])*P/(R*T)**2

    # Calculate fugacity coefficients
    for j in range(len(comps)):
        Bj = B[j]/B_mix
        Aj = Ai[j]/A_mix

        divL = ZL + (1 + np.sqrt(2))*B_mix
        quoL = ZL + (1 - np.sqrt(2))*B_mix

        divV = ZV + (1 + np.sqrt(2))*B_mix
        quoV = ZV + (1 - np.sqrt(2))*B_mix

        lnphiL[j] = (ZL - 1)*Bj - np.log(ZL - B_mix) - A_mix/(np.sqrt(8)*B_mix)*np.log(divL/quoL)*(2*Aj - Bj)
        lnphiV[j] = (ZV - 1)*Bj - np.log(ZV - B_mix) - A_mix/(np.sqrt(8)*B_mix)*np.log(divV/quoV)*(2*Aj - Bj)

        phiL[j] = np.exp(lnphiL[j])
        phiV[j] = np.exp(lnphiV[j])

    phi = [phiL, phiV]
    return phi

def flash(comps, z, P, T):
    n = range(len(comps))

    # Get fugacity coefficients
    phi = get_phi(comps, z, P, T)
    z = z[z>0]
    
    # Define K
    K = [phi[0][i]/(phi[1][i]) for i in n]
    
    flashV = [None]*len(comps)
    
    # Define the flash function to calculate V
    def fV(V):
        for i in n:
            flashV[i] = z[i]*K[i]/(1 + V*(K[i] - 1))
        return np.abs(sum(flashV) - 1)
    
    # Minimize sum(flashV) - 1 to get V
    V = minimize(fV, 0, method='nelder-mead', bounds=bnds, tol=1e-12, options={'maxiter':1e5})
    V = V.x

    # Back calculate y and x, vapor and liquid compositions
    y = [z[i]*K[i]/(1 + V*(K[i] - 1)) for i in n]
    x = [(z[i] - y[i]*V)/(1 - V) for i in n]

    x = [item for sublist in x for item in sublist]
    y = [item for sublist in y for item in sublist]

    # Equation 8-12.1, Poling (2000)
    fv = [y[i]*phi[1][i]*P for i in n]
    fl = [x[i]*phi[0][i]*P for i in n]

    f = [fl, fv]
    return f, x, y
