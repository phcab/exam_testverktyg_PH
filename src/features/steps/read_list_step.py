from behave import given, when, then
from playwright.sync_api import expect


@given("Att jag som användare")
def step_user(context):
    pass


@when("Går in på websidan")
def step_open_website(context):
    context.base_page.open(
        "https://tap-ht25-testverktyg.github.io/exam/"
    )


@then("Vill jag kunna se lista över böcker")
def step_check_book_list(context):
    page = context.base_page.page
    expect(page).to_have_title("Läslistan")


@when(u'jag favoritmarkerar en bok i listan')
def step_mark_as_favorite(context):
    page = context.base_page.page

    favorite = page.get_by_test_id(
        "star-The Pragmatic Procrastinator"
    )
    expect(favorite).to_be_visible()
    favorite.click()

    # print("Före klick:", favorite.get_attribute("class"))


@then("ska boken vara favoritmarkerad")
def step_check_favorite(context):
    page = context.base_page.page
    favorite = page.get_by_test_id(
        "star-The Pragmatic Procrastinator"
    )
    expect(favorite).to_have_class("star selected")


@when("har en favoritmarkerad bok i boklistan")
def step_favorite_already_selected(context):
    page = context.base_page.page
    favorite = page.get_by_test_id(
        "star-The Pragmatic Procrastinator"
    )
    expect(favorite).to_have_class("star selected")


@when("tar bort en favoritmarkering i boklistan")
def favorite_mark_delete(context):
    page = context.base_page.page
    favorite = page.get_by_test_id(
        "star-The Pragmatic Procrastinator"
    )
    favorite.click()


@then("boken visas utan favoritmarkering i boklistan")
def step_check_favorite_removed(context):
    page = context.base_page.page
    favorite = page.get_by_test_id(
        "star-The Pragmatic Procrastinator"
    )
    expect(favorite).to_have_class("star")
