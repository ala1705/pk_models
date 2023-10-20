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

	python simulation.py

This will run the simulation with pre-set parameter values.


## Setting up the simulation
In order to change the parameter values, ............................................................


## Usage

### Dosing function

The dosing function consists of three parameters:
* X: The amount of the drug administered [ng]
* dose: The length of the time period for which the drug is administered
* no_dose: The length of the time period between doses

If dose = 0, then there is an instantaneous dose at the beginning, and no more of the drug will be administered.

If dose = 1, no_dose = 0, there will be a continuous dose of amount X administered over the time period.

If dose > 0 and no_dose > 0, then the dose function switches between a continuous dose applied for the time period dose specifies
and no dose applied for the time period no_dose specifies.

