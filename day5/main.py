import copy

# Didn't find a way to read the file into this format.
# had to add [::-1] to reverse the list, because it was donkey
STACKS = {
    "1": ["P", "V", "Z", "W", "D", "T"][::-1],
    "2": ["D", "J", "F", "V", "W", "S", "L"][::-1],
    "3": ["H", "B", "T", "V", "S", "L", "M", "X"][::-1],
    "4": ["J", "S", "R"][::-1],
    "5": ["W", "L", "M", "F", "G", "B", "Z", "C"][::-1],
    "6": ["B", "G", "R", "Z", "H", "V", "W", "Q"][::-1],
    "7": ["N", "D", "B", "C", "P", "J", "V"][::-1],
    "8": ["Q", "B", "T", "P"][::-1],
    "9": ["C", "R", "Z", "G", "H"][::-1],
}


def process_input_file(file_path):
    raw_input = ""
    with open(file_path) as f:
        raw_input = f.readlines()

    return raw_input[10:]


def main():
    commands = process_input_file("./day5/input.txt")

    new_stacks = copy.deepcopy(STACKS)
    new_stacks_with_cratemover_9001 = copy.deepcopy(STACKS)
    for command in commands:
        command = command.strip().split()

        number = int(command[1])
        _from = str(command[3])
        to = str(command[-1])

        # part 1
        for _ in range(number):
            crate_to_move = new_stacks[_from][-1]
            new_stacks[to].append(crate_to_move)  # move to new stack
            new_stacks[_from] = new_stacks[_from][:-1]  # remove from previous stack

        # part 2
        crates_to_move = new_stacks_with_cratemover_9001[_from][-number:]
        new_stacks_with_cratemover_9001[to] = (
            new_stacks_with_cratemover_9001[to] + crates_to_move
        )
        new_stacks_with_cratemover_9001[_from] = new_stacks_with_cratemover_9001[_from][
            :-number
        ]

    result = ""
    for stack, crates in new_stacks.items():
        result += crates[-1]

    result_part_2 = ""
    for _, crates in new_stacks_with_cratemover_9001.items():
        result_part_2 += crates[-1]

    print(f"Result: {result}")
    print(f"Result part 2: {result_part_2}")


if __name__ == "__main__":
    main()
