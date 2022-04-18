class Solution:

  def replaceElements(self, arr):

    maxSoFar = -1

    for i in range(len(arr) - 1, -1, -1):
      temp = arr[i]
      arr[i] = maxSoFar
      if temp > maxSoFar:
        maxSoFar = temp

    return arr