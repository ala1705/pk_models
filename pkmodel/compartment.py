# Class for Compartments

class Compartment:

    def __init__(self, volume, drug_quantity):

        self.volume = volume
        self.drug_quantity = drug_quantity



class Central(Compartment):

    def __init__(self, volume, drug_quantity):

        super().__init__(volume, drug_quantity)
        


class Periphery(Compartment):

    def __init__(self, volume, drug_quantity, transition_rate):

        super().__init__(volume, drug_quantity)
        self.transition_rate = transition_rate

    def find_transition(self, q_c, V_c):

        return self.transition_rate * ((q_c / V_c) - (self.drug_quantity / self.volume))



class Dose(Compartment):

    def __init__(self, volume, drug_quantity, absorption_rate):

        super().__init__(volume, drug_quantity)
        self.absorption_rate = absorption_rate

