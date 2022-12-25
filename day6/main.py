def process_input_file(file_path):
    with open(file_path) as f:
        return f.read()


def elements_are_unique(x):
    if len(x) == len(set(x)):
        return True

    return False


def main():
    signal = process_input_file("./day6/input.txt")
    print(signal)

    mark_counter = 0
    mark_list = []
    for char in signal:
        mark_counter += 1
        mark_list.append(char)

        if len(mark_list) < 4:
            continue

        if len(mark_list) > 4:
            del mark_list[0]  # Remove first element

        if elements_are_unique(mark_list):
            break

    print(
        f"Marker position: {mark_counter} | Unique sequential characters: {''.join(mark_list)}"
    )

    mark_counter_part_2 = 0
    mark_list_part_2 = []
    for char in signal:
        mark_counter_part_2 += 1
        mark_list_part_2.append(char)

        if len(mark_list_part_2) < 14:
            continue

        if len(mark_list_part_2) > 14:
            del mark_list_part_2[0]  # Remove first element

        if elements_are_unique(mark_list_part_2):
            break

    print(
        f"Part 2: Marker position: {mark_counter_part_2} | Unique sequential characters: {''.join(mark_list_part_2)}"
    )


if __name__ == "__main__":
    main()
