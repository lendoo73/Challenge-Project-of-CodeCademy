def sparse_search(data, search_val):
  print("Data: " + str(data))
  print("Search Value: " + str(search_val))
  # 1.:
  first = 0
  last = len(data) - 1
  # 2.:
  while first <= last:
    # 3.:
    mid = (first + last) // 2
    # 4.:
    if not data[mid]:
      # 5.:
      left = mid -1
      right = mid + 1
      # 6.:
      while True:
        # 7-8.:
        if left < first and right > last:
          print("{0} is not in the dataset".format(search_val)) 
          return
        # 9.:
        elif right <= last and data[right]:
          mid = right
          break
        # 10.:
        elif left >= first and data[left]:
          mid = left
          break
        # 11.:
        right += 1
        left -= 1

    # 12-13.:
    if data[mid] == search_val:
      print("{0} found at position {1}".format(search_val, mid))
      return
    
    # 14.:
    if search_val < data[mid]:
      last = mid - 1
    # 15.:
    if search_val > data[mid]:
      first = mid + 1
  
  # 16-17.:
  print("{0} is not in the dataset".format(search_val))
