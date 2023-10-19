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
        q_c, q_p_list = y[0], y[1:]

    def solve_equations(self) -> dict:
        """Here we use the Intravenous ODE model to solve the problem

        :return: A dictionary of numpy arrays containing the amount of drug in each compartment for each time step
        """
        # Here we set up the time steps, and we set all initial compartment drug amount to zero
        t_eval = np.linspace(0, 1, 1000)
        y0 = np.array([0.0, 0.0])

        solution = scipy.integrate.solve_ivp(
            fun=lambda t, y: self.rhs_ode(t, y),
            t_span=[t_eval[0], t_eval[-1]],
            y0=y0, t_eval=t_eval
        )

        # This returns the solution as a dictionary containing the time steps and the
        # different drug amounts over time for each compartment
        return {"t": solution.t, "Central": solution.y[0], "Peripheries": solution.y[1:]}
