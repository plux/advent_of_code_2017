sum = 0
file = open('input.txt', 'r')
input = str(file.readline())
halfway = len(input) / 2
for counter in range (0, len(input)):
  if counter + halfway >= len(input):
    next = counter + halfway -len(input)
  else:
    next = counter + halfway
  if input[counter]==input[next]:
    sum+=int(input[counter])

print sum

"""
for ix, pos in enumerate(input):
  
    if pos == input[ix+1]:
      sum += int(pos)
  else:
      if pos == input[0]:
        sum += int(pos)

print sum"""
