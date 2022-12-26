def process_input_file(file_path):
    with open(file_path) as f:
        raw_commands = f.read()

    return raw_commands.split("\n")


def main(input_file):
    commands = process_input_file(input_file)

    during_cycle = {}
    after_cycle = {}

    x = 1
    cycle = 1
    for command in commands:
        if command == "noop":
            during_cycle[cycle] = x
        else:
            for a in range(2):
                if a == 0:
                    during_cycle[cycle] = x
                if a == 1:
                    during_cycle[cycle] = x
                    x += int(command.split(" ")[1])
                    break

                # Cycle completed
                after_cycle[cycle] = x
                cycle += 1

        # Cycle completed
        after_cycle[cycle] = x
        cycle += 1

    print(f"{during_cycle=}")
    print(f"{after_cycle=}")

    total_strength = 0
    for number_cycle in [20, 60, 100, 140, 180, 220]:
        print(f"{during_cycle[number_cycle]=}")
        cycle_x = during_cycle[number_cycle]
        total_strength += cycle_x * number_cycle

    print(f"{total_strength=}")


if __name__ == "__main__":
    main("./day10/input.txt")
    # main("./day10/test_input.txt")
    # main("./day10/example_input.txt")
