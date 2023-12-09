#!/usr/bin/env python

# Writing the code to calculate the total winnings based on the provided hand rankings

from collections import Counter
from itertools import product


def calculate_winnings(hands_data, wildcard=False):
    hands = [line.split() for line in hands_data]
    hands = [
        (
            label_to_number(hand[0], wildcard=wildcard),
            int(
                hand[1],
            ),
            get_score(hand[0], wildcard=wildcard),
        )
        for hand in hands
    ]
    hands = sorted(hands, key=lambda hand: (hand[2], hand[0]), reverse=False)
    return sum(rank * hand[1] for rank, hand in enumerate(hands, start=1))


def label_to_number(cards, wildcard=False):
    mapping = {"T": 10, "J": 1 if wildcard else 11, "Q": 12, "K": 13, "A": 14}
    return [int(mapping.get(card, card)) for card in cards]


def get_score(cards, wildcard=False):
    types = {
        50: "Five of a kind",
        40: "Four of a kind",
        32: "Full house",
        30: "Three of a kind",
        22: "Two pair",
        20: "One pair",
        10: "High card",
    }
    counter = Counter(cards)
    jokers = counter["J"] if wildcard else 0

    if jokers:
        max_score = 10  # Default to "High card"
        other_ranks = [c for c in cards if c != "J"]
        possible_replacements = product("AKQJT98765432", repeat=jokers)

        for replacement in possible_replacements:
            test_hand = other_ranks + list(replacement)
            test_counter = Counter(test_hand)
            _max, _2nd = (sorted(test_counter.values(), reverse=True) + [0, 0])[:2]
            test_score = 10 * _max + _2nd
            test_score = max(i for i in types.keys() if i <= test_score)
            max_score = max(max_score, test_score)

        rank_score = max_score
    else:
        _max, _2nd = (sorted(counter.values(), reverse=True) + [0, 0])[:2]
        rank_score = 10 * _max + _2nd
        rank_score = max(i for i in types.keys() if i <= rank_score)

    return rank_score


hands_data = ["32T3K 765", "T55J5 684", "KK677 28", "KTJJT 220", "QQQJA 483"]
total_winnings = calculate_winnings(hands_data)
print(total_winnings)


def load_and_parse_input(file_path):
    """
    Load hands and their bids from a file and parse them into a dictionary.
    """
    hands = []
    with open(file_path) as file:
        for line in file:
            hand = line.strip()
            hands.append(hand)

    return hands


file_path = "input7.txt"

parsed_hands = load_and_parse_input(file_path)
total_winnings = calculate_winnings(parsed_hands)
print(total_winnings)

total_winnings = calculate_winnings(parsed_hands, wildcard=True)
print(total_winnings)
