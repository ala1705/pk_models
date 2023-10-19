"""Plot graphs"""

import matplotlib.pylab as plt
import os
import time


def plot(data: dict, title: str = None):

    """function to plot model outcome and save plots

    Args:
        data (dict): dictionary storing all plot data
        title (str): optional title for the output png doc
    """

    t = data["t"]

    q_c = data["Central"]
    plt.plot(t, q_c, label="Central")

    if "Peripheries" in data:

        q_p = data["Peripheries"]

        i = 1
        for p in q_p:
            plt.plot(t, p, label="Peripheral " + str(i))
            i += 1

    model_type = "Intravenous"

    if "Dose" in data:

        q_d = data["Dose"]
        plt.plot(t, q_d, label="Dose")
        model_type = "Subcutaneous"

    plt.legend()
    plt.ylabel('drug mass [ng]')
    plt.xlabel('time [h]')

    plt.title("Drug Quantity over Time: "+model_type+" Model")

    plot_folder = "plots"

    if not os.path.exists(plot_folder):
        os.makedirs(plot_folder)

    if title is None:
        title = str(time.strftime("%H%M%S"))

    destination = plot_folder + "/" + model_type.lower() + "_" + title + ".png"
    plt.savefig(destination)
    plt.show()
