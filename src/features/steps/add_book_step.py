from behave import then
from playwright.sync_api import expect


@then("Vill jag kunna lägga till en bok som saknas i listan")
def step_add_book(context):
    page = context.base_page.page
    page.get_by_role("button", name="Lägg till bok").click()


@then("Registrera och spara titel och författare")
def step_add_book_details(context):
    page = context.base_page.page

    page.get_by_test_id("add-input-title").fill("Testbokens Titel")
    page.get_by_test_id("add-input-author").fill("Författarens Namn")

    page.get_by_role("button", name="Lägg till ny bok").click()


@then("Se boken i boklistan")
def step_view_book(context):
    page = context.base_page.page
    page.get_by_role("button", name="Katalog").click()
    expect(page.get_by_text("Testbokens Titel")).to_be_visible()
