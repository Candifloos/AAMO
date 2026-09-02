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

print("Problem 1)")
tau = 1.6*10**(-9) #s
Gamma = hbar / tau 
print(f"{Gamma = :.4e} eV ")

print("\nProblem 2)")
T = 300 #K
m = 938.95*10**6      #eV  
p = 6.242*10**23      # eV/m^3

sigma = np.pi * a_0**2
v = np.sqrt(2*k_B*T/m * c**2)
n = p/(k_B*T)

W_c = n * sigma * v 
print(f"{W_c = :.4e} s^-1 ")
Gamma = W_c * hbar
print(f"{Gamma = :.4e} eV ")


print("\nProblem 3)")
