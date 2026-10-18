#✅ Python 3.9.6
#✅ pytest 8.4.2
#✅ Behave 1.3.3
#vs code och mac

kör enhetstest med
python -m pytest tests/unit/test_book_store.py -v
python -m pytest tests/unit/test_fav_books.py -v
python -m pytest tests/unit/ -v

kör enhets och integrationstest med
python -m pytest tests/ -v
