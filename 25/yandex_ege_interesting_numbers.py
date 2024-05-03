# In this task interesting number is number, which have 3 dividers, that are squares
def isInteresting(number) -> bool:
  countDel = 0
  for i in range(2, int(i**0.5)+1):
    if i ** 0.5 == int(i**0.5):
      if number % i == 0:
        countDel += 1
    if (number // i) ** 0.5 == int((number // i) ** 0.5):
      if number % (number // i) == 0:
        countDel += 1
  if countDel == 3:
    return True
  else:
    return False


# Function, which found max square divider
def maxDel(number) -> int:
  mxDel = 0
  for i in range(2, int(i**0.5) + 1):
    if i ** 0.5 == int(i ** 0.5):
      if number % i == 0:
        mxDel = max(mxDel, i)
    if (number // i) ** 0.5 == int((number // i) ** 0.5):
      if number % (number // i) == 0:
        mxDel = max(mxDel, number // i)


number = 10**7
count = 0
while count < 5:
  if isInteresting(number):
    count += 1
    print(number, maxDel(number))
  number += 1
