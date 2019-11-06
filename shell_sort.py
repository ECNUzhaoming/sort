a=[1,2,5,6,9,3,5,7,24,6557,687];

def shell_sort(array):
  gap = len(array)
  while gap > 1:
    gap = gap // 2
    for i in range(gap, len(array)):
      for j in range(i % gap, i, gap):
        if array[i] < array[j]:
          array[i], array[j] = array[j], array[i]
  return array

print(shell_sort(a))