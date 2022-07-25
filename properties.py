# Properties library
# Available properties: critical temperature, critical pressure and acentric factor



def Tcrit(comp):
    comp = comp.lower()

    if comp=="ch4" or comp=="methane" or comp=="c1":
        return 190.55
    elif comp=="c2h6" or comp=="ch3ch3" or comp=="ethane" or comp=="c2":
        return 305.32
    elif comp=="c3h8" or comp=="ch3ch2ch3" or comp=="propane" or comp=="c3":
        return 370
    elif comp=="n2" or comp=="nitrogen":
        return 126.21
    elif comp=="co2" or comp=="carbondioxide":
        return 304.12
    elif comp=="nc4h10" or comp=="n-butane" or comp=="nbutane" or comp=="nc4" or comp=="butane":
        return 426.3
    elif comp=="ic4h10" or comp=="i-butane" or comp=="ibutane" or comp=="ic4" or comp=="isobutane":
        return 407.84
    elif comp=="c5h12" or comp=="nc5h12" or comp=="pentane" or comp=="n-pentane" or comp=="npentane" or comp=="c5":
        return 469.7
    elif comp=="c6h14" or comp=="nc6h14" or comp=="hexane" or comp=="n-hexane" or comp=="nhexane" or comp=="c6":
        return 507
    elif comp=="c7h16" or comp=="nc7h16" or comp=="heptane" or comp=="n-heptane" or comp=="nheptane" or comp=="c7":
        return 540
    elif comp=="c8h18" or comp=="nc8h18" or comp=="octane" or comp=="n-octane" or comp=="noctane" or comp=="c8":
        return 569
    elif comp=="c9h20" or comp=="nc9h20" or comp=="nonane" or comp=="n-nonane" or comp=="nnonane" or comp=="c9":
        return 594
    elif comp=="c10h22" or comp=="nc10h22" or comp=="decane" or comp=="n-decane" or comp=="ndecane" or comp=="c10":
        return 617
    elif comp=="h2" or comp=="hydrogen":
        return 32.97
    elif comp=="o2" or comp=="oxygen":
        return 154.59
    elif comp=="co" or comp=="carbonmonoxide":
        return 133
    elif comp=="h2o" or comp=="water":
        return 647.14
    elif comp=="h2s" or comp=="hydrogensulfide":
        return 373.1
    elif comp=="he" or comp=="helium":
        return 5.19
    elif comp=="ar" or comp=="argon":
        return 150.87
    else:
        raise ValueError("Properties are not available for the given component.")

def Tc(comp):
    comp = comp.lower()

    if comp=="ch4" or comp=="methane" or comp=="c1":
        return 190.55
    elif comp=="c2h6" or comp=="ch3ch3" or comp=="ethane" or comp=="c2":
        return 305.32
    elif comp=="c3h8" or comp=="ch3ch2ch3" or comp=="propane" or comp=="c3":
        return 370
    elif comp=="n2" or comp=="nitrogen":
        return 126.21
    elif comp=="co2" or comp=="carbondioxide":
        return 304.12
    elif comp=="nc4h10" or comp=="n-butane" or comp=="nbutane" or comp=="nc4" or comp=="butane":
        return 426.3
    elif comp=="ic4h10" or comp=="i-butane" or comp=="ibutane" or comp=="ic4" or comp=="isobutane":
        return 407.84
    elif comp=="c5h12" or comp=="nc5h12" or comp=="pentane" or comp=="n-pentane" or comp=="npentane" or comp=="c5":
        return 469.7
    elif comp=="c6h14" or comp=="nc6h14" or comp=="hexane" or comp=="n-hexane" or comp=="nhexane" or comp=="c6":
        return 507
    elif comp=="c7h16" or comp=="nc7h16" or comp=="heptane" or comp=="n-heptane" or comp=="nheptane" or comp=="c7":
        return 540
    elif comp=="c8h18" or comp=="nc8h18" or comp=="octane" or comp=="n-octane" or comp=="noctane" or comp=="c8":
        return 569
    elif comp=="c9h20" or comp=="nc9h20" or comp=="nonane" or comp=="n-nonane" or comp=="nnonane" or comp=="c9":
        return 594
    elif comp=="c10h22" or comp=="nc10h22" or comp=="decane" or comp=="n-decane" or comp=="ndecane" or comp=="c10":
        return 617
    elif comp=="h2" or comp=="hydrogen":
        return 32.97
    elif comp=="o2" or comp=="oxygen":
        return 154.59
    elif comp=="co" or comp=="carbonmonoxide":
        return 133
    elif comp=="h2o" or comp=="water":
        return 647.14
    elif comp=="h2s" or comp=="hydrogensulfide":
        return 373.1
    elif comp=="he" or comp=="helium":
        return 5.19
    elif comp=="ar" or comp=="argon":
        return 150.87
    else:
        raise ValueError("Properties are not available for the given component.")

