import re

def GetNumber(string):
    num = ""
    for char in string:
        if char.isdigit():
            num += char
    
    return int(num)

if __name__ == "__main__":
    input = open("input.txt", "r").read().strip().split("\n")

    # Parse the input
    time = GetNumber(input[0])
    distance = GetNumber(input[1])

    total = 1
    firstWin = -1
    for i in range(1, time):
        dist = i * (time-i)
        if dist > distance:
            firstWin = i
            break
    lastWin = -1
    for i in reversed(range(1, time)):
        dist = i * (time-i)
        if dist > distance:
            lastWin = i
            break        
    
    total = (lastWin - firstWin + 1)

    print(total)