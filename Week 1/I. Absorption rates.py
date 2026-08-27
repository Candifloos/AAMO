import numpy as np
E = lambda n: -13.6/n/n #eV
hbar = 6.582e-16 #eV s
alpha = 1/137
c = 299792458 #m/s
m_e = 510.998e3 #eV
k_B = 8.617e-5 #eV/K


B = (256/243/np.sqrt(2))**2 * 4*np.pi**2 * c**3 * hbar / (3 * m_e**2 * alpha)
print("Problem 1:")
print(f"{B = :.4f} m^3 eV^-1 s^-2")
print(f"B = {B/(1.6022e-19) :.4e} m^3 J^-1 s^-2")

print("\nProblem 2:")
T = 2000 #K
w_ba = (E(2) - E(1))/hbar
print(f"{w_ba = :.4e} s^-1")
rho = hbar*w_ba**3/(np.pi**2*c**3) * 1/(np.exp(hbar*w_ba/(k_B * T)) - 1)
print(f"{rho = :.4e} eV s m^-3")

I = rho * c
print(f"{I = :.4e} eV m^-2")

print("\nProblem 3:")
W_ba = 4/3 * (256/(243 * np.sqrt(2)))**2 * w_ba**3 * hbar**2 / m_e**2 / alpha
print(f"Absorption transition rate \dot N_ba = W_ba")
print(f"\t{W_ba = :.4e} s^-1")
