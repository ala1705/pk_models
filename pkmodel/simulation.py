import getopt
import sys
import os
from pkmodel.model import Model


CL = 1.0
dose = 1.0
dose_on = 0
dose_off = 0
Vc = 1.0
N = 1
Vp = None
Qp = None
V0 = 1.0
absorption = 1.0
run_time = 1.0
t = 1.0
plot = "/plots"


dirname = os.path.dirname(os.path.realpath(__file__))


argv = sys.argv[1:]
try:
    options, args = getopt.getopt(argv, "hm:c:d:s:e:v:n:V:Q:D:a:r:t:f:",
                                  [
                                      "help",
                                      "model-type =",
                                      "clearance =",
                                      "dose-rate =",
                                      "dose-on =",
                                      "dose-off =",
                                      "Vcentral =",
                                      "n-peripheries =",
                                      "Vperipheries =",
                                      "Qperipheries =",
                                      "drug-volume =",
                                      "drug-absorption =",
                                      "run-time =",
                                      "time-step =",
                                      "plot-folder =",
                                  ])
except:
    print("Error: incorrect arguments provided. Use '--help' option for help.")
    sys.exit()
names = list(zip(*options))[0]
if not ('-m' in names or '--model-type' in names or "-h" in names or "--help" in names):
    print("Error: model type has to be specified. Available options: "
          + "'Intravenous', 'Subcutaneous'. Choose '--help' option for help")
    sys.exit()

for name, value in options:
    if name in ['-h', '--help']:
        with open(dirname + "/docs.txt", "r") as file:
            text = file.read()
        print(text)
        sys.exit()
    elif name in ['-m', '--model-type']:
        if value in ["Intravenous", "Subcutaneous"]:
            m = value
        else:
            print("Error: unrecognised model type. Available options: 'Intravenous', 'Subcutaneous'")
            sys.exit()
    elif name in ['-c', '--clearance']:
        try:
            CL = float(value)
        except:
            print("Error: clearance value should be Int or Float")
            sys.exit()
    elif name in ['-d', '--dose-rate']:
        try:
            dose = float(value)
        except:
            print("Error: dose rate value should be Int or Float")
            sys.exit()
    elif name in ['-s', '--dose-on']:
        try:
            dose_on = int(value)
        except:
            print("Error: dose on value should be Int")
            sys.exit()
    elif name in ['-e', '--dose-off']:
        try:
            dose_off = int(value)
        except:
            print("Error: dose off value should be Int")
            sys.exit()
    elif name in ['-v', '--Vcentral']:
        try:
            Vc = float(value)
        except:
            print("Error: volume of the central compartment should be Int or Float")
            sys.exit()
    elif name in ['-n', '--n-peripheries']:
        try:
            N = int(value)
        except:
            print("Error: number of peripheries value should be Int")
            sys.exit()
    elif name in ['-V', '--Vperipheries']:
        Vp = value
    elif name in ['-Q', '--Qperipheries']:
        Qp = value
    elif name in ['-D', '--drug-volume']:
        try:
            V0 = float(value)
        except:
            print("Error: volume of the drug compartment should be Int or Float")
            sys.exit()
    elif name in ['-a', '--drug-absorption']:
        try:
            absorption = float(value)
        except:
            print("Error: drug absorption rate value should be Int or Float")
            sys.exit()
    elif name in ['-r', '--run-time']:
        try:
            run_time = float(value)
        except:
            print("Error: run time length should be Int or Float")
            sys.exit()
    elif name in ['-t', '--time-step']:
        try:
            t = float(value)
        except:
            print("Error: time step size should be Int or Float")
            sys.exit()
    elif name in ['-f', '--plot-folder']:
        plot = value


print(N + CL)
