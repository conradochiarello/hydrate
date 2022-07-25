import numpy as np
#from scipy.integrate import fixed_quad
from scipy import integrate

# Constants used throughout the library
x_w = 1
k = 1.380649*10**-23
R = 8.31446261815324
Na = 6.022*10**23
Texp = 277.15
Pexp = 100*1E5
gamma = 1
dHm = 0.334
hyd_number = 6


def langmuir(structure, component, cageType, T):
    # Get the correct cage properties according to the structure
    r1, r2, z1, z2 = cageProp(structure)

    # and choose them according to the type of cage (5^12, 5^12-6^2 or 5^12-6^4)
    if cageType == 1:
        Rcell = r1
        z = z1
    else:
        Rcell = r2
        z = z2

    # Get the Kihara potential parameters
    eps_g, sigma_g, a_g = kihara(component)
    eps_w, sigma_w, a_w = kihara('h2o')

    eps = np.sqrt(eps_g*eps_w)
    sigma = 0.5*(sigma_g + sigma_w)
    a = 0.5*(a_g + a_w)

    # Define the potential function to be integrated
    # Note: the potential function takes into account the potential for the first (W1), second (W2) and third (W3) shells
    def potential(r):
        W = np.zeros(3)

        # Delta, Eq. 7
        delta = lambda n, i: ((1 - r/Rcell[i] - a/Rcell[i])**(-n) - (1 + r/Rcell[i] - a/Rcell[i])**(-n))/n

        # Auxiliary variable to make calculations simpler
        srr = lambda n, i: sigma**n/(r*Rcell[i]**(n-1))*(delta(n-2, i) + (a/Rcell[i])*delta(n-1, i))

        W1 = 2*z[0]*eps*(srr(12, 0) - srr(6, 0))
        W2 = 2*z[1]*eps*(srr(12, 1) - srr(6, 1))
        W3 = 2*z[2]*eps*(srr(12, 2) - srr(6, 2))

        W = W1 + W2 + W3
        return W

    # Create integrand for Eq. 4, Klauda and Sandler (2000)
    # Note: there is a missing minus sign on the paper
    toIntegrate = lambda r: np.exp(-potential(r)/(k*T))*r**2

    # Gaussian quadrature 36 point integration, as per recommendation of the authors
    integ = integrate.fixed_quad(toIntegrate, 0, Rcell[0]-a, n = 36)

    # Computes Langmuir constant
    Cml = 4*np.pi/(k*T)*integ[0]
    return Cml

# Need to review this
def tempdep(T, P):
    #Tnfp = prop("T_FREEZE", "Water")
    Tnfp = 273.15
    return R*Tnfp**2/dHm*np.log(x_w*gamma)

# Cage properties, Klauda and Sandler (2000)
def cageProp(structure):
    if structure == 1:
        r1 = [3.906e-10, 6.593e-10, 8.086e-10]
        r2 = [4.326e-10, 7.078e-10, 8.285e-10]

        z1 = [20, 20, 50]
        z2 = [24, 24, 50]
    else:
        r1 = [3.902e-10, 6.667e-10, 8.079e-10]
        r2 = [4.682e-10, 7.464e-10, 8.782e-10]

        z1 = [20, 20, 50]
        z2 = [28, 28, 50]

    return r1, r2, z1, z2

