import utils
import sorts

bookshelf = utils.load_books('books_small.csv')

# Get to know the data
print(bookshelf[0])
# 1. print the titles within the bookshelf
for book in bookshelf:
  print(book["title"])

# 2.
# What is the code point of “a”, " ", "A"?
#print(ord("a"))
#print(ord(" "))
#print(ord("A"))

# 6. define a sort comparison function:
def by_title_ascending(book_a, book_b):
  return book_a["title_lower"] > book_b["title_lower"]

# 7. Sort the bookshelf using bubble sort:
sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
for book in sort_1:
  print(book["title"])

# A new sorting order
# 8. Define a new comparison function:
def by_author_ascending(book_a, book_b):
  return book_a["author_lower"] > book_b["author_lower"]

# 9., 14. create a new copy of 'bookshelf':
# print(type(bookshelf))
bookshelf_v1 = list(bookshelf)
bookshelf_v2 = list(bookshelf)

# 10. sorting the list of books, bookshelf_v1 by authors:
sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
for book in sort_2:
  print(book["author"])

# A new sorting algorithm
# 11, 15. 
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)
print("\nQuicksort")
for book in bookshelf_v2:
  print(book["author"])

# 16. sorting by the length of the sum of the number of characters 
def by_total_length(book_a, book_b):
  sum_title_chars_a = len(book_a["title"] + book_a["author"])
  sum_title_chars_b = len(book_b["title"] + book_b["author"])
  return sum_title_chars_a > sum_title_chars_b

# 17. Load the long list of books
long_bookshelf = utils.load_books('books_large.csv')

# 18. Run bubble sort:
#sort_long = sorts.bubble_sort(long_bookshelf, by_total_length)

# 19. 
sorts.quicksort(long_bookshelf, 0, len(long_bookshelf) - 1, by_total_length)

# 20. By the reverse of the author’s name
def by_author_descending(book_a, book_b):
  return book_a["author_lower"] < book_b["author_lower"]

sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_descending)
print("\nQuicksort descending")
for book in bookshelf_v2:
  print(book["author"])
