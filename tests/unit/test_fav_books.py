from src.fav_books import FavoriteBooks

def test_add_book_to_favorites():
    favorites = FavoriteBooks()
    book = {"id": 100, "title": "Titel", "author": "Författare"}

    favorites.add(book)

    assert book in favorites.books

def test_remove_book_from_favorites():
    favorites = FavoriteBooks()
    book = {
        "id": 100,
        "title": "Titel",
        "author": "Författare"
    }

    favorites.add(book)
    favorites.remove(book)

    assert book not in favorites.books
    