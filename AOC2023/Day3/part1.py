import re

def CheckNumber(i, j, l, input):
  if j-1 >= 0 and input[i][j-1] != ".": #left of number
    return True
  if j+l < len(input[i]) and input[i][j+l] != ".": #right of number
    return True
  for k in range(j-1, j+l+1):
    if k < 0 or k >= len(input[i]):
      continue
    if i+1 < len(input): #below number
      if not input[i+1][k].isdigit() and input[i+1][k] != ".":
        return True
    if i-1 >= 0: #above number
      if not input[i-1][k].isdigit() and input[i-1][k] != ".":
        return True
  
  return False
      
if __name__ == "__main__":
  input = open("input.txt", "r").read().strip().split("\n")
  
  total = 0
  for line in input:
    matches = re.finditer(r'\d+', line)
    for match in matches:
      if CheckNumber(input.index(line), match.start(), len(match.group()), input):
        total += (int)(match.group())

  print(total)

    