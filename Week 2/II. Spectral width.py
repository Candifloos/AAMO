import numpy as np  
E = lambda n: -13.6/n/n #eV
hbar = 6.582e-16 #eV s
w_ = lambda n1,n2: (E(n1) - E(n2))/hbar
alpha = 1/137
c = 299792458 #m/s
m_e = 510.998e3 #eV
k_B = 8.617e-5 #eV/K
eV_to_J = 1.602*10**(-19)
e_0 = 8.85418782*10**(-12)#farad / m  - eller s^4*A^2/kg/m^3
e = 1.60217663 * 10**(-19)  #coulomb
a_0 = 5.29 * 10**(-11)

print("Problem 1 - Natural linewidth)")
tau = 1.6*10**(-9) #s
Gamma = hbar / tau 
print(f"{Gamma = :.4e} eV ")

print("\nProblem 2 - Pressure broadening)")
T = 300 #K
m = 938.95*10**6      #eV  
p = 6.242*10**23      # eV/m^3

sigma = np.pi * a_0**2
# v = np.sqrt(2*k_B*T/m * c**2)
v = np.sqrt(8*k_B*T/(np.pi * m) * c**2) #average speed
n = p/(k_B*T)

W_c = n * sigma * v 
print(f"{W_c = :.4e} s^-1 ")
Gamma = W_c * hbar
print(f"{Gamma = :.4e} eV ")


print("\nProblem 3 - Doppler broadening)")
W_D = 2*w_(2,1) * np.sqrt(2*k_B*T/m * np.log(2))
print(f"{W_D = :.4e} s^-1 ")
Gamma = W_D * hbar
print(f"{Gamma = :.4e} eV ")

print("\nProblem 4 - Power broadening)")
W_P = 1.16e6 #1/s (from problem I)
print(f"{W_P = :.4e} s^-1")
Gamma = W_P * hbar
print(f"{Gamma = :.4e} eV")

#Pulsed laser from 'I. Absorption rates.py'
print("\nPulsed laser:")
B = (256/243/np.sqrt(2))**2 * 4*np.pi**2 * c**3 * hbar / (3 * m_e**2 * alpha)
P = 1e-3/1e-9   #J/s
A = 0.0005**2 * np.pi #m^2
I = P/A       #W/m^2
I_spectral = I / w_(2,1)  /10**(-5)#J/m^2
print(f'Spectral intensity {I_spectral = :.4e} J/m^2')

Rate = B * I_spectral / c / eV_to_J
print(f"\t{Rate = :.4e} s^-1")
Gamma = Rate * hbar
print(f"{Gamma = :.4e} eV")