a=[1,2,5,6,9,3,5,7,24,6557,687];

def bubble_sort(array):
  for i in range(len(array)):
    for j in range(i, len(array)):
      if array[i] > array[j]:
        array[i], array[j] = array[j], array[i]
  return array

print(bubble_sort(a))