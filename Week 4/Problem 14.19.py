import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sco

plt.rc("axes", labelsize=30, titlesize=32)   # skriftstørrelse af xlabel, ylabel og title
plt.rc("xtick", labelsize=26, top=True, direction="in")  # skriftstørrelse af ticks, vis også ticks øverst og vend ticks indad
plt.rc("ytick", labelsize=26, right=True, direction="in") # samme som ovenstående
plt.rc("legend", fontsize=26) # skriftstørrelse af figurers legends
plt.rcParams["font.size"] = "20"
plt.rcParams["figure.figsize"] = (16,8)

thf_i = lambda thf, thi: np.cos(thf) - np.cos(thi) + (thf - thi) * np.sin(thi)

thf = lambda thi: sco.root(thf_i, thi + 1.3 * np.pi, args=thi)["x"][0]


E = lambda thi: 2 * (np.sin(thf(thi)) - np.sin(thi))**2

this = np.linspace(0,np.pi/2,1000)
Es = [E(thi) for thi in this]
fig, ax = plt.subplots()
ax.set(xlabel="$\\theta_i$", ylabel="$E/U_P$")

ax.plot(this, Es)
ax.grid()
print(f"Max of function: {max(Es):.3f}")

fig, ax = plt.subplots()
ax.set(xlabel="$\\theta_i$", ylabel="$\\theta_f$")
thfs = [thf(thi) for thi in this]
ax.plot(this, thfs)


ax.set_yticks(ticks = np.arange(0,2*np.pi+0.1, np.pi/4), labels=[f"{i}π/4" for i in range(9)])
ax.set_xticks(ticks = np.arange(0,np.pi/2+0.01, np.pi/4), labels=[f"{i}π/4" for i in range(3)])
ax.grid()   
plt.show()