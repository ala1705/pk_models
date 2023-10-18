# Class for Compartments

class Compartment:
    """Class representing a drug compartment
    """

    def __init__(self, volume, drug_quantity):
        """Initialise compartment class

        Args:
            volume (float): volume of compartment [mL]
            drug_quantity (float): quantity of drug in compartment [ng]
        """

        self.volume = volume
        self.drug_quantity = drug_quantity



class Central(Compartment):
    """Class representing the central drug compartment
    """

    def __init__(self, volume, drug_quantity):
        """Initialise central compartment class

        Args:
            volume (float): volume of compartment [mL]
            drug_quantity (float): quantity of drug in compartment [ng]
        """

        super().__init__(volume, drug_quantity)
        


class Periphery(Compartment):
    """Class representing a periphery drug compartment
    """

    def __init__(self, volume, drug_quantity, transition_rate):
        """Initialize periphery compartment class

        Args:
            volume (float): volume of compartment [mL]
            drug_quantity (float): quantity of drug in compartment [ng]
            transition_rate (float): rate of drug transition between central and peripheral compartment [mL/h]
        """

        super().__init__(volume, drug_quantity)
        self.transition_rate = transition_rate

    def find_transition(self, q_c, V_c):
        """Function to calculate transition expression in diff equation model

        Args:
            q_c (float): drug quantity in central compartment [ng]
            V_c (float): volume of central compartment [mL]

        Returns:
            float: expression for transition rate in diff eq
        """

        return self.transition_rate * ((q_c / V_c) - (self.drug_quantity / self.volume))
    
class Dose(Compartment):
    """Class representing the dose compartment
    """
    
    def __init__(self, volume, drug_quantity, absorption_rate):
        """Initialise dose compartment class

        Args:
            volume (float): volume of compartment [mL]
            drug_quantity (float): quantity of drug in compartment [ng]
        """
        super().__init__(volume, drug_quantity)
        self.absorption_rate = absorption_rate

