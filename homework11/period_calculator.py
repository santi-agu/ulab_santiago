# File: period_calculator.py
import numpy as np

def calculate_period_with_numpy_in_module(axis):
    # Given the semi-major axis of a planet a (in AU), calculates and returns its orbiral period (in years)
    # Uses the equation T^2 = a^3 and the numpy library
    period = np.power(axis, 1.5)
    return period