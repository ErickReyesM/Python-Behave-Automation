import time

from behave import *
from pages.result_page import ResultPage


@when('the user apply the filters to get a specific product')
def step_impl(context):
    context.result_page = ResultPage(context.driver)
    context.result_page.show_more_sizes()
    for row in context.table:
        context.result_page.select_size(row['size'])
        context.result_page.select_price(row['price'])
        context.result_page.select_brand(row['brand'])


@then('the user should be able to see the results')
def step_impl(context):
    assert (context.result_page.products_displayed() > 0)
    time.sleep(4)
