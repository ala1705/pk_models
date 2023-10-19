#
# Model class
#
import numpy as np

from pkmodel.compartment import Central, Periphery


class Model:
    """A Pharmokinetic (PK) model
    This is the base class, which will always contain one central compartment and 0-2 periphery
    compartments. The `Intravenous` and `Subcutaneous` Models will inherit from this class, implementing
    their own versions of the `add_compartments` and `solve_equations` methods.


    """

    def __init__(self, clearance_rate: float = 1.0, dose_rate: float = 1.0,
                 V_c: float = 1.0, num_peripheries: int = 1, V_p_list: list[float] = None,
                 Q_p_list: list[float] = None):
        """

        :param clearance_rate: The constant clearance rate from the central compartment
        :param dose_rate: The constant dose rate into the central compartment
        :param V_c: The constant volume of the central compartment
        :param num_peripheries: The number of periphery compartments (0-2 inclusive)
        :param V_p_list: The list of volumes of the different periphery compartments
        :param Q_p_list: The list of transition rates between the central compartment and each periphery
        compartment

        """

        # Checks for the clearance_rate, dose_rate and central volume
        if isinstance(clearance_rate, (float, int)) and isinstance(dose_rate, (float, int)) \
                and isinstance(V_c, (float, int)):
            if clearance_rate >= 0 and dose_rate >= 0 and V_c > 0:
                self.CL = float(clearance_rate)
                self.dose_rate = float(dose_rate)
                self.V_c = float(V_c)
            else:
                raise ValueError("Fluxes cannot be negative and volumes must be positive")
        else:
            raise TypeError("Input fluxes and volumes must be floats")

        # Checks for the number of peripheries
        if isinstance(num_peripheries, int):
            if 0 <= num_peripheries <= 2:
                self.num_peripheries = num_peripheries
            else:
                raise ValueError("num_peripheries must lie between 0 and 2 inclusive")
        else:
            raise TypeError("num_peripheries must be an int")

        # Checks for the periphery volumes and fluxes

        # IMPORTANT: If the user has provided no values for V_p_list or Q_p_list, then we will
        # initialise these lists with default values. The length of these lists will be
        # num_peripheries
        if V_p_list is None:
            V_p_list = [1.0] * num_peripheries
        if Q_p_list is None:
            Q_p_list = [1.0] * num_peripheries

        # Check that the length of lists are correct, that they are of the correct type and are
        # within a valid range
        if len(V_p_list) == num_peripheries and len(Q_p_list) == num_peripheries:

            for i in range(num_peripheries):
                if not isinstance(V_p_list[i], (float, int)) or not isinstance(Q_p_list[i], (float, int)):
                    raise TypeError("Input rates and volumes must be floats")
                else:
                    V_p_list[i], Q_p_list[i] = float(V_p_list[i]), float(Q_p_list[i])

            invalid_values = [vol for vol in V_p_list if vol <= 0] + [flux for flux in Q_p_list if flux < 0]

            # If there are no invalid values, then we can set the lists
            if len(invalid_values) == 0:
                self.V_p_list = V_p_list
                self.Q_p_list = Q_p_list
            else:
                raise ValueError("Fluxes cannot be negative and volumes must be positive")

        else:
            raise ValueError("There must be exactly " + str(self.num_peripheries) +
                             " periphery volumes and fluxes each")

        self.compartments = {}
        self.add_compartments()

    def add_compartments(self) -> None:
        """The general model will add a `Central` compartment and a number of `Periphery` compartments
        """
        self.compartments["Central"] = Central(self.V_c)
        self.compartments["Peripheries"] = []

        for i in range(self.num_peripheries):
            # For each periphery, we get its inputted volume and transition_rate, and then create a new
            # dictionary entry for each periphery
            V_p_i = self.V_p_list[i]
            Q_p_i = self.Q_p_list[i]
            self.compartments["Peripheries"].append(Periphery(V_p_i, Q_p_i))

    def solve_equations(self) -> dict:
        """Here we will solve the equations for the given model, but we don't wish for this to be ever called from this
        base class, so raise a NotImplementedError if this method is called!
        """
        raise NotImplementedError("Cannot call `solve_equations` from Model base class, must do so from a subclass")

    def rhs_ode(self, t: np.array, y: list[np.array]):
        """We leave the implementation to subclasses, so raise a NotImplementedError here
        """
        raise NotImplementedError("Cannot call `rhs` from Model base class, must do so from a subclass")
