from intravenous import Intravenous
from subcutaneous import Subcutaneous
from plot import plot

intravenous_model = Intravenous(1.0, 1.0, 1.0, 2, [1.0, 2.0], [1.0, 3.0])
subcutaneous_model = Subcutaneous(1.0, 1.0, 1.0, 2, [1.0, 2.0], [1.0, 3.0], 1.0, 1.0)
results_intravenous = intravenous_model.solve_equations()
results_subcutaneous = subcutaneous_model.solve_equations()
plot(results_intravenous)
plot(results_subcutaneous)
