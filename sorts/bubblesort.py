def bubble_sort(arr):
  swaps = 0
  sorted = False
  while not sorted:
    sorted = True
    for idx in range(len(arr) - 1):
      if arr[idx] > arr[idx + 1]:
        sorted = False
        arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
        swaps += 1
  return arr
