# list -1 --> up
# list +1 --> down
# list +1 --> right
# list -1 --> left


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


def is_tree_visible(tree, top_tree, bottom_tree, left_tree, right_tree):
    if tree > top_tree or tree > bottom_tree or tree > left_tree or tree > right_tree:
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


def main():
    tree_grid = process_input_file("./day8/input.txt")

    total_visible_trees = 0
    test = 0
    for tree_row_index, tree_row in enumerate(tree_grid):
        for tree_index, tree in enumerate(tree_row):
            if is_edge(tree_grid, tree_row, tree_row_index, tree_index):
                print("/", end="")
                total_visible_trees += 1
                continue  # Don't process edge trees

            # visible = is_tree_visible(
            #     tree=tree,
            #     top_tree=tree_grid[tree_row_index - 1][tree_index],
            #     bottom_tree=tree_grid[tree_row_index + 1][tree_index],
            #     left_tree=tree_row[tree_index - 1],
            #     right_tree=tree_row[tree_index + 1],
            # )
            visible = is_tree_visible_from_edge(
                tree, tree_row_index, tree_index, tree_grid
            )

            if visible:
                print("1", end="")
                total_visible_trees += 1

            else:
                print("0", end="")

            # print(f"{tree=}")

        print()
        # if test == 1:
        #     break
        # test = 1

    print(f"Total visible trees: {total_visible_trees}")


if __name__ == "__main__":
    main()
