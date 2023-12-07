def GetHandLocalRank(hand):
    cardDict = {}
    for card in hand[0]:
        if card not in cardDict:
            cardDict[card] = 0
        cardDict[card] += 1
    
    print(cardDict)

def SortHands(hands):
    pass

if __name__ == "__main__":
    input = open("inputSmall.txt", "r").read().strip().split("\n")

    hands = []
    for line in input:
        hands.append(line.split(" "))
    
    for hand in hands:
        GetHandLocalRank(hand)