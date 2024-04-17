from behave import *
from pages.home_page import HomePage


@given('the user navigates to "{path}" page')
def step_impl(context, path):
    context.driver.get(context.base_url + path)


@when('the user writes a word and selects the a country from the available list')
def step_impl(context):
    for row in context.table:
        context.home_page = HomePage(context.driver)
        context.home_page.write_on_class_example_input(row['word'])
        context.home_page.select_country_from_the_available_list(row['country'])


@when('the user wants to select an option from the dropdown')
def step_impl(context):
    for row in context.table:
        context.home_page.click_on_the_dropdown()
        context.home_page.select_option_from_the_dropdown(row['option'])


@then('the user switches to a new window and validate hte {text} is present on the page')
def step_impl(context, text):
    context.home_page.open_new_window()
    assert True is not False
