import numpy as np


def process_input_file(file_path):
    with open(file_path) as f:
        raw_grid = f.readlines()

    processed_grid = []
    for tree_row in raw_grid:
        tree_row_list = []
        for tree in tree_row.strip():
            tree_row_list.append(tree)
        processed_grid.append(tree_row_list)

    return processed_grid


def is_edge(tree_grid, tree_row, tree_row_index, tree_index):

    # top border
    if tree_row_index - 1 < 0:
        return True

    # bottom border
    if tree_row_index + 1 >= len(tree_grid):
        return True

    # right border
    if tree_index + 1 >= len(tree_row):
        return True

    # left border
    if tree_index - 1 < 0:
        return True

    return False


def is_tree_visible_from_edge(tree, tree_row_index, tree_index, tree_grid):
    right_trees = tree_grid[tree_row_index][tree_index + 1 :]
    left_trees = tree_grid[tree_row_index][:tree_index]
    top_trees = [tree_row[tree_index] for tree_row in tree_grid[:tree_row_index]]
    bottom_trees = [
        tree_row[tree_index] for tree_row in tree_grid[tree_row_index + 1 :]
    ]
    # print(f"{max(right_trees)=}")
    # print(f"{len(right_trees)=}")
    # print(f"{max(left_trees)=}")
    # print(f"{len(left_trees)=}")
    # print(f"{max(top_trees)=}")
    # print(f"{len(top_trees)=}")
    # print(f"{max(bottom_trees)=}")
    # print(f"{len(bottom_trees)=}")

    if (
        max(right_trees) < tree
        or max(left_trees) < tree
        or max(top_trees) < tree
        or max(bottom_trees) < tree
    ):
        return True


def calculate_distance_score(tree, tree_row_index, tree_index, tree_grid):
    right_trees = tree_grid[tree_row_index][tree_index + 1 :]
    left_trees = tree_grid[tree_row_index][:tree_index]
    top_trees = [tree_row[tree_index] for tree_row in tree_grid[:tree_row_index]]
    bottom_trees = [
        tree_row[tree_index] for tree_row in tree_grid[tree_row_index + 1 :]
    ]

    score = 1

    for trees in [right_trees, left_trees, top_trees[::-1], bottom_trees]:
        indices = [
            index + 1 for index, item in enumerate(trees) if int(item) >= int(tree)
        ]
        if indices:
            score *= indices[0]
        else:
            score *= len(trees)

    return score


def main():
    tree_grid = process_input_file("./day8/input.txt")

    total_visible_trees = 0
    distance_score_list = []
    for tree_row_index, tree_row in enumerate(tree_grid):
        for tree_index, tree in enumerate(tree_row):
            if is_edge(tree_grid, tree_row, tree_row_index, tree_index):
                print("/", end="")
                total_visible_trees += 1
                continue  # Don't process edge trees

            visible = is_tree_visible_from_edge(
                tree, tree_row_index, tree_index, tree_grid
            )

            distance_score = calculate_distance_score(
                tree, tree_row_index, tree_index, tree_grid
            )
            distance_score_list.append(distance_score)

            if visible:
                print("1", end="")
                total_visible_trees += 1

            else:
                print("0", end="")

        print()

    print(f"Total visible trees: {total_visible_trees}")
    print(f"Hightest distance score: {max(distance_score_list)}")


def test_calculate_distance_score():
    tree_grid = [
        ["1", "2", "3", "2", "3"],
        ["3", "5", "10", "2", "3"],
        ["5", "5", "7", "2", "3"],
        ["1", "2", "2", "2", "3"],
        ["3", "5", "10", "2", "3"],
        ["5", "5", "7", "2", "3"],
    ]

    tree_row_index = 3
    tree_index = 1
    tree = tree_grid[tree_row_index][tree_index]

    expected_value = 1

    return_value = calculate_distance_score(tree, tree_row_index, tree_index, tree_grid)
    print(return_value)
    assert return_value == expected_value


if __name__ == "__main__":
    main()
    test_calculate_distance_score()
