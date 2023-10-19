"""Plot graphs"""

import matplotlib.pylab as plt
import numpy as np
import scipy.integrate


def plot(data):
    t = data["t"]
    q_c = data["Central"]
    plt.plot(t, q_c, label="q_c")

    if "Peripheries" in data:

        q_p = data["Peripheries"]

        i = 1
        for p in q_p:
            plt.plot(t, p, label="q_p"+str(i))
            i += 1

    if "Dose" in data:

        q_d = data["Dose"]
        plt.plot(t, q_d, label="q_d")

    plt.legend()
    plt.ylabel('drug mass [ng]')
    plt.xlabel('time [h]')
    plt.show()
