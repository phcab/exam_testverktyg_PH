from behave import when, then
from playwright.sync_api import expect


@then(u'Ser boklistan och möjlighet Lägg till bok')
def step_add_book(context):
    page = context.base_page.page
    expect(page.get_by_role("button", name="Lägg till bok")).to_be_visible()


@when(u'Saknar en bok i listan som visas')
def step_add_book_button(context):
    page = context.base_page.page
    page.get_by_role("button", name="Lägg till bok").click()


@when(u'lägger till en bok som saknas i listan')
def step_add_book_details(context):
    page = context.base_page.page

    page.get_by_test_id("add-input-title").fill("Testbokens Titel")
    page.get_by_test_id("add-input-author").fill("Författarens Namn")

    page.get_by_role("button", name="Lägg till ny bok").click()


@then(u'vill jag se den tillagda boken i boklistan')
def step_view_book(context):
    page = context.base_page.page
    page.get_by_role("button", name="Katalog").click()
    expect(page.get_by_text("Testbokens Titel")).to_be_visible()
