#
# Model class
#

class Model:
    """A Pharmokinetic (PK) model
    This is the base class, which will always contain one central compartment and 0-2 periphery
    compartments. The `Intravenous` and `Subcutaneous` Models will inherit from this class, implementing
    their own versions of the `add_compartments` and `add_equations` methods.


    """
    def __init__(self, clearance_rate: float, dose_rate: float,
                 V_c: float, num_peripheries: int, V_p_list: list[float], Q_p_list: list[float]):
        """

        :param clearance_rate: The constant clearance rate from the central compartment
        :param dose_rate: The constant dose rate into the central compartment
        :param V_c: The constant volume of the central compartment
        :param num_peripheries: The number of periphery compartments (0-2 inclusive)
        :param V_p_list: The list of volumes of the different periphery compartments
        :param Q_p_list: The list of transition rates between the central compartment and each periphery
        compartment

        """
        if clearance_rate is float and dose_rate is float and V_c is float:
            self.CL = clearance_rate
            self.dose_rate = dose_rate
            self.V_c = V_c
        else:
            raise TypeError("Input fluxes and volumes must be floats")

        if num_peripheries is int:
            if 0 <= num_peripheries <= 2:
                self.num_peripheries = num_peripheries
            else:
                raise ValueError("num_peripheries must lie between 0 and 2 inclusive")
        else:
            raise TypeError("num_peripheries must be an int")

        if V_p_list is list[float] and Q_p_list is list[float]:
            if len(V_p_list) == num_peripheries and len(Q_p_list) == num_peripheries:
                self.V_p_list = V_p_list
                self.Q_p_list = Q_p_list
            else:
                raise ValueError("There must be exactly", self.num_peripheries,
                                 "periphery volumes and fluxes each")
        else:
            raise TypeError("Input rates and volumes must be floats")

        self.compartments = self.add_compartments()
        self.equations = self.add_equations()

    def add_compartments(self) -> dict[str, Compartment]:
        """The general model will add a `Central` compartment and a number of `Periphery` compartments

        :return: A dictionary keyed by the name of the `Compartment` containing each compartment
        """
        self.compartments["Central"] = Central(self.V_c)

        for i in range(self.num_peripheries):
            volume = self.V_p_list[i]
            transition_rate = self.Q_p_list[i]
            self.compartments["Periphery " + str(i + 1)] = Periphery(volume, transition_rate)

    def add_equations(self) -> dict[str, float]:
        pass

