import numpy as np
import scipy
from model import Model

#
# Subcutaneous class
#
from pkmodel.compartment import Dose


class Subcutaneous(Model):
    """This describes the Subcutaneous model implementation for the compartments and equations
    """

    def __init__(self, clearance_rate: float, dose_rate: float, V_c: float, num_peripheries: int, V_p_list: list[float],
                 Q_p_list: list[float], V_0, absorption_rate: float):
        """
        :param V_0: The volume of the Dose compartment
        :param absorption_rate: The rate at which the substance is absorbed from the 
        Dose compartment to the Central compartment
        """
        # Checks for the dose compartment
        if isinstance(V_0, float) and isinstance(absorption_rate, float):
            if V_0 > 0 and absorption_rate >= 0:
                self.V_0 = V_0
                self.k_a = absorption_rate
            else:
                raise ValueError("Fluxes must be non-negative and volumes must be positive")
        else:
            raise TypeError("Dose compartment volume and absorption rate must be floats")

        super().__init__(clearance_rate, dose_rate, V_c, num_peripheries, V_p_list, Q_p_list)

    def add_compartments(self) -> None:

        # For the Subcutaneous model, we must also add a Dose compartment
        super().add_compartments()
        self.compartments["Dose"] = Dose(self.V_0, self.k_a)

    def rhs_ode(self, t: np.array, y: list[np.array]):
        """This method returns a list of right-hand sides for the ODEs defined in the intravenous
        model. This will include one central compartment equation and some periphery equations

        :param t: A numpy array of time steps for the problem
        :param y: A list of numpy arrays for each compartment. The first element is for the Dose compartment,
        the second is for the Central compartment and the last elements are for Periphery data
        :return:
        """
        q_0, q_c, q_p_list = y[0], y[1], y[2:]

        # This is adapting prototype.py to make a list of transitions for each periphery compartment
        # instead of just one transition, using a list comprehension
        transition_list = [self.Q_p_list[i] * (q_c / self.V_c - q_p_list[i] / self.V_p_list[i])
                           for i in range(len(q_p_list))]

        # The dose compartment ODE
        dq0_dt = self.dose_rate - self.k_a * q_0

        # The central compartment ODE
        dqc_dt = self.k_a * q_0 - q_c / self.V_c * self.CL - sum(transition_list)

        # A list of periphery compartment ODEs
        dqp_dt_list = transition_list
        return [dq0_dt] + [dqc_dt] + dqp_dt_list

    def solve_equations(self) -> dict:
        """Here we use the Intravenous ODE model to solve the problem

        :return: A dictionary of numpy arrays containing the amount of drug in each compartment for each time step
        """
        # Here we set up the time steps, and we set all initial compartment drug amount to zero
        t_eval = np.linspace(0, 1, 1000)

        # This must contain initial data for all the peripheries
        y0 = np.array([0.0] * (2 + self.num_peripheries))

        solution = scipy.integrate.solve_ivp(
            fun=lambda t, y: self.rhs_ode(t, y),
            t_span=[t_eval[0], t_eval[-1]],
            y0=y0, t_eval=t_eval
        )

        # This returns the solution as a dictionary containing the time steps and the
        # different drug amounts over time for each compartment
        return {"t": solution.t, "Dose": solution.y[0], "Central": solution.y[1],
                "Peripheries": solution.y[2:]}
