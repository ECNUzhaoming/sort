a=[1,2,5,6,9,3,5,7,24,6557,687];

def select_sort(array):
  for i in range(len(array)):
    x = i # min index
    for j in range(i, len(array)):
      if array[j] < array[x]:
        x = j
    array[i], array[x] = array[x], array[i]
  return array

print(select_sort(a))