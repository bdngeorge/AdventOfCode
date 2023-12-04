if __name__ == "__main__":
    summedPowers = 0
    for game in open("input.txt", "r").read().split("\n"):
        _, rounds = game.split(":")

        minimumColors = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for round in rounds.split(";"):
            for pile in round.split(","):
                num, color = pile.strip().split(" ")
                if (int)(num) > minimumColors[color]:
                    minimumColors[color] = (int)(num)
        
        summedPowers += (minimumColors["red"] * minimumColors["green"] * minimumColors["blue"])

    print(summedPowers)