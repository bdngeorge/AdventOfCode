import re

if __name__ == "__main__":
  input = open("input.txt", "r").read().strip().split("\n")

  total = 0
  copies = {}
  for game in input:
    card, numbers = game.strip().split(":")

    winningNumsStr = numbers.strip().split("|")[0]
    elfsNumsStr = numbers.strip().split("|")[1]

    winningNums = re.findall(r'\d+', winningNumsStr)
    elfsNums = re.findall(r'\d+', elfsNumsStr)
    cardNum = (int)(card.split(" ")[-1])
    if cardNum not in copies.keys():
      copies[cardNum] = 1

    subtotal = 0
    matches = 0
    for number in elfsNums:
      if number in winningNums:
        if subtotal == 0:
          subtotal += 1
        else:
          subtotal *= 2
        matches += 1
    
    if matches > 0:
      for i in range(cardNum+1, matches+cardNum+1):
        if i not in copies.keys():
          copies[i] = 1
        copies[i] += copies[cardNum]
    
    total += subtotal

  totalCopies = 0
  for key in copies:
    totalCopies += copies[key]
  
  print(totalCopies)
  print(total)