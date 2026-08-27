import numpy as np
E = lambda n: -13.6/n/n #eV
hbar = 6.582e-16 #eV s
alpha = 1/137
c = 299792458 #m/s
m_e = 510.998e3 #eV
k_B = 8.617e-5 #eV/K
eV_to_J = 1.602*10**(-19)
e_0 = 8.85418782*10**(-12)#farad / m  - eller s^4*A^2/kg/m^3
e = 1.60217663 * 10**(-19)  #coulomb
a_0 = 5.29 * 10**(-11)

r = 256/243/np.sqrt(2) * a_0
B = (256/243/np.sqrt(2))**2 * 4*np.pi**2 * c**3 * hbar / (3 * m_e**2 * alpha)
print("Problem 1:")
print(f"{B = :.4f} m^3 eV^-1 s^-2")
print(f"B = {B/(eV_to_J) :.4e} m^3 J^-1 s^-2")

print("\nProblem 2:")
T = 2000 #K
w_ba = (E(2) - E(1))/hbar
print(f"{w_ba = :.4e} s^-1")
rho = hbar*w_ba**3/(np.pi**2*c**3) * 1/(np.exp(hbar*w_ba/(k_B * T)) - 1)
print(f"{rho = :.4e} eV s m^-3")

I = rho * c
print(f"{I = :.4e} eV m^-2")

print("\nProblem 3:")
# W_ba = 4/3 * (256/(243 * np.sqrt(2)))**2 * w_ba**3 * hbar**2 / m_e**2 / alpha
Rate = B * rho
print(r"Absorption transition rate \dot N_ba / N_a = B_ba \rho(\omega_ba)")
print(f"\t{Rate = :.4e} s^-1")


print("\nProblem 4:")
#intensitet P/A, dimensionsanalyse sammenlignet med tidligere skal vi gange med en tid så maybe 1/\omega?
#dk hvad relative bandwidth er / skal bruges til though
P = 0.001   #J/s
A = 0.0005**2 * np.pi #m^2
I = P/A       #W/m^2
I_spectral = I / w_ba  /10**(-7)#J/m^2
print(f'Spectral intensity {I_spectral = :.4e} J/m^2')

Rate = B * I_spectral / c / eV_to_J
print(f"\t{Rate = :.4e} s^-1")


print("\nProblem 5:")
#fra 4.4 t = sqrt(2ce_0/I_l) * m\omega_L / e * sqrt(|c_b(t)|^2 * |M(\omega_L)|^2)
#for perfect on resonance vil matrixelement være max altså bare 1? Har \omega_L=\omega_ba hvertfald
M = -m_e / c**2 * w_ba /hbar * r   #4.70
# M = 1
t = np.sqrt(2*c*e_0 / I) * m_e /c**2 * eV_to_J * w_ba / e * np.sqrt(1/np.exp(1) * M**2)

print(f'{t = :.4e} s')
