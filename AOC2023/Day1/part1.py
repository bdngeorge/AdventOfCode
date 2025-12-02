if __name__ == "__main__":
    input = open("input.txt", "r")

    total = 0
    for line in input:
        firstDigit = ""
        lastDigit = ""

        for char in line:
            if char.isdigit():
                if firstDigit == "":
                    firstDigit = char
                lastDigit = char
        
        total += (int)((firstDigit + lastDigit))
    
    print(total)