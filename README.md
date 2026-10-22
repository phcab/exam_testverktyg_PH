#✅ Python 3.9.6
#✅ pytest 8.4.2
#✅ Behave 1.3.3
#jag har använt vs code och mac

kör enhetstest med
python -m pytest tests/unit/test_book_store.py -v
python -m pytest tests/unit/test_fav_books.py -v
python -m pytest tests/unit/ -v

kör enhets och integrationstest med
python -m pytest tests/ -v

E2E tester
python -m behave src/features

Innan PR har jag också kontrollerat:
python -m flake8 src tests
python -m pytest --maxfail=1 --disable-warnings -q
python -m playwright install chromium

Jag siktar på G
