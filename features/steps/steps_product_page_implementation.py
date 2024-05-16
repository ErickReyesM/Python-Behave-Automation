from behave import *
from pages.product_page import ProductPage


@then('the user should be able to see the product detail page')
def step_impl(context):
    context.product_page = ProductPage(context.driver)
    assert (context.product_page.product_title_displayed() and context.product_page.product_price_displayed())
