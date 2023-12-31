# Pharmacokinetics Model Solver

## Overview

Pharmacokinetics Model Solver is a library designed to specify, solve and visualise the solution of a PK model. 

## Installation

To install a copy of the solver, open a terminal and run:

	git clone git@github.com:ala1705/pk_models.git

To make sure all dependencies are installed, in the current directory run:

	pip install ./pk_models


## Quick run
Move to the pk_models directory. In the command line, run

	python simulation.py -m Intravenous

This will run the simulation with pre-set parameter values. The model type must be specified! Here, the model is Intravenous, but this could be replaced with Subcutaneous.

In order to change these parameter values, you will need to use commands within pk_models (see below)

## Commands
Entering commands in the terminal will allow you to set-up a specific simulation.

A comprehensive list of the commands is provided below:


|Command|Command Shortcut|Description|
| --- | --- | --- |
|`--help`|`-h`|Print help|
|`--model-type`|`-m`|Model type {Intravenous,Subcutaneous}|
|`--clearance=1.0`|`-c`|Clearance|
|`--dose-rate=1.0`|`-d`|Dose amount per time step [ng per time step]|
|`--dose-on=0`|`-s`|Number of time steps per cycle when the drug is administered. If both the dose_on and dose_off is set to 0, the drug is administered only once, immediately.|
|`--dose-off=0`|`-e`|Number of time steps per cycle when the drug is not administered.|
|`--V-central=1`|`-v`|Volume of the central compartment [mL]|
|`--n-peripheries=1`|`-n`|Number of peripheral compartments (0-2)|
|`--V-peripheries="[1.0]"`|`-V`|List of volumes of peripheral compartments [mL]|
|`--Q-peripheries="[1.0]"`|`-Q`|List of flux rates between the central and peripheral compartments [mL/h]|
|`--drug-volume=1.0`|`-D`|Volume of the subcutaneous compartment where the drug is administered [mL] - only applicable to the Subcutaneous model type|
|`--drug-absorption=1.0`|`-a`|Flux rate between the drug and central compartment [mL/h] - only applicable to the Subcutaneous model type|
|`--run-time=1.0`|`-r`|Length of the runtime [h]|
|`--time-step=1.0`|`-t`|Length of the time step [s]|
|`--plot-folder="/plots"`|`-f`|Destination of the plot files|
|`--title=""`|`-T`|Title attached to the output .png file|


## Parameter Definitions

### clearance_rate: 
The constant clearance rate (mL/h) from the central compartment

### dose_per_time_step: 
The rate of dosage (ng/time_step) into the central compartment

### dose_on: 
The number of time-steps the drug is administered at a time (if dose_on = 0,there is single dose_on at time 0) If dose_off = 0, the dose_on can be 0 (instantaneous dose_on) or 1 (continuous dose_on)

### dose_off: 
The number of time-steps for which drug is not administered at a time

### V_c: 
The constant volume (mL) of the central compartment

### num_peripheries: 
The number of periphery compartments (0-2 inclusive)

### V_p_list: 
The list of volumes (mL) of the different periphery compartments

### Q_p_list: 
The list of transition rates (mL/h) between the central compartment and each periphery compartment

### run_time: 
The simulated time (h) that the model runs for

### time_step_length: 
The length (s) of an individual time-step







## Usage

### Dosing function

If dose = 0, then there is an instantaneous dose at the beginning, and no more of the drug will be administered.

If dose = 1, no_dose = 0, there will be a continuous dose of amount X administered over the time period.

If dose > 0 and no_dose > 0, then the dose function switches between a continuous dose applied for the time period dose specifies
and no dose applied for the time period no_dose specifies.



## Biological Meaning: Pharmokinetic Modelling
The information provided is sourced from the [oxrse website](https://train.oxrse.uk/event/5/1960).

The field of Pharmacokinetics (PK) provides a quantitative basis for describing the delivery of a drug to a patient, the diffusion of that drug through the plasma/body tissue, and the subsequent clearance of the drug from the patient's system. PK is used to ensure that there is sufficient concentration of the drug to maintain the required efficacy of the drug, while ensuring that the concentration levels remain below the toxic threshold (See Fig 1). Pharmacokinetic (PK) models are often combined with Pharmacodynamic (PD) models, which model the positive effects of the drug, such as the binding of a drug to the biological target, and/or undesirable side effects, to form a full PKPD model of the drug-body interaction. This project will only focus on PK, neglecting the interaction with a PD model.

PK enables the following processes to be quantified:

* Absorption
* Distribution
* Metabolism
* Excretion









