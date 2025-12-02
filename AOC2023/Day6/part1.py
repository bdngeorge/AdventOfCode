import re

if __name__ == "__main__":
    input = open("input.txt", "r").read().strip().split("\n")

    # Parse the input
    times = [int(i) for i in re.findall(r'\d+', input[0].split(":")[1])]
    distances = [int(i) for i in re.findall(r'\d+', input[1].split(":")[1])]

    total = 1
    dist = 0
    for time in times:
        firstWin = -1
        for i in range(1, time):
            distance = i * (time-i)
            if distance > distances[dist]:
                firstWin = i
                break
        lastWin = -1
        for i in reversed(range(1, time)):
            distance = i * (time-i)
            if distance > distances[dist]:
                lastWin = i
                break        
        
        total *= (lastWin - firstWin + 1)
        dist += 1

    print(total)