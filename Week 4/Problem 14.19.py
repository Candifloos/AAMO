import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sco

thf_i = lambda thf, thi: np.cos(thf) - np.cos(thi) + (thf - thi) * np.sin(thi)

thf = lambda thi: sco.root(thf_i, thi + 1.3 * np.pi, args=thi)["x"][0]


E = lambda thi: 2 * (np.sin(thf(thi)) - np.sin(thi))**2

this = np.linspace(0,np.pi/2,100)
fig, ax = plt.subplots()

Es = [E(thi) for thi in this]
ax.plot(this, Es)
print(f"Max of function: {max(Es):.3f}")


plt.show()