# U --> =y
# R --> +x
# L --> -x
# D --> -y


def process_input_file(file_path):
    with open(file_path) as f:
        raw_commands = f.read()

    return raw_commands.split("\n")


def move_head(point, direction):
    direction_map = {"U": [0, 1], "R": [1, 0], "L": [-1, 0], "D": [0, -1]}
    direction_move = direction_map[direction]

    # Create the sum between the direction and the current location of the point
    return [point[x] + direction_move[x] for x in range(len(point))]


def find_shared_neighbors(tail_neighbors, head_neighbors):
    return [element for element in tail_neighbors if element in head_neighbors]


def find_not_diagonally_shared_point(matching_neighbors, point):
    for x in matching_neighbors:
        if x[0] == point[0] or x[1] == point[1]:
            return x


def calculate_neighbors(point):
    neighbor_map = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0],
        [1, 1],
        [1, -1],
        [-1, 1],
        [-1, -1],
        [0, 0],
    ]

    result = []

    # Calculate the neighbors of the point
    for x in neighbor_map:
        result.append([point[y] + x[y] for y in range(len(point))])

    return result


def main(input_file):
    commands = process_input_file(input_file)
    head = [0, 0]
    tail = [0, 0]

    total_points_covered_by_tail = 0
    visited_by_tail = []
    for command in commands:
        (direction, steps) = command.split(" ")
        print(f"{direction=}")
        for step in range(int(steps)):
            head = move_head(head, direction)
            print(f"{head=}")

            head_neighbors = calculate_neighbors(point=head)
            print(f"{head_neighbors=}")

            if tail not in head_neighbors:
                tail_neighbors = calculate_neighbors(point=tail)
                matching_neighbors = find_shared_neighbors(
                    tail_neighbors=tail_neighbors, head_neighbors=head_neighbors
                )
                print(f"{matching_neighbors=}")

                tail_to_move = find_not_diagonally_shared_point(
                    matching_neighbors=matching_neighbors, point=head
                )
                tail = tail_to_move
                print(f"{tail=}")

                if tail not in visited_by_tail:
                    visited_by_tail.append(tail)

            else:
                print("Not needed to move tail")

            print()

    print(f"Total unique points covered by tail: {len(visited_by_tail)}")


if __name__ == "__main__":
    main("./day9/input.txt")
    # main("./day9/test_input.txt")
