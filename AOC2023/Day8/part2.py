import collections as c

def GCD(a, b):
    while b:
        a, b = b, a%b
    return a

if __name__ == "__main__":
    input = open("input.txt", "r").read().strip().split("\n")

    directions = input[0]

    #Find all maps and starting nodes
    mapMap = c.defaultdict(lambda:())
    startingNodes = []
    for direction in input[2:]:
        node, map = direction.strip().split("=")
        mapMap[node.strip()] = (map.strip()[1:4], map.strip()[6:9])

        if node.strip()[2] == 'A':
            startingNodes.append(node.strip())

    #Find the count for each starting node
    counts = []
    for node in startingNodes:
        steps = 1
        i = 0
        currentNode = node
        while True:
            if i == len(directions):
                i = 0
                continue

            if directions[i] == 'L':
                currentNode = mapMap[currentNode][0]
            else:
                currentNode = mapMap[currentNode][1]
            
            if currentNode[2] == 'Z':
                break

            i += 1
            steps += 1
        counts.append(steps)

    #Find LCM of all counts
    sortedCounts = sorted(counts)
    currentLCM = sortedCounts[0] * sortedCounts[1] / GCD(sortedCounts[0], sortedCounts[1])
    for i in range(2, len(sortedCounts)):
        currentLCM = currentLCM * sortedCounts[i] / GCD(currentLCM, sortedCounts[i])
        
    print(currentLCM)
        
