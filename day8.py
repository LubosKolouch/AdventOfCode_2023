#!/usr/bin/env python

from functools import reduce
from math import gcd


def navigate_puzzle(instructions, nodes):
    """
    Navigates the network of nodes based on the given instructions to reach the destination node 'ZZZ'.

    :param instructions: A string of 'L' and 'R' characters representing left and right instructions.
    :param nodes: A dictionary where keys are node labels and values are tuples representing left and right nodes.
    :return: The number of steps taken to reach the destination node 'ZZZ'.
    """
    current_node = "AAA"  # Starting node
    step_count = 0

    while current_node != "ZZZ":
        # If we run out of instructions, repeat the sequence
        instruction = instructions[step_count % len(instructions)]

        # Navigate left or right based on the instruction
        if instruction == "L":
            current_node = nodes[current_node][0]
        else:  # instruction == 'R'
            current_node = nodes[current_node][1]

        step_count += 1

    return step_count


# Revised function to showcase the sub-routine using LCM
def navigate_puzzle_part2(instructions, nodes):
    """
    Algorithm to find the minimum number of steps required for all paths starting from nodes
    ending with 'A' to simultaneously reach nodes ending with 'Z', using LCM.

    :param instructions: A string of 'L' and 'R' characters representing left and right instructions.
    :param nodes: A dictionary where keys are node labels and values are tuples representing left and right nodes.
    :return: The number of steps taken for all paths to reach nodes that end with 'Z'.
    """

    # Sub-function to calculate LCM
    def lcm(numbers):
        """Calculate the least common multiple of a list of numbers."""

        def lcm_of_two(a, b):
            return a * b // gcd(a, b)

        return reduce(lcm_of_two, numbers, 1)

    # Tracking the least number of steps for each path from 'A' to 'Z'
    least_steps = []

    for start_node in [node for node in nodes if node.endswith("A")]:
        current_node = start_node
        steps = 0

        while not current_node.endswith("Z"):
            instruction = instructions[steps % len(instructions)]
            current_node = (
                nodes[current_node][0] if instruction == "L" else nodes[current_node][1]
            )
            steps += 1

        least_steps.append(steps)

    # Calculate and return the LCM of the least steps
    return lcm(least_steps)


# Define the nodes based on the new puzzle part 2 description
nodes_example_part2 = {
    "11A": ("11B", "XXX"),
    "11B": ("XXX", "11Z"),
    "11Z": ("11B", "XXX"),
    "22A": ("22B", "XXX"),
    "22B": ("22C", "22C"),
    "22C": ("22Z", "22Z"),
    "22Z": ("22B", "22B"),
    "XXX": ("XXX", "XXX"),
}

# Test the function with the provided example for part 2
steps_example_part2 = navigate_puzzle_part2("LR", nodes_example_part2)
steps_example_part2

# Define the nodes based on the puzzle description
nodes_example_1 = {
    "AAA": ("BBB", "CCC"),
    "BBB": ("DDD", "EEE"),
    "CCC": ("ZZZ", "GGG"),
    "DDD": ("DDD", "DDD"),
    "EEE": ("EEE", "EEE"),
    "GGG": ("GGG", "GGG"),
    "ZZZ": ("ZZZ", "ZZZ"),
}

nodes_example_2 = {"AAA": ("BBB", "BBB"), "BBB": ("AAA", "ZZZ"), "ZZZ": ("ZZZ", "ZZZ")}

# Test the function with the provided examples
steps_example_1 = navigate_puzzle("RL", nodes_example_1)
steps_example_2 = navigate_puzzle("LLR", nodes_example_2)

print(steps_example_1, steps_example_2)

file_path = "input8.txt"


def parse_puzzle_file_corrected(file_path):
    with open(file_path) as file:
        lines = file.readlines()

        instructions = lines[0].strip()
        node_mappings = lines[2:]

        # Creating a dictionary to store node connections
        nodes = {}
        for mapping in node_mappings:
            if mapping.strip():  # Ignore empty lines
                parts = mapping.split(" = ")
                node = parts[0].strip()
                connections = (
                    parts[1].strip().replace("(", "").replace(")", "").split(", ")
                )
                nodes[node] = tuple(connections)

    return instructions, nodes


instructions, nodes = parse_puzzle_file_corrected(file_path)
print(navigate_puzzle(instructions, nodes))
print(navigate_puzzle_part2(instructions, nodes))