def criticalTemperature(comp):
    comp = comp.lower()

    if comp=="ch4" or comp=="methane" or comp=="c1":
        return 190.55
    elif comp=="c2h6" or comp=="ch3ch3" or comp=="ethane" or comp=="c2":
        return 305.32
    elif comp=="c3h8" or comp=="ch3ch2ch3" or comp=="propane" or comp=="c3":
        return 370
    elif comp=="n2" or comp=="nitrogen":
        return 126.21
    elif comp=="co2" or comp=="carbondioxide":
        return 304.12
    elif comp=="nc4h10" or comp=="n-butane" or comp=="nbutane" or comp=="nc4" or comp=="butane":
        return 426.3
    elif comp=="ic4h10" or comp=="i-butane" or comp=="ibutane" or comp=="ic4" or comp=="isobutane":
        return 407.84
    elif comp=="c5h12" or comp=="nc5h12" or comp=="pentane" or comp=="n-pentane" or comp=="npentane" or comp=="c5":
        return 469.7
    elif comp=="c6h14" or comp=="nc6h14" or comp=="hexane" or comp=="n-hexane" or comp=="nhexane" or comp=="c6":
        return 507
    elif comp=="c7h16" or comp=="nc7h16" or comp=="heptane" or comp=="n-heptane" or comp=="nheptane" or comp=="c7":
        return 540
    elif comp=="c8h18" or comp=="nc8h18" or comp=="octane" or comp=="n-octane" or comp=="noctane" or comp=="c8":
        return 569
    elif comp=="c9h20" or comp=="nc9h20" or comp=="nonane" or comp=="n-nonane" or comp=="nnonane" or comp=="c9":
        return 594
    elif comp=="c10h22" or comp=="nc10h22" or comp=="decane" or comp=="n-decane" or comp=="ndecane" or comp=="c10":
        return 617
    elif comp=="h2" or comp=="hydrogen":
        return 32.97
    elif comp=="o2" or comp=="oxygen":
        return 154.59
    elif comp=="co" or comp=="carbonmonoxide":
        return 133
    elif comp=="h2o" or comp=="water":
        return 647.14
    elif comp=="h2s" or comp=="hydrogensulfide":
        return 373.1
    elif comp=="he" or comp=="helium":
        return 5.19
    elif comp=="ar" or comp=="argon":
        return 150.87
    else:
        raise ValueError("Properties are not available for the given component.")

def Pcrit(comp):
    comp = comp.lower()

    if comp=="ch4" or comp=="methane" or comp=="c1":
        return 4.599e6
    elif comp=="c2h6" or comp=="ch3ch3" or comp=="ethane" or comp=="c2":
        return 4.88e6
    elif comp=="c3h8" or comp=="ch3ch2ch3" or comp=="propane" or comp=="c3":
        return 4.257e6
    elif comp=="n2" or comp=="nitrogen":
        return 3.39e6
    elif comp=="co2" or comp=="carbondioxide":
        return 7.39e6
    elif comp=="nc4h10" or comp=="n-butane" or comp=="nbutane" or comp=="nc4":
        return 3.8e6
    elif comp=="ic4h10" or comp=="i-butane" or comp=="ibutane" or comp=="ic4":
        return 3.629e6
    elif comp=="c5h12" or comp=="nc5h12" or comp=="pentane" or comp=="n-pentane" or comp=="npentane" or comp=="c5":
        return 3.37e6
    elif comp=="c6h14" or comp=="nc6h14" or comp=="hexane" or comp=="n-hexane" or comp=="nhexane" or comp=="c6":
        return 3.01
    elif comp=="c7h16" or comp=="nc7h16" or comp=="heptane" or comp=="n-heptane" or comp=="nheptane" or comp=="c7":
        return 2.81e6
    elif comp=="c8h18" or comp=="nc8h18" or comp=="octane" or comp=="n-octane" or comp=="noctane" or comp=="c8":
        return 2.51e6
    elif comp=="c9h20" or comp=="nc9h20" or comp=="nonane" or comp=="n-nonane" or comp=="nnonane" or comp=="c9":
        return 2.28e6
    elif comp=="c10h22" or comp=="nc10h22" or comp=="decane" or comp=="n-decane" or comp=="ndecane" or comp=="c10":
        return 2.099e6
    elif comp=="h2" or comp=="hydrogen":
        return 1.293e6
    elif comp=="o2" or comp=="oxygen":
        return 5.043e6
    elif comp=="co" or comp=="carbonmonoxide":
        return 3.5e6
    elif comp=="h2o" or comp=="water":
        return 22.064e6
    elif comp=="h2s" or comp=="hydrogensulfide":
        return 9e6
    elif comp=="he" or comp=="helium":
        return 0.227e6
    elif comp=="ar" or comp=="argon":
        return 4.898e6
    else:
        raise ValueError("Properties are not available for the given component.")

