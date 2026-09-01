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


print("Problem 3)")
f_3p2s, f_3p1s = 0.435, 0.0792
f_2s3p = -1/3 * f_3p2s
f_1s3p = -1/3 * f_3p1s

rt3p = 2*hbar*alpha/m_e * (w_(2,3)**2 * abs(f_2s3p) + w_(1,3)**2 * abs(f_1s3p))
t = 1/rt3p
print(f"{t = :.4e} s (5.4 ns from table)")

print("\nProblem 4)")
f_4s3p, f_4s2p = 0.0322, 0.00305
f_3p4s = -3/1 * f_4s3p
f_2p4s = -3/1 * f_4s2p

rt4s = 2*hbar*alpha/m_e * (w_(3,4)**2 * abs(f_3p4s) + w_(2,4)**2 * abs(f_2p4s))
t = 1/rt4s
print("4s state:")
print(f"{t = :.4e} s (230 ns from table)")


f_4p1s, f_4p2s, f_4p3s, f_4p3d = 0.029, 0.103, 0.485, 0.011
f_1s4p = -1/3 * f_4p1s
f_2s4p = -1/3 * f_4p2s
f_3s4p = -1/3 * f_4p3s
f_3d4p = -5/3 * f_4p3d
rt4p = 2*hbar*alpha/m_e * (w_(1,4)**2 * abs(f_1s4p) + w_(2,4)**2 * abs(f_2s4p) + w_(3,4)**2 * abs(f_3s4p) + w_(3,4)**2 * abs(f_3d4p))
t = 1/rt4p

print("4p state:")
print(f"{t = :.4e} s (12.4 ns from table)")
