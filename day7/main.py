def process_input_file(file_path):
    raw_input = ""
    with open(file_path) as f:
        raw_input = f.read()

    return raw_input.split("\n")


def main():
    input_ = process_input_file("./day7/input.txt")
    print(input_)


if __name__ == "__main__":
    main()
