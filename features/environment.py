import os
from selenium import webdriver
from behave import fixture, use_fixture
from selenium.webdriver.chrome.options import Options as AndroidOptions
from selenium.webdriver.safari.options import Options as IOSOptions


@fixture
def browser_ios(context):
    ios_options = IOSOptions()
    ios_options.set_capability('platformName', 'ios')
    ios_options.set_capability('os_version', '16')
    ios_options.set_capability('device', 'iPhone 14')
    ios_options.set_capability('browserName', 'iphone')
    ios_options.set_capability('buildName', 'Stori_Automation_Practice_0.1')
    context.driver = webdriver.Remote(
        command_executor=context.browser_stack_url,
        options=ios_options
    )


@fixture
def browser_android(context):
    android_options = AndroidOptions()
    android_options.set_capability('platformName', 'android')
    android_options.set_capability('platformVersion', '9.0')
    android_options.set_capability('deviceName', 'Google Pixel 3')
    android_options.set_capability('buildName', 'Stori_Automation_Practice_0.1')
    context.driver = webdriver.Remote(
        command_executor=context.browser_stack_url,
        options=android_options
    )


def before_all(context):
    platform = context.config.userdata.get('platform', 'android')
    browserstack_username = os.environ.get('BROWSERSTACK_USERNAME')
    browserstack_access_key = os.environ.get('BROWSERSTACK_ACCESS_KEY')
    context.base_url = "https://rahulshettyacademy.com/"
    context.browser_stack_url = f"https://{browserstack_username}:{browserstack_access_key}@hub-cloud.browserstack.com/wd/hub"
    if platform.lower() == 'ios':
        use_fixture(browser_ios, context)
    elif platform.lower() == 'android':
        use_fixture(browser_android, context)
    else:
        raise Exception(f"Unsupported platform: {platform}")


def after_all(context):
    context.driver.quit()
