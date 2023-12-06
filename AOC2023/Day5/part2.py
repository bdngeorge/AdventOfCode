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

def FindPossibleSeeds(ranges, index, maps):
    if index >= len(maps):
        return ranges

    map = maps[index]

    newRanges = []
    for numbers in map[1:]:
        dest, source, span = numbers.split(" ")
        transformation = int(dest) - int(source)
        transformationRange = [int(source), int(source) + int(span) - 1]
        #seedsToChange = [i for i in range((int)(source), (int)(source)+(int)(span))]
        
        #check each map and apply transformation on source ranges
        # (cx, cy) (nx, ny)
        # if cx <= nx <= xy <= cy
        # if nx <= cx <= ny <= cy
        # if cx <= nx < ny <= cy

        
if __name__ == "__main__":
    input = open("inputSmall.txt", "r").read().split("\n")

    seedRanges = input[0].strip().split(" ")[1:]
    print(seedRanges)

    #Store the maps in sublists
    maps = []
    sublist = []
    for i in range(2, len(input)):
        if input[i] == "":
            maps.append(sublist)
            sublist = []
        else:
            sublist.append(input[i])

    print("Running...")
    locations = []
    for i in range(len(seedRanges)):
        if i % 2 == 0:
            x = (int)(seedRanges[i])
            y = (int)(seedRanges[i+1])+x
            possibleSeeds = FindPossibleSeeds([[x, y]], 0, maps)
    
    #finalLocation = min(locations)
    #print("Location found!\n" + str(finalLocation))