#!/usr/bin/env python


def extrapolate_next_value(history):
    """
    Given a history of values, this function extrapolates the next value in the sequence.
    """
    # Calculate the differences in the history
    differences = [history[i + 1] - history[i] for i in range(len(history) - 1)]

    # If the differences are all zero, return the last value in the history
    if all(d == 0 for d in differences):
        return history[-1] + differences[-1]

    # Else, recursively calculate the next value
    return history[-1] + extrapolate_next_value(differences)


def calculate_sum_of_next_values(data):
    """
    Takes multiple histories as input and returns the sum of their next values.
    """
    sum_of_next_values = 0
    for history in data:
        next_value = extrapolate_next_value(history)
        sum_of_next_values += next_value

    return sum_of_next_values


def extrapolate_previous_value(history):
    """
    Given a history of values, this function extrapolates the previous value in the sequence.
    """
    # Calculate the differences in the history
    differences = [history[i + 1] - history[i] for i in range(len(history) - 1)]

    # If the differences are all zero, return the first value in the history minus the first difference
    if all(d == 0 for d in differences):
        return history[0] - differences[0]

    # Else, recursively calculate the previous value
    return history[0] - extrapolate_previous_value(differences)


def calculate_sum_of_previous_values(data):
    """
    Takes multiple histories as input and returns the sum of their previous values.
    """
    sum_of_previous_values = 0
    for history in data:
        previous_value = extrapolate_previous_value(history)
        sum_of_previous_values += previous_value

    return sum_of_previous_values


# Test the function with the provided example
example_data = [[0, 3, 6, 9, 12, 15], [1, 3, 6, 10, 15, 21], [10, 13, 16, 21, 30, 45]]

print(calculate_sum_of_next_values(example_data))
print(calculate_sum_of_previous_values(example_data))

file_path = "input9.txt"

with open(file_path) as file:
    input_data = file.readlines()

input_histories = [list(map(int, line.strip().split())) for line in input_data]

print(calculate_sum_of_next_values(input_histories))
print(calculate_sum_of_previous_values(input_histories))
