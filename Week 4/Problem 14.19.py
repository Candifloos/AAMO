import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sco

plt.rc("axes", labelsize=20, titlesize=22)   # skriftstørrelse af xlabel, ylabel og title
plt.rc("xtick", labelsize=16, top=True, direction="in")  # skriftstørrelse af ticks, vis også ticks øverst og vend ticks indad
plt.rc("ytick", labelsize=16, right=True, direction="in") # samme som ovenstående
plt.rc("legend", fontsize=20) # skriftstørrelse af figurers legends
plt.rcParams["font.size"] = "20"
plt.rcParams["figure.figsize"] = (8,5)

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


piLabels = ["0", "π/4", "π/2", "3π/4", "π", "5π/4", "3π/2", "7π/4", "2π"]
ax.set_yticks(ticks = np.arange(0,2*np.pi+0.1, np.pi/4), labels=piLabels[:9])
ax.set_xticks(ticks = np.arange(0,np.pi/2+0.01, np.pi/4), labels=piLabels[:3])
ax.grid()   
plt.show()