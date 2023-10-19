"""Plot graphs"""

import matplotlib.pylab as plt
import numpy as np
import scipy.integrate
import os
import time


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

    plt.title("Drug Quantity over Time: "+model_name+" Model")

    plot_folder = "plots"

    if not os.path.exists(plot_folder):
        os.makedirs(plot_folder)

    time_string = str(time.strftime("%H%M%S"))

    destination = plot_folder+"/"+model_name.lower()+time_string+".png"
    plt.savefig(destination)
    plt.show()



