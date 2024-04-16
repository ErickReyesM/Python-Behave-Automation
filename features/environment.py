import os
from selenium import webdriver
from behave import fixture, use_fixture
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.safari.options import Options


@fixture
def browser_ios(context):
    ios_options = Options()
    ios_options.set_capability('platformName', 'ios')
    ios_options.set_capability('platformVersion', '16')
    ios_options.set_capability('deviceName', 'iPhone 14')
    context.driver = webdriver.Remote(
        command_executor=f"https://{os.environ.get('BROWSERSTACK_USERNAME')}:{os.environ.get('BROWSERSTACK_ACCESS_KEY')}"
                         f"@hub-cloud.browserstack.com/wd/hub",
        options=ios_options
    )
    context.driver.implicitly_wait(2)


@fixture
def browser_android(context):
    android_options = Options()
    android_options.set_capability('platformName', 'android')
    android_options.set_capability('platformVersion', '9.0')
    android_options.set_capability('deviceName', 'Google Pixel 3')
    context.driver = webdriver.Remote(
        command_executor="https://erickreyes_Dc0zuJ:pjaxzTydTWC7b4qN7XGn@hub-cloud.browserstack.com/wd/hub",
        options=android_options
    )
    context.driver.implicitly_wait(2)


def before_all(context):
    platform = context.config.userdata.get('platform', 'ios')
    context.base_url = "https://rahulshettyacademy.com/"
    if platform.lower() == 'ios':
        use_fixture(browser_ios, context)
    elif platform.lower() == 'android':
        use_fixture(browser_android, context)
    else:
        raise Exception(f"Unsupported platform: {platform}")


def after_all(context):
    context.driver.quit()
