#!/usr/bin/env python


def is_game_possible(game, red_cubes, green_cubes, blue_cubes):
    """Check if a game is possible with the given number of red, green, and blue cubes."""
    for turn in game:
        if (
            turn["red"] > red_cubes
            or turn["green"] > green_cubes
            or turn["blue"] > blue_cubes
        ):
            return False
    return True


def parse_game_data(game_data):
    """Parse the game data to a more structured format."""
    games = {}
    for line in game_data.split("\n"):
        if line.strip():
            parts = line.split(": ")
            game_id = int(parts[0].split()[1])
            turns = parts[1].split("; ")
            games[game_id] = []
            for turn in turns:
                cube_counts = {"red": 0, "green": 0, "blue": 0}
                for cube_info in turn.split(", "):
                    count, color = cube_info.split()
                    cube_counts[color] = int(count)
                games[game_id].append(cube_counts)
    return games


def calculate_possible_games(game_data, red_cubes, green_cubes, blue_cubes):
    """Calculate the sum of IDs of games that are possible with the given number of cubes."""
    games = parse_game_data(game_data)
    possible_game_ids = [
        game_id
        for game_id, game in games.items()
        if is_game_possible(game, red_cubes, green_cubes, blue_cubes)
    ]
    return sum(possible_game_ids)


def calculate_min_cubes_per_game(games):
    """Calculate the minimum number of each color cube needed for each game."""
    min_cubes = {}
    for game_id, game in games.items():
        min_red, min_green, min_blue = 0, 0, 0
        for turn in game:
            min_red = max(min_red, turn["red"])
            min_green = max(min_green, turn["green"])
            min_blue = max(min_blue, turn["blue"])
        min_cubes[game_id] = {"red": min_red, "green": min_green, "blue": min_blue}
    return min_cubes


def calculate_power_of_sets(min_cubes):
    """Calculate the power of each set and return the sum of these powers."""
    total_power = 0
    for cubes in min_cubes.values():
        power = cubes["red"] * cubes["green"] * cubes["blue"]
        total_power += power
    return total_power


# Example game data
game_data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

# Constants for the number of cubes
RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14

# Calculate the sum of IDs of possible games
sum_of_possible_game_ids = calculate_possible_games(
    game_data, RED_CUBES, GREEN_CUBES, BLUE_CUBES
)
assert sum_of_possible_game_ids == 8

try:
    filename = "input2.txt"
    with open(filename) as file:
        input_file = file.read()
except FileNotFoundError:
    raise FileNotFoundError(f"The file '{filename}' was not found.")

# Parse the uploaded game data
games = parse_game_data(input_file)

print(calculate_possible_games(input_file, RED_CUBES, GREEN_CUBES, BLUE_CUBES))

# Calculate the minimum number of cubes needed for each game
min_cubes = calculate_min_cubes_per_game(games)

# Calculate the sum of the power of these minimum sets of cubes
sum_of_powers = calculate_power_of_sets(min_cubes)
print(sum_of_powers)
