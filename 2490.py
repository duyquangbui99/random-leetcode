def isCircularSentence(sentence): # beat 100% in time complexity 
  if sentence[0] != sentence[-1]:
      return False
  arr = sentence.split()
  char = arr[0][-1]
  for i in range(1, len(arr)):
      if char == arr[i][0]:
          char = arr[i][-1]
      else:
          return False
  return True
