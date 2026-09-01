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
f_3s2p = 0.0139
f_2p3s = -3/1 * f_3s2p
rt3s = 2*hbar*alpha/m_e * w_(3,2)**2 * abs(f_2p3s)
t = 1/rt3s
print(f"{t = :.4e} s (160 ns from table)")
