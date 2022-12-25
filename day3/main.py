import string
from textwrap import wrap


def generate_priority_list():
    alphabet_low = list(string.ascii_lowercase)
    alphabet_high = list(string.ascii_uppercase)

    return alphabet_low + alphabet_high


def process_input_file(file_path):
    raw_input = ""
    with open(file_path) as f:
        raw_input = f.read()

    return raw_input.split("\n")


def get_items_in_department(rucksacks_items):
    return wrap(rucksacks_items, int(len(rucksacks_items) / 2))


def find_shared_item(department_1_items, department_2_items):
    for item in department_1_items:
        if item in department_2_items:
            return item


def find_shared_item_in_group(group):
    return list(set.intersection(*map(set, group)))[0]


def get_groups(rucksacks_items):
    return [rucksacks_items[n : n + 3] for n in range(0, len(rucksacks_items), 3)]


def main():
    rucksacks_items = process_input_file("./day3/input.txt")

    # Part 1
    sum_priorities = 0
    for items in rucksacks_items:
        items_in_department = get_items_in_department(items)
        shared_item = str(
            find_shared_item(items_in_department[0], items_in_department[1])
        )

        priority_list = generate_priority_list()
        priority = priority_list.index(shared_item) + 1

        sum_priorities += priority

    print(f"Sum of all priorities: {sum_priorities}")

    # Part 2
    rucksacks_items_group = get_groups(rucksacks_items)
    sum_group_priorities = 0

    for group in rucksacks_items_group:
        shared_group_item = str(find_shared_item_in_group(group))

        priority_list = generate_priority_list()
        priority = priority_list.index(shared_group_item) + 1

        sum_group_priorities += priority

    print(f"Sum of all group priorities: {sum_group_priorities}")


if __name__ == "__main__":
    main()
