from src.fav_books import FavoriteBooks

class BookStore:
    def __init__(self):
        self.books = []
        self.favorites = FavoriteBooks()
        self.next_id = 1

    def addBook(self, author, title):
        book = {
            "id": self.next_id,
            "author": author,
            "title": title
        }
        self.books.append(book)
        self.next_id += 1

    def toggleFavorite(self, book_id):
        book = next(
            (book for book in self.books if book["id"] == book_id),
            None
        )

        if book is None:
            return

        if book in self.favorites.books:
            self.favorites.remove(book)
        else:
            self.favorites.add(book)

# _init__ skapar en tom lista 

# Ta emot författare och titel
# SkP en dictionary för bokwn

# Lägg till boken i listan self.books

# toggleFavorite(book_id)

# self.favorites = FavoriteBooks() skapar en favoritlista 
# self.next_id håller reda på nästa ID som ska tilldelas
# addBook() skapar en bok med ID, författare och titel
# toggleFavorite() letar upp boken via ID
# Om boken redan är favorit tas den bort; annars läggs den till (twice - tar bort)