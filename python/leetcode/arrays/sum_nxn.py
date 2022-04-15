def sum_all(list_of_lists):
  sum = 0
  for j in range(len(list_of_lists)):
    for k in range(len(list_of_lists[j])):
      sum += list_of_lists[j][k]
  return sum

def sum_all_2(list_of_lists):
  return sum([sum(k) for k in list_of_lists])


print(sum_all_2([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]))