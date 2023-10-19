from intravenous import Intravenous
from subcutaneous import Subcutaneous
from plot import plot

# Some manual testing cases - Basic arguments
intravenous_model_1 = Intravenous(1.0, 1.0, 1.0, 2, [1.0, 2.0], [1.0, 3.0])
subcutaneous_model_1 = Subcutaneous(1.0, 1.0, 1.0, 2, [1.0, 2.0], [1.0, 3.0], 1.0, 1.0)

# Default values
intravenous_model_2 = Intravenous()
subcutaneous_model_2 = Subcutaneous()

# Setting dosage only to zero
intravenous_model_3 = Intravenous(clearance_rate=1, dose_rate=0, Q_p_list=[2.0])
subcutaneous_model_3 = Subcutaneous(clearance_rate=1, dose_rate=0, Q_p_list=[2.0], absorption_rate=1.0)

# Setting clearance_rate to zero
intravenous_model_4 = Intravenous(clearance_rate=0, dose_rate=1, Q_p_list=[2.0])
subcutaneous_model_4 = Subcutaneous(clearance_rate=0, dose_rate=1, Q_p_list=[2.0], absorption_rate=1.0)

results_intravenous = intravenous_model_4.solve_equations()
results_subcutaneous = subcutaneous_model_4.solve_equations()
plot(results_intravenous)
plot(results_subcutaneous)


