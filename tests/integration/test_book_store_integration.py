from src.book_store import BookStore


def test_add_book_and_toggle_favorite():
    # Arrange
    store = BookStore()

    # Act
    store.addBook("Författare", "Titel")
    book = store.books[0]
    store.toggleFavorite(book["id"])

    # Assert
    assert book in store.favorites.books


def test_toggle_favorite_twice_removes_book():
    # Arrange
    store = BookStore()
    store.addBook("Författare", "Titel")
    book = store.books[0]

    # Act
    store.toggleFavorite(book["id"])
    store.toggleFavorite(book["id"])

    # Assert
    assert book not in store.favorites.books

# skapa en bok, markera den som favorit och
# kontrollera att den finns i favoritlistan
