#!/usr/bin/env python


def calculate_scratchcard_points(cards):
    total_points = 0

    for card in cards:
        winning_numbers, your_numbers = card.split("|")
        winning_numbers = set(map(int, winning_numbers.strip().split()))
        your_numbers = set(map(int, your_numbers.strip().split()))

        matches = winning_numbers.intersection(your_numbers)
        if matches:
            points = 1
            for _ in range(len(matches) - 1):
                points *= 2
            total_points += points

    return total_points


def count_matches(winning_numbers, your_numbers):
    return len(winning_numbers.intersection(your_numbers))


def calculate_new_scratchcard_rule(cards):
    card_count = len(cards)
    card_instances = [1] * card_count  # Starting with 1 instance of each card

    for i in range(card_count):
        winning_numbers, your_numbers = cards[i].split("|")
        winning_numbers = set(map(int, winning_numbers.strip().split()))
        your_numbers = set(map(int, your_numbers.strip().split()))

        matches = count_matches(winning_numbers, your_numbers)
        for j in range(i + 1, min(i + 1 + matches, card_count)):
            card_instances[j] += card_instances[i]

    total_cards = sum(card_instances)
    return total_cards


# Example scratchcards
scratchcards = [
    "41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    " 1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "31 18 13 56 72 | 74 77 10 23 35 67 36 11",
]

# Calculating the total points of the Elf's scratchcards
total_points = calculate_scratchcard_points(scratchcards)
assert total_points == 13

# Calculating the total scratchcards based on the new rule
total_scratchcards = calculate_new_scratchcard_rule(scratchcards)
assert total_scratchcards == 30

file_name = "input4.txt"


def load_input_from_file(file_path):
    cards = []
    try:
        with open(file_path) as file:
            for line in file:
                # Extract the part after the colon
                card_info = line.split(":", 1)[1].strip()
                cards.append(card_info)
    except Exception as e:
        return f"An error occurred while reading the file: {e}"

    return cards


scratchcards = load_input_from_file(file_name)
total_points = calculate_scratchcard_points(scratchcards)
print(total_points)

total_points = calculate_new_scratchcard_rule(scratchcards)
print(total_points)
