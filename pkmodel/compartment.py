# Class for Compartments

class Compartment:
    """Class representing a drug compartment
    """

    def __init__(self, volume):
        """Initialise compartment class

        Args:
            volume (float): volume of compartment [mL]
        """

        self.volume = volume


class Central(Compartment):
    """Class representing the central drug compartment
    """

    def __init__(self, volume):
        """Initialise central compartment class

        Args:
            volume (float): volume of compartment [mL]
        """

        super().__init__(volume)
        

class Periphery(Compartment):
    """Class representing a periphery drug compartment
    """

    def __init__(self, volume, transition_rate):
        """Initialize periphery compartment class

        Args:
            volume (float): volume of compartment [mL]
            transition_rate (float): rate of drug transition between central and peripheral compartment [mL/h]
        """

        super().__init__(volume)
        self.transition_rate = transition_rate

    
class Dose(Compartment):
    """Class representing the dose compartment
    """
    
    def __init__(self, volume, absorption_rate):
        """Initialise dose compartment class

        Args:
            volume (float): volume of compartment [mL]
            absorption_rate (float): rate of drug absorption [/h]
        """
        super().__init__(volume)
        self.absorption_rate = absorption_rate
