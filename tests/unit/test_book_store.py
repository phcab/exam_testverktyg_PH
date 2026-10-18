from src.book_store import BookStore


def test_add_book():
    # Arrange
    store = BookStore()

    # Act
    store.addBook("Författare", "Titel")

    # Assert
    assert len(store.books) == 1
    assert store.books[0]["author"] == "Författare"
    assert store.books[0]["title"] == "Titel"


def test_toggle_favorite():
    store = BookStore()
    store.addBook("Författare", "Titel")

    book_id = store.books[0]["id"]
    store.toggleFavorite(book_id)

    assert store.books[0] in store.favorites.books


def test_toggle_favorite_with_unknown_id():
    store = BookStore()
    store.addBook("Författare", "Titel")

    store.toggleFavorite(999)

    assert store.favorites.books == []
