def process_input_file(file_path):
    with open(file_path) as f:
        raw_coordinates = f.read()

    processed_coordinates = []
    for coordinate in raw_coordinates.split("\n"):
        int_coordinate = []
        for position in coordinate.split(","):
            int_coordinate.append(int(position))

        processed_coordinates.append(int_coordinate)

    return processed_coordinates


def get_number_of_not_collapsing_borders(coordinate, coordinates):
    neighbor_list = [
        [0, 0, 1],
        [0, 0, -1],
        [0, 1, 0],
        [0, -1, 0],
        [1, 0, 0],
        [-1, 0, 0],
    ]
    number = 0
    for neighbor in neighbor_list:
        neighbor_coordinate = [
            coordinate[y] + neighbor[y] for y in range(len(coordinate))
        ]
        if neighbor_coordinate not in coordinates:
            number += 1

    return number


def main(input_file):
    coordinates = process_input_file(input_file)
    print(coordinates)

    tot_n = 0
    for coordinate in coordinates:
        n = get_number_of_not_collapsing_borders(
            coordinate=coordinate, coordinates=coordinates
        )
        tot_n += n

    print(f"{tot_n=}")


if __name__ == "__main__":
    # main("./day18/test_input.txt")
    main("./day18/input.txt")
