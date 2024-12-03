if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()
        print(sum([int(line) for line in lines]))