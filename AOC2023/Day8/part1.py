import collections as c

if __name__ == "__main__":
    input = open("input.txt", "r").read().strip().split("\n")

    directions = input[0]

    mapMap = c.defaultdict(lambda:())
    for direction in input[2:]:
        element, map = direction.strip().split("=")
        mapMap[element.strip()] = (map.strip()[1:4], map.strip()[6:9])
    
    steps = 1
    i = 0
    currentNode = 'AAA'
    while True:
        if i == len(directions):
            i = 0
            continue

        if directions[i] == 'L':
            currentNode = mapMap[currentNode][0]
        else:
            currentNode = mapMap[currentNode][1]
        
        if currentNode == 'ZZZ':
            break

        i += 1
        steps += 1

    
    print(steps)
        
