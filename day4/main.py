def process_input_file(file_path):
    raw_input = ""
    with open(file_path) as f:
        raw_input = f.read()

    pairs_list = []

    for pairs in raw_input.split("\n"):
        pair = pairs.split(",")

        pair_list = []
        for _ranges in pair:
            pair_list.append(_ranges.split("-"))

        pairs_list.append(pair_list)

    return pairs_list


def get_section_list(start, end):
    section = []
    for i in range(start, end + 1):
        section.append(i)

    return section


def is_one_pair_fully_contained_in_other(pair_1, pair_2):
    if (pair_1[0] in pair_2 and pair_1[-1] in pair_2) or (
        pair_2[0] in pair_1 and pair_2[-1] in pair_1
    ):
        return True

    return False


def is_there_an_overlap_between_the_pairs(pair_1, pair_2):
    for section in pair_1:
        if section in pair_2:
            return True

    for section in pair_2:
        if section in pair_1:
            return True

    return False


def main():
    input_ = process_input_file("./day4/input.txt")

    # part 1
    fully_contained_counter = 0
    overlap_counter = 0
    for pairs in input_:
        pair_1 = get_section_list(int(pairs[0][0]), int(pairs[0][1]))
        pair_2 = get_section_list(int(pairs[1][0]), int(pairs[1][1]))

        is_one_fully_containd = is_one_pair_fully_contained_in_other(
            pair_1, pair_2
        )  # part 1
        is_there_an_overlap = is_there_an_overlap_between_the_pairs(
            pair_1, pair_2
        )  # part 2

        if is_one_fully_containd:
            fully_contained_counter += 1

        if is_there_an_overlap:
            overlap_counter += 1

    print(
        f"There are {fully_contained_counter} pairs where one is fully contained in the other"
    )

    print(
        f"There are {overlap_counter} pairs where on overlapped sections in the other"
    )

    # part 2


if __name__ == "__main__":
    main()
