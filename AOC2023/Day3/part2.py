import re

gears = {}

#Definitely super readable code right here... If it works, it works :)
def CheckNumber(i, j, l, input):
  symbolsFound = {}
  if j-1 >= 0 and input[i][j-1] != ".": #left of number
    if not input[i][j-1] in symbolsFound.keys():
      symbolsFound[input[i][j-1]] = []
    symbolsFound[input[i][j-1]].append((i, j-1))
  if j+l < len(input[i]) and input[i][j+l] != ".": #right of number
    if not input[i][j+l] in symbolsFound.keys():
      symbolsFound[input[i][j+l]] = []
    symbolsFound[input[i][j+l]].append((i, j+l))
  for k in range(j-1, j+l+1):
    if k < 0 or k >= len(input[i]):
      continue
    if i+1 < len(input): #below number
      if not input[i+1][k].isdigit() and input[i+1][k] != ".":
        if not input[i+1][k] in symbolsFound.keys():
          symbolsFound[input[i+1][k]] = []
        symbolsFound[input[i+1][k]].append((i+1, k))
    if i-1 >= 0: #above number
      if not input[i-1][k].isdigit() and input[i-1][k] != ".":
        if not input[i-1][k] in symbolsFound.keys():
          symbolsFound[input[i-1][k]] = []
        symbolsFound[input[i-1][k]].append((i-1, k))
  
  if len(symbolsFound.keys()) > 0:
    if "*" in symbolsFound.keys():
      for index in symbolsFound["*"]:
        if not index in gears.keys():
          gears[index] = []
        gears[index].append(input[i][j:j+l])
    return True

  return False

def FindGearRatio(gears):
  total = 0
  for key in gears:
    if key == ():
      continue
    if len(gears[key]) == 2:
      ratio = 1
      for value in gears[key]:
        ratio *= (int)(value)
      total += ratio

  return total
      
if __name__ == "__main__":
  input = open("input.txt", "r").read().strip().split("\n")
  
  total = 0
  for line in input:
    matches = re.finditer(r'\d+', line)
    for match in matches:
      if CheckNumber(input.index(line), match.start(), len(match.group()), input):
        total += (int)(match.group())

  print(total)
  print(FindGearRatio(gears))

    