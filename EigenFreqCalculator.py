import numpy as np
from mpmath import findroot, exp
import workfiles as rf
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)


def M1(n, L, k0):
    """Transfer matrix for the layer."""
    return np.array([[exp(1j * k0 * L * n), 0], [0, exp(-1j * k0 * L * n)]], dtype=np.complex)


def M2(n1, n2):
    """Boundary transfer matrix between layers."""
    return 1 / (2 * n2) * np.array([[n2 + n1, n2 - n1], [n2 - n1, n2 + n1]], dtype=np.complex)


def fun (NL, L, n, hw, state):
    """Function for calculating the coefficients r, t, rs, ts and equations for eigenfrequencies."""
    k0 = 0.005067730758485526 * hw
    M = np.dot(M2(n[NL], n[NL + 1]), M1(n[NL], L[NL], k0))
    for i in range(NL - 1, -1, -1):
        M = np.dot(M, np.dot(M2(n[i], n[i + 1]), M1(n[i], L[i], k0)))

    r = -M[1, 0] / M[1, 1]
    t = M[0, 0] + M[0, 1] * r
    ts = 1 / M[1, 1]
    rs = M[0, 1] / M[1, 1]

    if state == 1:
        return (t - 1) * (ts - 1) - r * rs
    elif state == 3:
        return r, t, rs, ts


def Ertef(Bar):
    """Calculation of eigenfrequencies and related parameters."""
    layer, friqrt, profile, inangle, hw0, hw1, hws, h_nm = rf.readin()
    NL, L, n = rf.readlayer(layer)
    eigenfreq = []
    h = hws
    w = hw0
    niter = int((hw1 - hw0) / h)
    for i in range(niter):
        Bar.setProperty("value", i / niter * 100)
        print(i, '/', niter)
        funct = lambda we: fun(NL, L, n, we, 1)
        try:
            froot = findroot(funct, w, solver='muller', verbose=False, verify=False)
            eigenfreq.append(np.round(complex(froot), 14))
        except Exception:
            eigenfreq.append('nan')
        w += h

    Bar.setProperty("value", 0)
    return verify_frequencies(NL, L, n, eigenfreq, hw0, hw1, friqrt)


def verify_frequencies(NL, L, n, eigenfreq, hw0, hw1, friqrt):
    """Checking and recording correct eigenfrequencies."""
    Neigenfreq, r1, t1, rs1, ts1 = [], [], [], [], []
    for ef in eigenfreq:
        flag = 0
        if ((np.real(ef) >= hw0) and (np.real(ef) <= hw1)) == 0:
            flag = 1
        for i in Neigenfreq:
            if i == ef:
                flag = 1

        if (np.real(fun(NL, L, n, ef, 1)) > 1e-14) or (np.imag(fun(NL, L, n, ef, 1)) > 1e-14):
                flag = 1

        if flag == 0:
            Neigenfreq.append(ef)

    Neigenfreq.sort(key=lambda x: x.real)
    for ef in Neigenfreq:
        r, t, rs, ts = fun(NL, L, n, ef, 3)
        r1.append(np.round(r, 8))
        t1.append(np.round(t, 8))
        rs1.append(np.round(rs, 8))
        ts1.append(np.round(ts, 8))

    # calc init prifiles
    E0, El = [], []

    for i in range (0, len(Neigenfreq)):
        E0.append(1)

    for i in range (0, len(Neigenfreq)):
        if rs1[i] == 0 :
            El.append(1)
            # еще надо бы добавлять -1
        else:
            El.append(np.round( - (t1[i] - 1) / (rs1[i]), 8))

    rf.writefriqrt(friqrt, E0, El, r1, t1, rs1, ts1, Neigenfreq)

    return  E0, El, r1, t1, rs1, ts1, Neigenfreq


def profile(E0, El, r1, t1, rs1, ts1, eigenfreq):
    """Calculation and saving of field profiles."""
    layer, friqrt, profile, inangle, hw0, hw1, hws, h_nm = rf.readin()
    NL, L, n = rf.readlayer(layer)

    z = 0
    zcoord = []
    while z <= sum(L[1:NL+1]):
        zcoord.append(z)
        z = z + h_nm

    E1 = np.zeros([ len(zcoord), len(eigenfreq) + 1])
    for i in range(len(zcoord)):
        E1[[i],[0]] = zcoord[i]

    for eg in range(len(eigenfreq)):
        k0 = 0.005067731239*eigenfreq[eg]
        z = 0
        j = 0
        M0 = np.array([[E0[eg]],[E0[eg]*r1[eg] + El[eg]*ts1[eg]]], dtype = np.complex)
        # run through all layers
        for i in range(1, NL + 1, 1):
            SLI = sum(L[1:i])           # coord start layer i
            ELI = sum(L[1:i+1])         # coord end layer i
            while z <= ELI:
                M = np.dot(np.dot(M1(n[i], z - SLI, k0), M2(n[i-1],n[i])), M0)
                E1[[j],[eg + 1]] = np.real(M[0, 0] + M[1, 0])
                z = z + h_nm
                j = j + 1
            M0 = M

    np.savetxt("data/" + profile + ".dat", E1)

    return E1


def R(Bar):
    """Calculation of reflection and transmission coefficients for a given frequency range."""
    layer, friqrt, profile, inangle, hw0, hw1, hws, h_nm = rf.readin()
    NL, L, n = rf.readlayer(layer)

    # calc r1, t1, rs1, ts1
    eigenfreq, r1, t1, rs1, ts1 = [], [], [], [], []
    h = 0.01 * hws
    w = hw0
    niter = int((hw1 - hw0)/h)
    i = 0
    while w <= hw1:
        eigenfreq.append(w)
        r, t, rs, ts = fun(NL, L, n, w, 3)
        r1.append(np.round(r, 16))
        t1.append(np.round(t, 16))
        rs1.append(np.round(rs, 16))
        ts1.append(np.round(ts, 16))
        i = i + 1
        w = w + h
        Bar.setProperty("value", i/niter * 100)

    Bar.setProperty("value", 0)

    return r1, t1, rs1, ts1, eigenfreq


