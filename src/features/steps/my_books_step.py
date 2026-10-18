from behave import then
from playwright.sync_api import expect


@then(
    u'ska knappen Mina böcker gå till lista som visar bara mina '
    u'favoritmarkerade böcker')
def step_my_books(context):
    # Klicka på knappen Mina böcker
    context.page.get_by_role("button", name="Mina Böcker").click()

    # Hitta listan med böcker
    book_list = context.page.get_by_test_id("book-list")

    # Kontrollera att listan visas
    expect(book_list).to_be_visible()

    # Kontrollera att alla böcker i listan är favoritmarkerade
    expect(book_list.locator("li.book")).not_to_have_count(0)
    expect(book_list.locator("li:not(.book)")).to_have_count(0)
