from behave import *
from pages.home_page import HomePage


@given('the user navigates to "{path}" page')
def step_impl(context, path):
    context.driver.get(context.base_url + path)


@when('the user writes the {word}')
def step_impl(context, word):
    context.home_page = HomePage(context.driver)
    context.home_page.write_on_class_example_input(word)


@when('selects the {country} from the available list')
def step_impl(context, country):
    context.home_page.select_country_from_the_available_list(country)


@when('the user wants to select an option from the dropdown')
def step_impl(context):
    for row in context.table:
        context.home_page.click_on_the_dropdown()
        context.home_page.select_option_from_the_dropdown(option=row['option'])


@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False
