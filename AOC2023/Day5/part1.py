# Find the 'goal' in the current 'index' and recurse down to find the location
# goal = current number (start at seed)
# index = current map (start at 0, seed to soil)
def FindLocation(current, index, maps):
    if index >= len(maps):
        return current

    map = maps[index]

    next = -1
    for numbers in map[1:]:
        dest, source, range = numbers.split(" ")
        if (int)(source) <= current < (int)(source) + (int)(range):
            next = (int)(dest) + (current - (int)(source))
            break
    
    if next == -1:
        next = current
    
    return FindLocation(next, index + 1, maps)

if __name__ == "__main__":
    input = open("input.txt", "r").read().split("\n")

    seeds = input[0].strip().split(" ")[1:]

    #Store the maps in sublists
    maps = []
    sublist = []
    for i in range(2, len(input)):
        if input[i] == "":
            maps.append(sublist)
            sublist = []
        else:
            sublist.append(input[i])

    locations = []
    for seed in seeds:
        # Run down the maps to find the location
        locations.append(FindLocation((int)(seed), 0, maps))
    
    finalLocation = min(locations)
    print(finalLocation)