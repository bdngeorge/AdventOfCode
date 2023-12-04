rules = {
    "red": 12,
    "green": 13,
    "blue": 14
}

if __name__ == "__main__":
    totaledIds = 0
    for game in open("input.txt", "r").read().split("\n"):
        gameNum, rounds = game.split(":")
        id = (int)(gameNum[5:])

        valid = True
        for round in rounds.split(";"):
            for pile in round.split(","):
                num, color = pile.strip().split(" ")
                if (int)(num) > rules[color]:
                    valid = False
                    break
        
        if valid:
            print(id)
            totaledIds += id

    print(totaledIds)