def Pc(comp):
    comp = comp.lower()

    if comp=="ch4" or comp=="methane" or comp=="c1":
        return 4.599e6
    elif comp=="c2h6" or comp=="ch3ch3" or comp=="ethane" or comp=="c2":
        return 4.88e6
    elif comp=="c3h8" or comp=="ch3ch2ch3" or comp=="propane" or comp=="c3":
        return 4.257e6
    elif comp=="n2" or comp=="nitrogen":
        return 3.39e6
    elif comp=="co2" or comp=="carbondioxide":
        return 7.39e6
    elif comp=="nc4h10" or comp=="n-butane" or comp=="nbutane" or comp=="nc4":
        return 3.8e6
    elif comp=="ic4h10" or comp=="i-butane" or comp=="ibutane" or comp=="ic4":
        return 3.629e6
    elif comp=="c5h12" or comp=="nc5h12" or comp=="pentane" or comp=="n-pentane" or comp=="npentane" or comp=="c5":
        return 3.37e6
    elif comp=="c6h14" or comp=="nc6h14" or comp=="hexane" or comp=="n-hexane" or comp=="nhexane" or comp=="c6":
        return 3.01
    elif comp=="c7h16" or comp=="nc7h16" or comp=="heptane" or comp=="n-heptane" or comp=="nheptane" or comp=="c7":
        return 2.81e6
    elif comp=="c8h18" or comp=="nc8h18" or comp=="octane" or comp=="n-octane" or comp=="noctane" or comp=="c8":
        return 2.51e6
    elif comp=="c9h20" or comp=="nc9h20" or comp=="nonane" or comp=="n-nonane" or comp=="nnonane" or comp=="c9":
        return 2.28e6
    elif comp=="c10h22" or comp=="nc10h22" or comp=="decane" or comp=="n-decane" or comp=="ndecane" or comp=="c10":
        return 2.099e6
    elif comp=="h2" or comp=="hydrogen":
        return 1.293e6
    elif comp=="o2" or comp=="oxygen":
        return 5.043e6
    elif comp=="co" or comp=="carbonmonoxide":
        return 3.5e6
    elif comp=="h2o" or comp=="water":
        return 22.064e6
    elif comp=="h2s" or comp=="hydrogensulfide":
        return 9e6
    elif comp=="he" or comp=="helium":
        return 0.227e6
    elif comp=="ar" or comp=="argon":
        return 4.898e6
    else:
        raise ValueError("Properties are not available for the given component.")

