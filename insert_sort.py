a=[1,2,5,6,9,3,5,7,24,6557,687];

def insert_sort(array):
  for i in range(len(array)):
    for j in range(i):
      if array[i] < array[j]:
        array.insert(j, array.pop(i))
        break
  return array

print(insert_sort(a));