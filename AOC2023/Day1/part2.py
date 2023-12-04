numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

if __name__ == "__main__":
    input = open("input.txt", "r")

    total = 0
    for line in input:
        firstDigit = ""
        lastDigit = ""

        for i in range(len(line)):
            if line[i].isdigit():
                if firstDigit == "":
                    firstDigit = line[i]
                lastDigit = line[i]
            else:   
                for j in range(i+1, len(line)+1):
                    if line[i:j] in numbers:
                        if firstDigit == "":
                            firstDigit = numbers[line[i:j]]
                        lastDigit = numbers[line[i:j]]
                        break
        
        total += (int)((firstDigit + lastDigit))
    
    print(total)