def criticalPressure(comp):
    comp = comp.lower()

    if comp=="ch4" or comp=="methane" or comp=="c1":
        return 4.599e6
    elif comp=="c2h6" or comp=="ch3ch3" or comp=="ethane" or comp=="c2":
        return 4.88e6
    elif comp=="c3h8" or comp=="ch3ch2ch3" or comp=="propane" or comp=="c3":
        return 4.257e6
    elif comp=="n2" or comp=="nitrogen":
        return 3.39e6
    elif comp=="co2" or comp=="carbondioxide":
        return 7.39e6
    elif comp=="nc4h10" or comp=="n-butane" or comp=="nbutane" or comp=="nc4":
        return 3.8e6
    elif comp=="ic4h10" or comp=="i-butane" or comp=="ibutane" or comp=="ic4":
        return 3.629e6
    elif comp=="c5h12" or comp=="nc5h12" or comp=="pentane" or comp=="n-pentane" or comp=="npentane" or comp=="c5":
        return 3.37e6
    elif comp=="c6h14" or comp=="nc6h14" or comp=="hexane" or comp=="n-hexane" or comp=="nhexane" or comp=="c6":
        return 3.01
    elif comp=="c7h16" or comp=="nc7h16" or comp=="heptane" or comp=="n-heptane" or comp=="nheptane" or comp=="c7":
        return 2.81e6
    elif comp=="c8h18" or comp=="nc8h18" or comp=="octane" or comp=="n-octane" or comp=="noctane" or comp=="c8":
        return 2.51e6
    elif comp=="c9h20" or comp=="nc9h20" or comp=="nonane" or comp=="n-nonane" or comp=="nnonane" or comp=="c9":
        return 2.28e6
    elif comp=="c10h22" or comp=="nc10h22" or comp=="decane" or comp=="n-decane" or comp=="ndecane" or comp=="c10":
        return 2.099e6
    elif comp=="h2" or comp=="hydrogen":
        return 1.293e6
    elif comp=="o2" or comp=="oxygen":
        return 5.043e6
    elif comp=="co" or comp=="carbonmonoxide":
        return 3.5e6
    elif comp=="h2o" or comp=="water":
        return 22.064e6
    elif comp=="h2s" or comp=="hydrogensulfide":
        return 9e6
    elif comp=="he" or comp=="helium":
        return 0.227e6
    elif comp=="ar" or comp=="argon":
        return 4.898e6
    else:
        raise ValueError("Properties are not available for the given component.")

def acentric(comp):
    comp = comp.lower()

    if comp=="ch4" or comp=="methane" or comp=="c1":
        return 0.011
    elif comp=="c2h6" or comp=="ch3ch3" or comp=="ethane" or comp=="c2":
        return 0.099
    elif comp=="c3h8" or comp=="ch3ch2ch3" or comp=="propane" or comp=="c3":
        return 0.152
    elif comp=="n2" or comp=="nitrogen":
        return 0.04
    elif comp=="co2" or comp=="carbondioxide":
        return 0.228
    elif comp=="nc4h10" or comp=="n-butane" or comp=="nbutane" or comp=="nc4":
        return 0.199
    elif comp=="ic4h10" or comp=="i-butane" or comp=="ibutane" or comp=="ic4":
        return 0.177
    elif comp=="c5h12" or comp=="nc5h12" or comp=="pentane" or comp=="n-pentane" or comp=="npentane" or comp=="c5":
        return 0.249
    elif comp=="c6h14" or comp=="nc6h14" or comp=="hexane" or comp=="n-hexane" or comp=="nhexane" or comp=="c6":
        return 0.305
    elif comp=="c7h16" or comp=="nc7h16" or comp=="heptane" or comp=="n-heptane" or comp=="nheptane" or comp=="c7":
        return 0.351
    elif comp=="c8h18" or comp=="nc8h18" or comp=="octane" or comp=="n-octane" or comp=="noctane" or comp=="c8":
        return 0.396
    elif comp=="c9h20" or comp=="nc9h20" or comp=="nonane" or comp=="n-nonane" or comp=="nnonane" or comp=="c9":
        return 0.438
    elif comp=="c10h22" or comp=="nc10h22" or comp=="decane" or comp=="n-decane" or comp=="ndecane" or comp=="c10":
        return 0.484
    elif comp=="h2" or comp=="hydrogen":
        return -0.215
    elif comp=="o2" or comp=="oxygen":
        return 0.022
    elif comp=="co" or comp=="carbonmonoxide":
        return 0.066
    elif comp=="h2o" or comp=="water":
        return 0.345
    elif comp=="h2s" or comp=="hydrogensulfide":
        return 0.083
    elif comp=="he" or comp=="helium":
        return -0.39
    elif comp=="ar" or comp=="argon":
        return 0
    else:
        raise ValueError("Properties are not available for the given component.")

