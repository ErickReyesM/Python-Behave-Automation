import os
from selenium import webdriver
from behave import fixture, use_fixture
from selenium.webdriver.chrome.options import Options as AndroidOptions
from selenium.webdriver.safari.options import Options as IOSOptions
from selenium.webdriver.safari.options import Options as WindowsOptions


@fixture
def browser_ios(context):
    ios_options = IOSOptions()
    ios_options.set_capability('platformName', 'ios')
    ios_options.set_capability('os_version', '16')
    ios_options.set_capability('device', 'iPhone 14')
    ios_options.set_capability('browserName', 'iphone')
    ios_options.set_capability('buildName', 'Apex_0.1')
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
    android_options.set_capability('buildName', 'Apex_0.1')
    context.driver = webdriver.Remote(
        command_executor=context.browser_stack_url,
        options=android_options
    )

@fixture
def windows_browser(context):
    desktop_options = WindowsOptions()
    desktop_options.set_capability('platformName', 'Windows')
    desktop_options.set_capability('platformVersion', 11)
    desktop_options.set_capability('browserName', 'Chrome')
    desktop_options.set_capability('browserVersion', 'latest')
    desktop_options.set_capability('buildName', 'Apex_0.1')
    context.driver = webdriver.Remote(
        command_executor=context.browser_stack_url,
        options=desktop_options
    )
    context.driver.maximize_window()


def before_all(context):
    platform = context.config.userdata.get('platform', 'desktop')
    browserstack_username = os.environ.get('BROWSERSTACK_USERNAME')
    browserstack_access_key = os.environ.get('BROWSERSTACK_ACCESS_KEY')
    context.base_url = "https://www.liverpool.com.mx/tienda/"
    context.browser_stack_url = f"https://{browserstack_username}:{browserstack_access_key}@hub-cloud.browserstack.com/wd/hub"
    if platform.lower() == 'ios':
        use_fixture(browser_ios, context)
    elif platform.lower() == 'android':
        use_fixture(browser_android, context)
    elif platform.lower() == 'desktop':
        use_fixture(windows_browser, context)
    else:
        raise Exception(f"Unsupported platform: {platform}")


def after_all(context):
    context.driver.quit()
