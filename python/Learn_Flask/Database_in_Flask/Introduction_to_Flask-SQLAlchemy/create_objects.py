#This is a separate Python script in which we practice creating database objects
#You can also perform these operations in command-line terminal
from app import Reader, Book, Review

b1 = Book(id = 123, title = 'Demian', author_name = 'Hermann', author_surname = 'Hesse')
b2 = Book(id = 533, title = 'The stranger', author_name = 'Albert', author_surname = 'Camus')
r1 = Reader(id = 342, name = 'Ann', surname = 'Adams', email = 'ann.adams@example.com')
r2 = Reader(id = 312, name = 'Sam', surname = 'Adams', email = 'sam.adams@example.com')

rev1 = Review(id = 435, text = 'This book is amazing...', stars = 5, reviewer_id = r1.id, book_id = b1.id)
print(rev1) #prints the rev1 object
print(rev1.text) #prints the text of the review rev1
print(rev1.book_id) #prints the id of the book for which the review was written

#Checkpoint 1: 
rev2 = Review(id = 450, reviewer_id = r2.id, book_id = b2.id, text = "This book is difficult!", stars = 2)

#Checkpoint 2:
print(len(rev2.text.split()))

