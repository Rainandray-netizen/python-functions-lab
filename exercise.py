def sum_to(num):
  x = range(num+1)
  tehSum = 0
  for n in x:
    tehSum = tehSum + n
  return tehSum

def largest(array):
  largest = 0
  for n in array:
    if n > largest:
      largest = n
  return largest

def occurances(string, snippet):
  res = [i for i in range(len(string)) if string.startswith(snippet, i)] 
  return len(res)

# print(occurances('oh fuck there are so many goddamn bees here save me from all these bees help bees','bees'))

def productify(*nums):
  current = 1
  for n in nums:
    current *= n
  return current