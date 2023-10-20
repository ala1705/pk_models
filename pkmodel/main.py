from intravenous import Intravenous
from subcutaneous import Subcutaneous
from plot import plot


def run_model(model_type: str, clearance: float, dose_rate: float, dose_on: int, dose_off: int,
              V_central: float, n_peripheries: int, V_peripheries: list[float], Q_peripheries: list[float],
              drug_volume: float, drug_absorption: float, run_time: float, time_step: float,
              plot_folder: str, title: str):
    """Runs the model. This function is called by simulation.py
    """
    if model_type == "Intravenous":
        model = Intravenous(clearance_rate=clearance, dose_per_time_step=dose_rate, dose_on=dose_on,
                            dose_off=dose_off, V_c=V_central, num_peripheries=n_peripheries,
                            V_p_list=V_peripheries, Q_p_list=Q_peripheries, run_time=run_time,
                            time_step_length=time_step)
        results = model.solve_equations()
        plot(data=results, plot_folder=plot_folder, title=title)

    elif model_type == "Subcutaneous":
        model = Subcutaneous(clearance_rate=clearance, dose_per_time_step=dose_rate, dose_on=dose_on,
                             dose_off=dose_off, V_c=V_central, num_peripheries=n_peripheries,
                             V_p_list=V_peripheries, Q_p_list=Q_peripheries, V_0=drug_volume,
                             absorption_rate=drug_absorption, run_time=run_time,
                             time_step_length=time_step)
        results = model.solve_equations()
        plot(data=results, plot_folder=plot_folder, title=title)

#     # Some manual testing cases - Basic arguments
#
#
# intravenous_model_1 = Intravenous(1.0, 10.0, 1, 1, 1.0, 2, [1.0, 2.0], [1.0, 3.0], 1, 60)
# subcutaneous_model_1 = Subcutaneous(1.0, 1.0, 1, 1, 1.0, 2, [1.0, 2.0], [1.0, 3.0], 1.0, 1.0, 1, 60)
#
# results_intravenous_1 = intravenous_model_1.solve_equations()
# results_subcutaneous_1 = subcutaneous_model_1.solve_equations()
# plot(results_intravenous_1, "standard_two_peripheries")
# plot(results_subcutaneous_1, "standard_two_peripheries")
#
# # Default values
# intravenous_model_2 = Intravenous(clearance_rate=0, num_peripheries=0, time_step_length=60)
# subcutaneous_model_2 = Subcutaneous()
#
# results_intravenous_2 = intravenous_model_2.solve_equations()
# results_subcutaneous_2 = subcutaneous_model_2.solve_equations()
# plot(results_intravenous_2, "all_defaults")
# plot(results_subcutaneous_2, "all_defaults")
#
# # Setting dosage only to zero
# intravenous_model_3 = Intravenous(clearance_rate=1, dose_per_time_step=0, Q_p_list=[2.0])
# subcutaneous_model_3 = Subcutaneous(clearance_rate=1, dose_per_time_step=0, Q_p_list=[2.0], absorption_rate=1.0)
#
# results_intravenous_3 = intravenous_model_3.solve_equations()
# results_subcutaneous_3 = subcutaneous_model_3.solve_equations()
# plot(results_intravenous_3, "zero_dosage")
# plot(results_subcutaneous_3, "zero_dosage")
#
# # Setting clearance_rate to zero
# intravenous_model_4 = Intravenous(clearance_rate=0, dose_per_time_step=1, Q_p_list=[2.0])
# subcutaneous_model_4 = Subcutaneous(clearance_rate=0, dose_per_time_step=1, Q_p_list=[2.0], absorption_rate=1.0)
#
# results_intravenous_4 = intravenous_model_4.solve_equations()
# results_subcutaneous_4 = subcutaneous_model_4.solve_equations()
# plot(results_intravenous_4, "zero_clearance")
# plot(results_subcutaneous_4, "zero_clearance")
#
# # Change run-time and number of time-steps
# intravenous_model_5 = Intravenous(clearance_rate=0, dose_per_time_step=1, Q_p_list=[2.0], run_time=10.0)
# subcutaneous_model_5 = Subcutaneous(clearance_rate=0, dose_per_time_step=1, Q_p_list=[2.0],
#                                     absorption_rate=1.0, time_step_length=20)
#
# results_intravenous_5 = intravenous_model_5.solve_equations()
# results_subcutaneous_5 = subcutaneous_model_5.solve_equations()
# plot(results_intravenous_5, "longer run-time")
# plot(results_subcutaneous_5, "less time-steps")
#
# #
