import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def ziegler_nichols(ku, tu):
    # Create a dictionary to store all control types and their respective coefficients
    tuning_rules = {
        'P': {
            'Kp': 0.5 * ku,
            'Ti': None,
            'Td': None,
            'Ki': None,
            'Kd': None,
        },
        'PI': {
            'Kp': 0.45 * ku,
            'Ti': tu / 1.2,  # Ti = 0.8 * Tu -> Ti = Tu / 1.2
            'Td': None,
            'Ki': 0.54 * ku / tu,
            'Kd': None,
        },
        'PD': {
            'Kp': 0.8 * ku,
            'Ti': None,
            'Td': 0.125 * tu,
            'Ki': None,
            'Kd': 0.1 * ku * tu,
        },
        'Classic PID': {
            'Kp': 0.6 * ku,
            'Ti': 0.5 * tu,
            'Td': 0.125 * tu,
            'Ki': 1.2 * ku / tu,
            'Kd': 0.075 * ku * tu,
        },
        'Pessen Integral': {
            'Kp': 0.7 * ku,
            'Ti': 0.4 * tu,
            'Td': 0.15 * tu,
            'Ki': 1.75 * ku / tu,
            'Kd': 0.105 * ku * tu,
        },
        'Some overshoot': {
            'Kp': 0.333 * ku,
            'Ti': 0.5 * tu,
            'Td': 0.333 * tu,
            'Ki': 0.666 * ku / tu,
            'Kd': 0.1 * ku * tu,
        },
        'No overshoot': {
            'Kp': 0.2 * ku,
            'Ti': 0.5 * tu,
            'Td': 0.333 * tu,
            'Ki': 0.4 * ku / tu,
            'Kd': 0.066 * ku * tu,
        }
    }

    return tuning_rules


def print_pid_table(tuning_rules):
    # Format the table using pandas for better presentation
    df = pd.DataFrame(tuning_rules).T
    df.columns = ['Kp', 'Ti (Integral Time)', 'Td (Derivative Time)', 'Ki', 'Kd']
    print(df)



if __name__ == "__main__":
    print("--------------------------------")