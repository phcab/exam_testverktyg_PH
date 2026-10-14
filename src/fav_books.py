class FavoriteBooks:
     def __init__(self):
        self.books = []

     def add(self, book):
        self.books.append(book)

     def remove(self, book):
        self.books.remove(book)
 
# _init__ skapar en tom lista 
# add(self, book) tar emot en bok
# self.books.append(book) lägger till i listan
# remove
