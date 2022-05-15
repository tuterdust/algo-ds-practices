def search_arr_naive(arr, target_val):
  for i in range(len(arr)):
    if arr[i] == target_val:
      return arr[i]
  return None

def search_arr(arr, target_val):
  arr.sort()
 
  start = 0
  end = len(arr) - 1

  while start <= end:
    mid = int(start+(end-start)/2)
    mid_ele = arr[mid]
    if mid_ele == target_val:
      return mid_ele
    if mid_ele < target_val:
      start = mid+1
    else:
      end = mid-1

  return None

def main():
  number_arr = [4, 6, 2, 77, 921, 31, -4, 2, 0, -56, 20]
  target_number = int(input("number to search: "))

  # search for number in array
  searched_number = search_arr(number_arr, target_number)

  print(f"Searching array {number_arr}")
  if searched_number is not None:
    print(f"target value={target_number} found")
  else:
    print(f"target value={target_number} not found")

if __name__ == "__main__":
    main()
