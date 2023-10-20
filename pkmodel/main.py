from intravenous import Intravenous
from subcutaneous import Subcutaneous
from plot import plot

# Some manual testing cases - Basic arguments
intravenous_model_1 = Intravenous(1.0, 10.0, 1, 1, 1.0, 2, [1.0, 2.0], [1.0, 3.0])
subcutaneous_model_1 = Subcutaneous(1.0, 1.0, 1, 1, 1.0, 2, [1.0, 2.0], [1.0, 3.0], 1.0, 1.0)

results_intravenous_1 = intravenous_model_1.solve_equations()
results_subcutaneous_1 = subcutaneous_model_1.solve_equations()
plot(results_intravenous_1, "standard_two_peripheries")
plot(results_subcutaneous_1, "standard_two_peripheries")

# Default values
intravenous_model_2 = Intravenous()
subcutaneous_model_2 = Subcutaneous()

results_intravenous_2 = intravenous_model_2.solve_equations()
results_subcutaneous_2 = subcutaneous_model_2.solve_equations()
plot(results_intravenous_2, "all_defaults")
plot(results_subcutaneous_2, "all_defaults")

# Setting dosage only to zero
intravenous_model_3 = Intravenous(clearance_rate=1, X=0, Q_p_list=[2.0])
subcutaneous_model_3 = Subcutaneous(clearance_rate=1, X=0, Q_p_list=[2.0], absorption_rate=1.0)

results_intravenous_3 = intravenous_model_3.solve_equations()
results_subcutaneous_3 = subcutaneous_model_3.solve_equations()
plot(results_intravenous_3, "zero_dosage")
plot(results_subcutaneous_3, "zero_dosage")

# Setting clearance_rate to zero
intravenous_model_4 = Intravenous(clearance_rate=0, X=1, Q_p_list=[2.0])
subcutaneous_model_4 = Subcutaneous(clearance_rate=0, X=1, Q_p_list=[2.0], absorption_rate=1.0)

results_intravenous_4 = intravenous_model_4.solve_equations()
results_subcutaneous_4 = subcutaneous_model_4.solve_equations()
plot(results_intravenous_4, "zero_clearance")
plot(results_subcutaneous_4, "zero_clearance")
