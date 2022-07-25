import numpy as np
#from CoolProp.CoolProp import PropsSI as prop
import CoolProp
from p2f import *
from thermo.unifac import UFIP, UFSG, UNIFAC
import eos
import os

os.system('clear')

water = CoolProp.AbstractState("HEOS", 'water')
water.update(CoolProp.QT_INPUTS, 0, Texp)
Psat = water.p()

Pexp = 100e5
Texp = 273.15 + 4
P = np.zeros(2)
#Psat = prop("P", "T", Texp, "Q", 0, "water")
component = "CH4"
comp = ["CH4"]
mix_comps = "Methane&Water"
comps = ['Methane', 'Water']

#mix_comps = "Methane"
z = [0.1, 0.9]

GE = UNIFAC.from_subgroups(chemgroups=[{1:1}, {7:1}], T = Texp, xs = z, version=0, interaction_data=UFIP, subgroups=UFSG)
gamma_w = GE.gammas()[1]

mix = CoolProp.AbstractState("PR", mix_comps)
mix.set_mole_fractions(z)
mix.set_binary_interaction_double(0, 1, "kij", 0.033)


#mix.specify_phase(CoolProp.iphase_twophase)

# Looping structures (main loop)
for structure in range(2):

    # Retrieve lattice parameter and number of molecules of water for current structure
    if structure == 1:
        n_H2O = 46
        nu = [2, 6]
    else:
        n_H2O = 136
        nu = [16, 8]


    # Initial pressure guess
    Pg = Pexp

    Psat_beta = antoine_beta(component)

    diff_new = 0
    Pg_new = 0
    # Isofugacity loop to determine Pg
    while True:
        Cf = np.zeros(len(comp))
        theta = np.zeros(len(comp))
        ddT = tempdep(Texp, Pg)
        nulog = np.zeros(2)

        #mix.update(CoolProp.PT_INPUTS, Pg, Texp)
        #water.update(CoolProp.PT_INPUTS, Pg, Texp)

        fug, x, y = eos.flash(comps, z, Pg, Texp)

        # The problem is either the Langmuir constant or the fugacity calculated.
        for cageType in range(2):
            Cml = langmuir(structure, component, cageType, Texp)
            #Cml = Cml(Texp)
            Cf = Cml*fug[0][0]
            #Cf = Cml*mix.fugacity(0)
            theta = Cf/(1 + Cf)
            nulog[cageType] = nu[cageType]*np.log(1 - theta)
        dMu = -R*Texp*sum(nulog)
        #print(mix.fugacity(0))

        #T_nfp = water.melting_line(1,1,Pg)
        #T_f = T_nfp + ddT

        # Need to implement equations later on
        #if Texp < T_f:
        #    print("Ice detected!")
        #    break

        # Volume of empty hydrate, eqns 27 and 28
        Pg_MPa = Pg*1e-6
        if structure == 1:
            V_beta = (11.835 + 2.217E-5*Texp + 2.242E-6*Texp**2)*1E-30*Na/n_H2O - 8.006E-9*(Pg_MPa) + 5.448E-12*(Pg_MPa)**2
        else:
            V_beta = (17.130 + 2.249E-4*Texp + 2.013E-6*Texp**2)*1E-30*Na/n_H2O - 8.006E-9*(Pg_MPa) + 5.448E-12*(Pg_MPa)**2

        # Volume of water at given T and Pg
        Vg = -10.9241 + 2.5e-4*(Texp - 273.15) - 3.3532e-4*(Pg_MPa - 0.101325) + 1.559e-7*(Pg_MPa - 0.101325)**2
        Vg = np.exp(Vg)
        # As calculated by CoolProp
        #Vg = 1/water.rhomolar()

        # Fugacities
        #f_pi = mix.fugacity(1)
        #x_w = 1 - mix.fugacity(0)/henry('CH4', Texp)
        x_w = x[1]
        f_pi = x_w*gamma_w*Psat*np.exp((Vg*(Pg - Psat))/(R*Texp))
        #f_pi = fug[1][1]

        f_beta = Psat_beta*np.exp(V_beta*(Pg - Psat_beta)/(R*Texp))
        #print(f_beta)
        #print(np.exp(-dMu/(R*Texp)))
        f_H = f_beta*np.exp(-dMu/(R*Texp))

        pdiff = np.abs(f_H - f_pi)
        diff_old = diff_new
        diff_new = f_pi - f_H

        if pdiff < 1e-9:
            P[structure] = Pg
            #print("Pg: " + str(Pg))
            break
        else:
            #print("Water fugacity: " + str(f_pi))
            #print("Hydrate fugacity: " + str(f_H))
            


            Pg_old = Pg_new
            Pg_new = Pg
            Pg = Pg_new - diff_new*(Pg_new - Pg_old)/(diff_new - diff_old)

            print(Pg_new)
            print(Pg_old)
            print(diff_new)
            print(diff_old)

            

            #Pg = Pg*(f_H/f_pi)
            
            #os.system('clear')
            
            #print(Pg)
            if(np.isnan(Pg)):
                print("NaN detected! Breaking the loop.")
                P = np.nan
                break

print("Temperature: " + str(Texp-273.15) + " C")
print("Pressure: " + str(np.min(P/1e5)) + " bar")
