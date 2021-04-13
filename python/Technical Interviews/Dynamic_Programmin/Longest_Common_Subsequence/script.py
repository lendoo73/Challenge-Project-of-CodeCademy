# 1-2. Setting up the Problem
dna_1 = "ACCGTT"
#dna_1 = "ABAZDC"
dna_2 = "CCAGCA"
#dna_2 = "BACBAD"

def longest_common_subsequence(string_1, string_2):
  print("Finding longest common subsequence of {0} and {1}".format(string_1, string_2))

  # 3-6. Creating a Grid
  col_length = len(string_1) + 1
  row_length = len(string_2) + 1
  grid = [
    [0 for col in range(col_length)]
    for row in range(row_length)
  ]

  for row in range(1, row_length):
    print("Comparing: {0}".format(string_2[row - 1]))
    
    for col in range(1, col_length):
      print("Against: {0}".format(string_1[col - 1]))

      # 7. Filling the Grid:
      if string_1[col - 1] == string_2[row - 1]:
        # letters match:
        grid[row][col] = grid[row - 1][col - 1] + 1
      else:
        grid[row][col] = max(grid[row - 1][col], grid[row][col - 1])
  
  for row_line in grid:
    print(row_line)
  # construct subsequence
  result = []
  while row > 0 and col > 0:
    if string_1[col - 1] == string_2[row - 1]:
      result.append(string_1[col - 1])
      row -= 1
      col -= 1
    elif grid[row - 1][col] > grid[row][col - 1]:
      row -= 1
    else:
      col -= 1
  result.reverse()
  return "".join(result), grid[-1][-1]

sequence, num = longest_common_subsequence(dna_1, dna_2)

print(sequence)
print(num)
