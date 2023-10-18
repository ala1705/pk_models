import numpy as np
import scipy
from model import Model

#
# Subcutaneous class
#


class Subcutaneous(Model):
    """This describes the Subcutaneous model implementation for the compartments and equations
    """

    def __init__(self, clearance_rate: float, dose_rate: float, V_c: float, num_peripheries: int, V_p_list: list[float],
                 Q_p_list: list[float], V_d, absorption_rate: float):
        """
        :param V_d: The volume of the Dose compartment
        :param absorption_rate: The rate at which the substance is absorbed from the Dose compartment to the Central compartment
        """
        super().__init__(clearance_rate, dose_rate, V_c, num_peripheries, V_p_list, Q_p_list)

        if V_d is float and absorption_rate is float:
            self.V_d = V_d
            self.k_a = absorption_rate
        else:
            raise TypeError("Dose compartment volume and absorption rate must be floats")

    def add_compartments(self) -> None:

        # For the Subcutaneous model, we must also add a Dose compartment
        super().add_compartments()
        self.compartments["Dose"] = Dose(self.V_d, self.k_a)