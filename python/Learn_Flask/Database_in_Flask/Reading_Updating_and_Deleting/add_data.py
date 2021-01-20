from app import db, Book, Reader, Review, Annotation
import os

if os.path.exists('myDB.db'):
  os.remove('myDB.db')
  
db.create_all()

r1 = Reader(id = 123, name = 'Ann', surname = 'Adams', email = 'ann.adams@example.com')
r2 = Reader(id = 345, name = 'Sam', surname = 'Adams', email = 'sam.adams@example.edu')
r3 = Reader(id = 450, name = 'Kim', surname = 'Smalls', email = 'kim.smalls@example.com')
r4 = Reader(id = 568, name = 'Sam', surname = 'Smalls', email = 'sam.smalls@example.com')
r5 = Reader(id = 753, name = 'Nova', surname = 'Yeni', email = 'nova.yeni@example.edu')
r6 = Reader(id = 653, name = 'Tom', surname = 'Grey', email = 'tom.grey@example.com')
db.session.add(r1)
db.session.add(r2)
db.session.add(r3)
db.session.add(r4)
db.session.add(r5)
db.session.add(r6)
try:
  db.session.commit()
except Exception:
  db.session.rollback()


b1 = Book(id = 12, title = 'Hundred years of solitude', author_name = 'Gabriel', author_surname = 'Garcia Marquez', month = 'April', year = '2020')
b2 = Book(id = 13, title = 'The Stranger', author_name = 'Albert', author_surname = 'Camus', month = 'May', year = '2020')
b3 = Book(id = 14, title = 'The Book of Why', author_name = 'Judea', author_surname = 'Pearl', month = 'September', year = '2019')
b4 = Book(id = 18, title = 'Demian', author_name = 'Herman', author_surname = 'Hesse', month = 'June', year = '2018')
b5 = Book(id = 19, title = 'Guns, Germs and Steel', author_name = 'Jared', author_surname = 'Diamond', month = 'August', year = '2019')
db.session.add(b1)
db.session.add(b2)
db.session.add(b3)
db.session.add(b4)
db.session.add(b5)
try:
  db.session.commit()
except Exception:
  db.session.rollback()

rev1 = Review(id = 111, text = 'This book is amazing...', stars = 5, reviewer_id = r1.id, book_id = b1.id)
rev2 = Review(id = 112, text = 'The story is hard to follow.', stars = 3, reviewer_id = r2.id, book_id = b1.id)
rev3 = Review(id = 113, text = 'The story is quite complicated.', stars = 2, reviewer_id = r1.id, book_id = b2.id)
rev4 = Review(id = 114, text = 'Albert Camus is an amazing writer who really understands the society.', stars =4, reviewer_id = r2.id, book_id = b2.id)
rev5 = Review(id = 115, text = 'The book is simply written and a rather quick read, but the depth Camus manages to convey through this simplicity is astounding.', stars =4, reviewer_id = r2.id, book_id = b2.id)
rev6 = Review(id = 116, text = 'Despite the fascinating subject matter I found this book a bit dry.', stars =3, reviewer_id = r4.id, book_id = b5.id)
rev7 = Review(id = 117, text = 'I liked this book, and it taught me a bunch of things.', stars =5, reviewer_id = r3.id, book_id = b5.id)

rev8 = Review(id = 118, text = 'Not bad.', stars =4, reviewer_id = r5.id, book_id = b1.id)
rev9 = Review(id = 119, text = 'Could not finish the book.', stars =3, reviewer_id = r5.id, book_id = b4.id)
db.session.add(rev1)
db.session.add(rev2)
db.session.add(rev3)
db.session.add(rev4)
db.session.add(rev5)
db.session.add(rev6)
db.session.add(rev7)
db.session.add(rev8)
db.session.add(rev9)
try:
  db.session.commit()
except Exception:
  db.session.rollback()

ann1 = Annotation(id = 331, text = 'Human history is a function of geography.', reviewer_id = r4.id, book_id = b5.id)
ann2 = Annotation(id = 332, text = 'I opened myself to the gentle indifference of the world.', reviewer_id = r1.id, book_id = b2.id)
ann3 = Annotation(id = 333, text = 'Everything is true, and nothing is true!', reviewer_id = r2.id, book_id = b2.id)
ann4 = Annotation(id = 334, text = 'Good that you ask -- you should always ask, always have doubts.', reviewer_id = r3.id, book_id = b4.id)
db.session.add(ann1)
db.session.add(ann2)
db.session.add(ann3)
db.session.add(ann4)
try:
  db.session.commit()
except Exception:
  db.session.rollback()

db.session.close()

