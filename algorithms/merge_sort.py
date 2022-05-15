def merge_sort(arr):
  n = len(arr)

  # base case
  if n == 1:
    return arr

  mid = int(n/2)
  left_arr = arr[:mid]
  right_arr = arr[mid:]
  merge_sort(left_arr)
  merge_sort(right_arr)

  # merge left and rigt arrays to target array
  i = j = k = 0
  while i < len(left_arr) and j < len(right_arr):
    if left_arr[i] < right_arr[j]:
      arr[k] = left_arr[i]
      i += 1
    else:
      arr[k] = right_arr[j]
      j += 1
    k += 1 # go to next index of target array after adding new element

  # in case there are leftovers in left arr
  while i < len(left_arr):
    arr[k] = left_arr[i]
    i += 1
    k += 1

  # in case there are leftovers in right arr
  while j < len(right_arr):
    arr[k] = right_arr[j]
    j += 1
    k += 1

def main():
  input_str = input("array to sort: ")
  input_arr = input_str.split(",")
  merge_sort(input_arr)
  print(input_arr)

if __name__ == "__main__":
  main()
