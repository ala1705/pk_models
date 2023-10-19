import numpy as np
import scipy
from model import Model

#
# Intravenous class
#


class Intravenous(Model):
    """This describes the Intravenous model implementation for the compartments and equations
    """

    def __init__(self, clearance_rate: float, dose_rate: float, V_c: float, num_peripheries: int, V_p_list: list[float],
                 Q_p_list: list[float]):
        super().__init__(clearance_rate, dose_rate, V_c, num_peripheries, V_p_list, Q_p_list)

    def add_compartments(self) -> None:
        super().add_compartments()

    def rhs_ode(self, t: np.array, y: list[np.array]):
        """This method returns a list of right-hand sides for the ODEs defined in the intravenous
        model. This will include one central compartment equation and some periphery equations

        :param t: A numpy array of time steps for the problem
        :param y: A list of numpy arrays for each compartment. The first element is the Central data
        and the rest of the elements are Periphery compartments
        :return:
        """
        q_c, q_p_list = y[0], y[1:]

        # This is adapting prototype.py to make a list of transitions for each periphery compartment
        # instead of just one transition, using a list comprehension
        transition_list = [self.Q_p_list[i] * (q_c / self.V_c - q_p_list[i] / self.V_p_list[i])
                           for i in range(len(q_p_list))]

        # The central compartment ODE
        dqc_dt = self.dose_rate - q_c / self.V_c * self.CL - sum(transition_list)

        # A list of periphery compartment ODEs
        dqp_dt_list = transition_list
        return [dqc_dt] + dqp_dt_list

    def solve_equations(self) -> dict:
        """Here we use the Intravenous ODE model to solve the problem

        :return: A dictionary of numpy arrays containing the amount of drug in each compartment for each time step
        """
        # Here we set up the time steps, and we set all initial compartment drug amount to zero
        t_eval = np.linspace(0, 1, 1000)

        # This contains initial data for all the peripheries
        y0 = np.array([0.0] * (1 + self.num_peripheries))

        solution = scipy.integrate.solve_ivp(
            fun=lambda t, y: self.rhs_ode(t, y),
            t_span=[t_eval[0], t_eval[-1]],
            y0=y0, t_eval=t_eval
        )
        print(len(solution.y))

        # This returns the solution as a dictionary containing the time steps and the
        # different drug amounts over time for each compartment
        return {"t": solution.t, "Central": solution.y[0], "Peripheries": solution.y[1:]}