def w(comp):
    comp = comp.lower()

    if comp=="ch4" or comp=="methane" or comp=="c1":
        return 0.011
    elif comp=="c2h6" or comp=="ch3ch3" or comp=="ethane" or comp=="c2":
        return 0.099
    elif comp=="c3h8" or comp=="ch3ch2ch3" or comp=="propane" or comp=="c3":
        return 0.152
    elif comp=="n2" or comp=="nitrogen":
        return 0.04
    elif comp=="co2" or comp=="carbondioxide":
        return 0.228
    elif comp=="nc4h10" or comp=="n-butane" or comp=="nbutane" or comp=="nc4":
        return 0.199
    elif comp=="ic4h10" or comp=="i-butane" or comp=="ibutane" or comp=="ic4":
        return 0.177
    elif comp=="c5h12" or comp=="nc5h12" or comp=="pentane" or comp=="n-pentane" or comp=="npentane" or comp=="c5":
        return 0.249
    elif comp=="c6h14" or comp=="nc6h14" or comp=="hexane" or comp=="n-hexane" or comp=="nhexane" or comp=="c6":
        return 0.305
    elif comp=="c7h16" or comp=="nc7h16" or comp=="heptane" or comp=="n-heptane" or comp=="nheptane" or comp=="c7":
        return 0.351
    elif comp=="c8h18" or comp=="nc8h18" or comp=="octane" or comp=="n-octane" or comp=="noctane" or comp=="c8":
        return 0.396
    elif comp=="c9h20" or comp=="nc9h20" or comp=="nonane" or comp=="n-nonane" or comp=="nnonane" or comp=="c9":
        return 0.438
    elif comp=="c10h22" or comp=="nc10h22" or comp=="decane" or comp=="n-decane" or comp=="ndecane" or comp=="c10":
        return 0.484
    elif comp=="h2" or comp=="hydrogen":
        return -0.215
    elif comp=="o2" or comp=="oxygen":
        return 0.022
    elif comp=="co" or comp=="carbonmonoxide":
        return 0.066
    elif comp=="h2o" or comp=="water":
        return 0.345
    elif comp=="h2s" or comp=="hydrogensulfide":
        return 0.083
    elif comp=="he" or comp=="helium":
        return -0.39
    elif comp=="ar" or comp=="argon":
        return 0
    else:
        raise ValueError("Properties are not available for the given component.")


def acentricFactor(comp):
    comp = comp.lower()

    if comp=="ch4" or comp=="methane" or comp=="c1":
        return 0.011
    elif comp=="c2h6" or comp=="ch3ch3" or comp=="ethane" or comp=="c2":
        return 0.099
    elif comp=="c3h8" or comp=="ch3ch2ch3" or comp=="propane" or comp=="c3":
        return 0.152
    elif comp=="n2" or comp=="nitrogen":
        return 0.04
    elif comp=="co2" or comp=="carbondioxide":
        return 0.228
    elif comp=="nc4h10" or comp=="n-butane" or comp=="nbutane" or comp=="nc4":
        return 0.199
    elif comp=="ic4h10" or comp=="i-butane" or comp=="ibutane" or comp=="ic4":
        return 0.177
    elif comp=="c5h12" or comp=="nc5h12" or comp=="pentane" or comp=="n-pentane" or comp=="npentane" or comp=="c5":
        return 0.249
    elif comp=="c6h14" or comp=="nc6h14" or comp=="hexane" or comp=="n-hexane" or comp=="nhexane" or comp=="c6":
        return 0.305
    elif comp=="c7h16" or comp=="nc7h16" or comp=="heptane" or comp=="n-heptane" or comp=="nheptane" or comp=="c7":
        return 0.351
    elif comp=="c8h18" or comp=="nc8h18" or comp=="octane" or comp=="n-octane" or comp=="noctane" or comp=="c8":
        return 0.396
    elif comp=="c9h20" or comp=="nc9h20" or comp=="nonane" or comp=="n-nonane" or comp=="nnonane" or comp=="c9":
        return 0.438
    elif comp=="c10h22" or comp=="nc10h22" or comp=="decane" or comp=="n-decane" or comp=="ndecane" or comp=="c10":
        return 0.484
    elif comp=="h2" or comp=="hydrogen":
        return -0.215
    elif comp=="o2" or comp=="oxygen":
        return 0.022
    elif comp=="co" or comp=="carbonmonoxide":
        return 0.066
    elif comp=="h2o" or comp=="water":
        return 0.345
    elif comp=="h2s" or comp=="hydrogensulfide":
        return 0.083
    elif comp=="he" or comp=="helium":
        return -0.39
    elif comp=="ar" or comp=="argon":
        return 0
    else:
        raise ValueError("Properties are not available for the given component.")
