# A: ROCK
# B: PAPER
# C: SCISSOR

# X: ROCK
# Y: PAPER
# Z: SCISSOR


YOUR_SHAPE_POINTS = {"X": 1, "Y": 2, "Z": 3}
OPPONENT_SHAPE_POINTS = {"A": 1, "B": 2, "C": 3}
POINTS = {
    "AX": 3,
    "AY": 6,
    "AZ": 0,
    "BX": 0,
    "BY": 3,
    "BZ": 6,
    "CX": 6,
    "CY": 0,
    "CZ": 3,
}

# * Can be simplified, because there is a pattern
PREDICT_SHAPE = {
    "A": {  # Opponent uses Rock
        "X": "Z",  # You need to lose
        "Y": "X",  # You need to draw
        "Z": "Y",  # You need to win
    },
    "B": {
        "X": "X",  # You need to lose
        "Y": "Y",  # You need to draw
        "Z": "Z",  # You need to win
    },
    "C": {
        "X": "Y",  # You need to lose
        "Y": "Z",  # You need to draw
        "Z": "X",  # You need to win
    },
}


def process_input_file(file_path):
    raw_input = ""
    with open(file_path) as f:
        raw_input = f.read()

    list_input = raw_input.split("\n")

    processed_input = []
    for item in list_input:
        processed_input.append(item.split(" "))

    return processed_input


def main():
    rounds = process_input_file("./day2/input.txt")

    # Part 1
    total_points = 0
    for r in rounds:
        opponent_shape = r[0]
        your_shape = r[1]

        game_point = POINTS[f"{opponent_shape}{your_shape}"]
        shape_point = YOUR_SHAPE_POINTS[your_shape]
        total_point = game_point + shape_point
        total_points += total_point

    print(f"Your total points in part 1: {total_points}")

    # Part 2
    total_points = 0
    for r in rounds:
        opponent_shape = r[0]
        round_outcome = r[1]

        your_shape = PREDICT_SHAPE[opponent_shape][round_outcome]
        game_point = POINTS[f"{opponent_shape}{your_shape}"]
        shape_point = YOUR_SHAPE_POINTS[your_shape]
        total_point = game_point + shape_point
        total_points += total_point

    print(f"Your total points part 2: {total_points}")


if __name__ == "__main__":
    main()
