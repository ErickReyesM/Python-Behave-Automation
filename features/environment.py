import os
from selenium import webdriver
from behave import fixture, use_fixture
from selenium.webdriver.chrome.options import Options as RemoteOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@fixture
def remote_browser(context):
    remote_options = RemoteOptions()
    remote_options.set_capability('platformName', 'Windows')
    remote_options.set_capability('platformVersion', 11)
    remote_options.set_capability('browserName', 'Chrome')
    remote_options.set_capability('browserVersion', 'latest')
    remote_options.set_capability('buildName', 'Apex_0.1')
    context.driver = webdriver.Remote(
        command_executor=context.browser_stack_url,
        options=remote_options
    )
    context.driver.maximize_window()


@fixture
def local_browser(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.maximize_window()


def before_all(context):
    platform = context.config.userdata.get('platform', 'remote')
    browserstack_username = os.environ.get('BROWSERSTACK_USERNAME')
    browserstack_access_key = os.environ.get('BROWSERSTACK_ACCESS_KEY')
    context.base_url = "https://www.liverpool.com.mx/tienda/"
    context.browser_stack_url = f"https://{browserstack_username}:{browserstack_access_key}@hub-cloud.browserstack.com/wd/hub"
    if platform.lower() == 'remote':
        use_fixture(remote_browser, context)
    elif platform.lower() == 'local':
        use_fixture(local_browser, context)
    else:
        raise Exception(f"Unsupported platform: {platform}")


def after_all(context):
    context.driver.quit()
