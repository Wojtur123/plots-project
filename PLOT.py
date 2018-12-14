import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


def plot(filename):
    tab = np.loadtxt(filename)
    x = tab[:, 0]
    y = tab[:, 1]
    plt.xlabel("x - squared period of oscillations")
    plt.ylabel(r"y - product of mass and 4$\Pi^2$")
    a, b, r, _, da = linregress(x, y)
    basis = np.linspace(min(x), max(x), 5000)
    plt.plot(basis, basis * a + b)

    plt.errorbar(x, y, marker='+', ls='', markersize=10)

    legend = plt.legend()
    legend.draggable()
    plt.tight_layout()
    plt.show()
    plt.savefig()


plot("data.txt")