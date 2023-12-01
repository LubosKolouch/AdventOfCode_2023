#!/usr/bin/env python
# -*- coding: utf-8 -*-


def sum_calibration_values_from_file(filename: str) -> int:
    """
    Reads a file where each line is expected to contain text with digits. 
    It extracts the first and last digit from each line, combines them to form a two-digit number, 
    and returns the sum of these numbers from all lines.

    :param filename: str - The name of the file to read from.
    :return: int - The sum of the two-digit numbers formed from the first and last digits of each line.

    If the file is not found, a FileNotFoundError is raised.
    """
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        total = 0
        for line in lines:
            first_digit = next((char for char in line if char.isdigit()), None)
            last_digit = next(
                (char for char in reversed(line) if char.isdigit()), None)

            if first_digit is not None and last_digit is not None:
                total += int(first_digit + last_digit)

        return total
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{filename}' was not found.")


def test_sum_calibration_values_from_file():
    """
    Test function for sum_calibration_values_from_file.
    It asserts whether the function correctly calculates the sum of calibration values from a given file.
    """
    expected_result = 142  # Expected result from the sample input
    try:
        actual_result = sum_calibration_values_from_file("input1_test.txt")
        assert actual_result == expected_result, f"Test Failed: Expected {expected_result}, got {actual_result}"
        print(
            "Test Passed: sum_calibration_values_from_file works as expected.")
    except FileNotFoundError as e:
        print(e)
    except AssertionError as e:
        print(e)


def main():
    # Main function to run the test
    print("Part1 :", sum_calibration_values_from_file(filename="input1.txt"))


if __name__ == "__main__":
    main()
