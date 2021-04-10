# what if we wanted to use recursion?
def palindrome_1(str):
  if len(str) <= 1:
    return True
  if str[0] != str[-1]:
    return False
  return palindrome_1(str[1:-1])

# what if we didn't care about case?
def palindrome_2(str):
  lower = str.lower()
  for i in range(len(str) // 2):
    if lower[i] != lower[-i - 1]:
      return False
  return True

# what if we wanted to ignore punctuation?
def palindrome_3(str):
  punctuation = [',', '!', '?', '.']
  no_punc_str = str[:]
  for punc in punctuation:
    no_punc_str = no_punc_str.replace(punc, '')
  for i in range(len(no_punc_str) // 2):
    if no_punc_str[i] != no_punc_str[-i - 1]:
      return False
  return True 

# what if we wanted to ignore space?
def palindrome_4(str):
  no_space_str = str.replace(' ', '')
  for i in range(len(no_space_str) // 2):
    if no_space_str[i] != no_space_str[-i - 1]:
      return False
  return True 
