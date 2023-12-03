#!/usr/bin/env python


def calculate_gear_ratios_final(schematic):
    total_gear_ratio_sum = 0

    # Function to find unique part numbers adjacent to a gear
    def find_adjacent_part_numbers(x, y):
        part_numbers = set()

        # Checking all adjacent cells
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:  # Skip the gear cell itself
                    continue

                nx, ny = x + dx, y + dy
                # Ensuring the coordinates are within the grid
                if 0 <= nx < len(schematic) and 0 <= ny < len(schematic[0]):
                    if schematic[nx][ny].isdigit():
                        num = ""
                        # Move left to the start of the number if we're in the middle
                        while ny > 0 and schematic[nx][ny - 1].isdigit():
                            ny -= 1
                        # Read the full number
                        while ny < len(schematic[0]) and schematic[nx][ny].isdigit():
                            num += schematic[nx][ny]
                            ny += 1
                        part_numbers.add(int(num))

        return list(part_numbers)

    # Iterate over the grid to find gears
    for i in range(len(schematic)):
        for j in range(len(schematic[0])):
            if schematic[i][j] == "*":
                adjacent_part_numbers = find_adjacent_part_numbers(i, j)
                if len(adjacent_part_numbers) == 2:
                    gear_ratio = adjacent_part_numbers[0] * adjacent_part_numbers[1]
                    total_gear_ratio_sum += gear_ratio

    return total_gear_ratio_sum


def sum_and_list_part_numbers_general(schematic):
    total_sum = 0
    part_numbers = []  # List to store the identified part numbers

    # Function to check if a cell is next to a non-digit, non-period character
    def next_to_symbol(x, y):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if 0 <= x + dx < len(schematic) and 0 <= y + dy < len(schematic[0]):
                    if schematic[x + dx][y + dy] not in "0123456789.":
                        return True
        return False

    # Function to extract the full number starting from a position
    def get_full_number(x, y):
        num = ""
        while y < len(schematic[0]) and schematic[x][y].isdigit():
            num += schematic[x][y]
            y += 1
        return num

    # Iterate over each cell in the schematic
    for i in range(len(schematic)):
        j = 0
        while j < len(schematic[i]):
            if schematic[i][j].isdigit():
                # Extract the full number first
                full_num = get_full_number(i, j)
                # Check if any digit of the number is next to a symbol
                if any(next_to_symbol(i, j + k) for k in range(len(full_num))):
                    part_numbers.append(
                        full_num
                    )  # Add the identified part number to the list
                    total_sum += int(full_num)
                    # Skip the rest of the number
                    j += len(full_num) - 1
            j += 1

    return total_sum


def load_input_from_file(file_name):
    with open(file_name) as file:
        schematic = file.readlines()
        schematic = [line.strip() for line in schematic]
    return schematic


file_name = "input3.txt"

schematic = load_input_from_file(file_name)
test_schematic = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]

assert sum_and_list_part_numbers_general(test_schematic) == 4361
assert calculate_gear_ratios_final(test_schematic) == 467835

print(sum_and_list_part_numbers_general(schematic))
print(calculate_gear_ratios_final(schematic))
