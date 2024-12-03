import re

if __name__ == "__main__":
    input = open("input.txt", "r")

    totalDist = 0
    left = []
    right = []

    for line in input:
        values = re.findall(r'\d+', line)
        left.append(values[0])
        right.append(values[1])

    left.sort()
    right.sort()

    for i in range(len(left)):
        totalDist += abs((int(left[i]) - int(right[i])))

    print(totalDist)
    