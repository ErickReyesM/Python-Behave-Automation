from behave import *
from pages.home_page import HomePage


@given('the user navigates to the "{path}" page')
def step_impl(context, path):
    context.driver.get(context.base_url + path)


@when('the user search for an article in the store')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    for row in context.table:
        context.home_page.search_article(row['article'])


@then('the suggested articles should be displayed')
def step_impl(context):
    assert (context.home_page.suggestion_displayed())
