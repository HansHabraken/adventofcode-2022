def read_file():
    with open("./day1/input.txt") as f:
        return f.read()


def calculate_calls_per_elf(input):
    processed_list = []
    cal_per_elf = []
    for cal in input:
        if cal != "":
            cal_per_elf.append(int(cal))
            continue
        processed_list.append(cal_per_elf)
        cal_per_elf = []

    return processed_list


def get_total_calls_per_elf(input):
    total_calls_per_elf = []
    for elf_calls in input:
        total_calls_per_elf.append(sum(elf_calls))

    return total_calls_per_elf


def main():
    raw_input = read_file()
    list_input = raw_input.split("\n")

    calls_per_elf = calculate_calls_per_elf(input=list_input)

    total_calls_per_elf = get_total_calls_per_elf(input=calls_per_elf)

    # Answer part 1
    print(f"Highest calls an elf carriers: {max(total_calls_per_elf)}")

    # Answer part 2
    total_calls_per_elf_sorted = sorted(total_calls_per_elf, reverse=True)
    print(
        f"Total calls cariered by the top three elves: {sum(total_calls_per_elf_sorted[:3])}"
    )


if __name__ == "__main__":
    main()
