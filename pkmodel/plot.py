"""Plot graphs"""

import matplotlib.pylab as plt
import numpy as np
import scipy.integrate


def plot(data):

    """function to plot model outcome and save plots

    Args:
        data (dict): dictionary storing all plot data
    """


    t = data["t"]
    
    q_c = data["Central"]
    plt.plot(t, q_c, label="Central")

    if "Peripheries" in data:

        q_p = data["Peripheries"]

        i = 1
        for p in q_p:
            plt.plot(t, p, label="Peripheral "+str(i))
            i += 1

    model_name = "Intravenous"

    if "Dose" in data:

        q_d = data["Dose"]
        plt.plot(t, q_d, label="Dose")
        model_name = "Subcutaneous"

    plt.legend()
    plt.ylabel('drug mass [ng]')
    plt.xlabel('time [h]')

    plt.title("Drug Mass against Time within Drug Compartments for the "+model_name+" Model")

    plt.savefig("comparison_plot.png")
    plt.show()


