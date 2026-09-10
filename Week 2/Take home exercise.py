import numpy as np
import scipy.integrate as scsi
import matplotlib.pyplot as plt
E = lambda n: -13.6/n/n #eV
hbar = 6.582e-16 #eV s
w_ba = lambda n1,n2: (E(n1) - E(n2))/hbar
alpha = 1/137
c = 299792458 #m/s
m_e = 510.998e3 #eV
m_H = 939e6 #eV
k_B = 8.617e-5 #eV/K
eV_to_J = 1.602*10**(-19)
e_0 = 8.85418782*10**(-12) * eV_to_J #C / eVm  - eller s^4*A^2/kg/m^3
e = 1.60217663 * 10**(-19)  #coulomb
a_0 = 5.29 * 10**(-11) #m


print("Problem 1)")
f_3s2p = 0.0139
f_2p3s = -3/1 * f_3s2p
rt3s = 2*hbar*alpha/m_e * w_ba(3,2)**2 * abs(f_2p3s)
t = 1/rt3s
print(f"{t = :.4e} s (160 ns from table)")

print("\nProblem 4)")
z_ab = 256/243/np.sqrt(2) * a_0
f_ab = 2*m_e*w_ba(2,1)/(3 * hbar * c*c) * z_ab**2 * 3 #factor 3 from f_x + f_y + f_z

print(f"{f_ab = :.4f}")

print("\nProblem 5)")
I = 5e8 / eV_to_J #eV/m^2
I_ba = I/1.8e10 #eV/m^2/s^2
W_ba = 4*np.pi**2/c/hbar/hbar * (e**2/(4 * np.pi * e_0)) * I_ba * 4*np.pi/3 * z_ab**2
print(f"{W_ba = :.4e} s^-1")


# dP = lambda t,P: W_ba * np.array([- P[0] + P[1], P[0] - P[1] * (1 + 6.27e8/W_ba)]) #Including spontaneous emission
dP = lambda t,P: W_ba * np.array([- P[0] + P[1], P[0] - P[1]])
sol = scsi.solve_ivp(dP, t_span = [0,10/W_ba], y0 = [1,0])

c_2p = lambda t: 2*np.pi*e**2/(3 * c * e_0 * hbar**2) * I * z_ab**2 * t**2
t_plot = np.linspace(sol.t[0], sol.t[-1],1000)
dc_2p = lambda t: 2*np.pi*e**2/(3 * c * e_0 * hbar**2) * I * z_ab**2 * t * 2
# print(f"c_2p[-1] = {c_2p(t_plot[-1])}")
# print(f"dc_2p[-1] = {dc_2p(t_plot[-1])}")



print("\nProblem 9)")
F = lambda t: np.sqrt(2 * I/c/e_0) * np.sin(w_ba(2,1) * t) #on resonance
dc = lambda t, c: np.array([-1j * F(t)/hbar * c[1] * np.exp(-1j*w_ba(2,1)*t)*e*z_ab,
                            -1j * F(t)/hbar * c[0] * np.exp( 1j*w_ba(2,1)*t)*e*z_ab])
sol9 = scsi.solve_ivp(dc, t_span = [0,0.1e-9], y0 = [1 + 0j,0 + 0j], rtol=3e-5, atol=1e-8)
c_1s2 = np.abs(sol9.y[0,:])**2
c_2p2 = np.abs(sol9.y[1,:])**2


fig, ax = plt.subplots()
ax.set(xlabel="Time [s]", ylabel = "Population", title="Excitation from 1s to 2p")
ax.plot(sol.t, sol.y[0,:], label="rate $P_{1s}$")
ax.plot(sol.t, sol.y[1,:], label="rate $P_{2p}$")

ax.plot(t_plot, c_2p(t_plot), label="perturb. monochromatic")

ax.plot(sol9.t, c_1s2, label="9) $|c_{1s}|^2$")
ax.plot(sol9.t, c_2p2, label="9) $|c_{2p}|^2$")

ax.legend()
ax.grid()
ax.axvline(1/W_ba, color="grey", linestyle="--")
plt.show()