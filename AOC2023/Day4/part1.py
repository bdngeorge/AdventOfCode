import re

if __name__ == "__main__":
  input = open("input.txt", "r").read().strip().split("\n")

  total = 0
  for game in input:
    _, numbers = game.strip().split(":")

    winningNumsStr = numbers.strip().split("|")[0]
    elfsNumsStr = numbers.strip().split("|")[1]

    winningNums = re.findall(r'\d+', winningNumsStr)
    elfsNums = re.findall(r'\d+', elfsNumsStr)

    subtotal = 0
    for number in elfsNums:
      if number in winningNums:
        if subtotal == 0:
          subtotal += 1
        else:
          subtotal *= 2
    
    total += subtotal

  print(total)