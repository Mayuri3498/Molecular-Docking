import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

r = pd.read_csv("mdpout_descriptors.csv")
y = r["pock_volume"].values
x = np.arange(len(y))

ylim = (2000, 4000)

plt.plot(x, y, linestyle='-', color='blue')

if len(y) > 3:
    spline = UnivariateSpline(x, y, s=40)
    xs = np.linspace(x.min(), x.max(), 500)
    y_smooth = spline(x)
    plt.plot(x, y_smooth, color="red", linewidth=3)

plt.ylim(ylim)
plt.xlim(x.min(), x.max())
plt.xlabel("snapshot")
plt.ylabel("volume")

plt.tight_layout()
plt.savefig("pocket_volume.jpeg", dpi=300, format="jpeg")