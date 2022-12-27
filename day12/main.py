# position --> [index_row, index_element]
# Paths -> [[start_position, n_position], [start_position, n_position]]
# example -> [[[0,0], [0,1]], [[0,0], [1,0]]]

import copy
import string

ALL_LEVELS = string.ascii_lowercase


def process_input_file(file_path):
    with open(file_path) as f:
        raw_grid = f.readlines()

    processed_grid = []
    for row in raw_grid:
        row_list = []
        for elem in row.strip():
            row_list.append(elem)
        processed_grid.append(row_list)

    return processed_grid


def find_start_and_end_index(grid):
    start_index = []
    end_index = []
    for row_index, row in enumerate(grid):
        for elem_index, elem in enumerate(row):
            if elem == "S":
                start_index = [row_index, elem_index]
            if elem == "E":
                end_index = [row_index, elem_index]

    return start_index, end_index


def find_next_positions(current_position, previous_path, grid):
    """Calculate all next positions and verify if these are able to go to"""
    current_level = grid[current_position[0]][current_position[1]]
    if current_level == "S":
        current_level = "a"

    possible_positions = []

    # Want to move up
    for next_position in [
        [current_position[0] - 1, current_position[1]],  # up
        [current_position[0] + 1, current_position[1]],  # down
        [current_position[0], current_position[1] - 1],  # left
        [current_position[0], current_position[1] + 1],  # right
    ]:
        # Prevent loops
        if next_position not in previous_path:
            if (
                next_position[0] >= 0  # checks top border
                and next_position[1] >= 0  # checks left border
                and next_position[0] < len(grid)  # checks bottom border
                and next_position[1] < len(grid[0])  # checks right border
            ):  # Position needs to b in grid
                next_level = grid[next_position[0]][next_position[1]]
                if next_level == "S":
                    next_level = "a"
                if next_level == "E":
                    next_level = "z"
                if ALL_LEVELS.index(next_level) - ALL_LEVELS.index(current_level) < 2:
                    # possible to move to this position
                    possible_positions.append(next_position)

    return possible_positions


def main(input_file):
    grid = process_input_file(input_file)
    start_position, end_position = find_start_and_end_index(grid)
    paths = [[start_position]]
    visited_positions = []


#     found = False
#     while not found:
#         next_paths = []
#         for path in paths:
#             last_position = path[-1]
#             next_positions = find_next_positions(
#                 current_position=last_position,
#                 grid=grid,
#                 previous_path=path,
#             )

#             # print(len(next_positions))
#             for next_position in next_positions:

#                 # for next_path in next_paths:
#                 #     if next_position in next_path:
#                 #         continue
#                 # next_path = path.append(next_position)
#                 next_path = path + [next_position]
#                 next_paths.append(next_path)

#                 # print(len(path + [next_position]))

#                 if next_position == end_position:
#                     # print(next_path)
#                     # print(len(next_path))
#                     found = True
#                     break

#             if found:
#                 break
#         paths = next_paths
#         paths = sorted(paths, key=len)
#         print(len(paths))


# # def test_find_next_positions():
# #     grid = process_input_file("./day12/test_input.txt")

# #     current_position = [1, 3]
# #     next_positions = find_next_positions(current_position=current_position, grid=grid)

# #     print(next_positions)


if __name__ == "__main__":
    main("./day12/input.txt")
    # test_find_next_positions()
    # main("./day12/test_input.txt")