# Kihara potential parameters, Klauda and Sandler (2000)
def kihara(comp):
    comp = comp.lower()
    if comp=="ch4" or comp=="methane" or comp=="c1":
        eps = 232.2*k
        sigma = 3.505e-10
        a = 0.28e-10
    elif comp=="c2h6" or comp=="ch3ch3" or comp=="ethane" or comp=="c2":
        eps = 404.3*k
        sigma = 4.022e-10
        a = 0.574e-10
    elif comp=="c3h8" or comp=="ch3ch2ch3" or comp=="propane" or comp=="c3":
        eps = 493.71*k
        sigma = 4.519e-10
        a = 0.6502e-10
    elif comp=="ic4h10" or comp=="i-butane" or comp=="ibutane" or comp=="ic4" or comp=="isobutane":
        eps = 628.6*k
        sigma = 4.746e-10
        a = 0.859e-10
    elif comp=="h2s" or comp=="hydrogensulfide":
        eps = 459.6*k
        sigma = 3.607e-10
        a = 0.3508e-10
    elif comp=="n2" or comp=="nitrogen":
        eps = 142.1*k
        sigma = 3.469e-10
        a = 0.341e-10
    elif comp=="co2" or comp=="carbondioxide":
        eps = 513.85*k
        sigma = 3.335e-10
        a = 0.677e-10
    elif comp == "cC3H6":
        eps = 554.4*k
        sigma = 4.185e-10
        a = 0.653e-10
    elif comp=="h2o" or comp=="water":
        eps = 102.134*k
        sigma = 3.564e-10
        a = 0e-10
    else:
        raise ValueError("Kihara cell parameters not defined")

    return eps, sigma, a

# Saturation pressure of empty hydrate, Klauda and Sandler (2000)
def antoine_beta(comp):
    comp = comp.lower()

    if comp=="ch4" or comp=="methane" or comp=="c1":
        A = 4.6477
        B = -5242.9790
        C = 2.7789
        D = -8.7156E-3
    elif comp=="c2h6" or comp=="ch3ch3" or comp=="ethane" or comp=="c2":
        A = 4.6766
        B = -5263.9565
        C = 2.7789
        D = -9.0154E-3
    elif comp=="c3h8" or comp=="ch3ch2ch3" or comp=="propane" or comp=="c3":
        A = 5.2578
        B = -5650.5584
        C = 2.7789
        D = -16.2021E-3
    elif comp=="ic4h10" or comp=="i-butane" or comp=="ibutane" or comp=="ic4" or comp=="isobutane":
        A = 4.6818
        B = -5455.2664
        C = 2.7789
        D = -8.9678E-3
    elif comp=="h2s" or comp=="hydrogensulfide":
        A = 4.6446
        B = -5150.3690
        C = 2.7789
        D = -8.7553E-3
    elif comp=="n2" or comp=="nitrogen":
        A = 5.1511
        B = -5595.4346
        C = 2.7789
        D = -16.0445E-3
    elif comp=="co2" or comp=="carbondioxide":
        A = 4.6188
        B = -5020.8289
        C = 2.7789
        D = -8.3455E-3
    elif comp == "cC3H6":
        A = 4.6652
        B = -5424.1108
        C = 2.7789
        D = -14.8446
    return np.exp(A*np.log(Texp) + B/Texp + C + D*Texp)

# Henry constants, Klauda and Sandler (2000)
def henry(comp, T):
    if comp == "CH4":
        H1 = -183.7860
        H2 = 9112.582
        H3 = 25.0405
        H4 = -0.00015
    elif comp == "C2H6":
        H1 = -183.7860
        H2 = 9112.582
        H3 = 25.0405
        H4 = -0.00015
    elif comp == "C3H8":
        H1 = -183.7860
        H2 = 9112.582
        H3 = 25.0405
        H4 = -0.00015
    elif comp == "iC4H10":
        H1 = -183.7860
        H2 = 9112.582
        H3 = 25.0405
        H4 = -0.00015
    elif comp == "H2S":
        H1 = -183.7860
        H2 = 9112.582
        H3 = 25.0405
        H4 = -0.00015
    elif comp == "N2":
        H1 = -183.7860
        H2 = 9112.582
        H3 = 25.0405
        H4 = -0.00015
    elif comp == "CO2":
        H1 = -183.7860
        H2 = 9112.582
        H3 = 25.0405
        H4 = -0.00015
    elif comp == "cC3H6":
        H1 = -183.7860
        H2 = 9112.582
        H3 = 25.0405
        H4 = -0.00015
    elif comp == "H2O":
        H1 = -183.7860
        H2 = 9112.582
        H3 = 25.0405
        H4 = -0.00015
    
    lnH = H1 + H2/T + H3*np.log(T) + H4*T
    H = 101325*np.exp(-lnH)
    return H
