#!/usr/bin/env python
# -*- coding: utf-8 -*-


def sum_advanced_calibration_values(filename: str) -> int:
    """
    Reads a list of lines where each line is expected to contain text with digits or spelled out digits (one, two, ...).
    It extracts the real first and last digit (or spelled out digit) from each line,
    combines them to form a two-digit number, and returns the sum of these numbers from all lines.

    :param lines: list - List of strings, each representing a line from the input.
    :return: int - The sum of the two-digit numbers formed from the first and last 'digits' of each line.
    """

    digit_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    def replace_spelled_digits(line):
        new_line = ""
        i = 0
        while i < len(line):
            found = False
            for word, digit in digit_map.items():
                if line[i:].startswith(word):
                    new_line += digit
                    i += 1
                    found = True
                    break
            if not found:
                if line[i].isdigit():
                    new_line += line[i]
                i += 1
        return new_line

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        total = 0
        for line in lines:
            line_with_digits = replace_spelled_digits(line)
            if line_with_digits:
                first_digit = line_with_digits[0]
                last_digit = line_with_digits[-1]
                total += int(first_digit + last_digit)

        return total
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{filename}' was not found.")


def test_sum_advanced_calibration_values():
    """
    Test function for sum_advanced_calibration_values.
    Asserts whether the function correctly calculates the sum of advanced calibration values from a given list of lines.
    """
    expected_result = 281  # Expected result from the sample input
    actual_result = sum_advanced_calibration_values(
        filename="input1_2_test.txt")
    assert actual_result == expected_result, f"Test Failed: Expected {expected_result}, got {actual_result}"
    print("Test Passed: sum_advanced_calibration_values works as expected.")


def main():
    # Main function to run the test
    print("Part2 :", sum_advanced_calibration_values(filename="input1.txt"))


if __name__ == "__main__":
    main()
