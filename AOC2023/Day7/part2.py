import collections as c
from functools import cmp_to_key

cardRanks = {"J":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "Q":12, "K":13, "A":14}

def GetLocalRank_Normal(hand):
    cardDict = c.defaultdict(lambda:0)
    for card in hand[0]:
        cardDict[card] += 1
    values = sorted(cardDict.values())

    if values == [5]:
        return 6
    elif values == [1,4]:
        return 5
    elif values == [2,3]:
        return 4
    elif values == [1,1,3]:
        return 3
    elif values == [1,2,2]:
        return 2
    elif values == [1,1,1,2]:
        return 1
    else:
        return 0   
    
def GetLocalRank_WildCard(hand):
    if 'J' not in hand[0]:
        return GetLocalRank_Normal(hand)
    
    cardDict = c.defaultdict(lambda:0)
    for card in hand[0]:
        cardDict[card] += 1
    values = sorted(cardDict.values())
    
    if values == [5] or values == [1,4] or values == [2,3]:
        return 6
    elif values == [1,1,3]:
        return 5
    elif values == [1,2,2]:
        if cardDict['J'] == 1:
            return 4
        return 5
    elif values == [1,1,1,2]:
        return 3
    else:
        return 1
    
def CompareHands(h1, h2):
     h1Rank = GetLocalRank_WildCard(h1)
     h2Rank = GetLocalRank_WildCard(h2)

     if h1Rank < h2Rank:
         return -1
     elif h1Rank == h2Rank:
         for i in range(len(h1[0])):
             if cardRanks[h1[0][i]] == cardRanks[h2[0][i]]:
                 continue
             elif cardRanks[h1[0][i]] < cardRanks[h2[0][i]]:
                 return -1
             else:
                 return 1

     return 1

if __name__ == "__main__":
    input = open("input.txt", "r").read().strip().split("\n")

    hands = []
    for line in input:
        hands.append(line.split(" "))
    
    total = 0
    sortedHands = sorted(hands, key=cmp_to_key(CompareHands))
    for i in range(len(sortedHands)):
        total += (int(sortedHands[i][1]) * (i+1))

    print(total)