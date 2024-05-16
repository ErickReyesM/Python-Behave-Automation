from behave import *
from pages.home_page import HomePage


@given('the user navigates to the "{path}" page')
def step_impl(context, path):
    context.driver.get(context.base_url + path)


@when('the user search for {article} in the store')
def step_impl(context, article):
    context.home_page = HomePage(context.driver)
    context.article = article
    context.home_page.search_article(context.article)


@then('related articles to {article} should be displayed as suggestion')
def step_impl(context, article):
    assert (article in context.home_page.suggestion_displayed())


@when('the user selects the {option} from the available options')
def step_impl(context, option):
    context.home_page.click_on_option(option)


@when('the user navigates to the results page to see the available options')
def step_impl(context):
    context.home_page.click_on_search_option()
