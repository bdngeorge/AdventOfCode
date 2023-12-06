import re

if __name__ == "__main__":
    input = open("input.txt", "r").read().strip().split("\n")

    # Parse the input
    times = re.findall(r'\d+', input[0].split(":")[1])
    timeStr = ""
    for time in times:
        timeStr += time
    time = int(timeStr)

    distances = re.findall(r'\d+', input[1].split(":")[1])
    distancesStr = ""
    for distance in distances:
        distancesStr += distance
    distance = int(distancesStr)

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