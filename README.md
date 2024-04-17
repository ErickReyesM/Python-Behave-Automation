# Stori-QA-Automation-Challenge


This project demonstrates how to execute tests using Python Behave on BrowserStack, launching the default browser for Android using a Google Pixel 3 and iOS on an iPhone 14. The project follows the Page Object Model design pattern for test organization and readability.

## Setup

### Prerequisites
- Python installed on your machine
- BrowserStack account
- Install dependencies:
   ```bash
   pip install -r requirements.txt
-  BrowserStack's credentials: credentials are stored as secrets to be taken from GitHub Actions

## Running Tests
### Pull Request Trigger
- Open a pull request (PR) on the repository.
- Or comment ```/run-tests``` in the comments section of the PR to trigger a test execution.
- Wait for the tests to run and check the test results.

### Manual Execution

For manual execution from the local environment we need to change the ```browser_stack_url``` in the ```environment.py``` file with the proper ```browserstack_username``` and ```browserstack_access_key```
    
    behave -D browser=android  # For Android tests
    behave -D browser=ios      # For iOS tests

## Project Structure
The project follows the Page Object Model design pattern for better organization and readability of tests. The structure is as follows:

`features/:` Contains Behave feature files.

`pages/:` Contains Page Object classes representing web pages.

`steps/:` Contains step definitions for Behave tests.

`environment.py:` Configures test environment and BrowserStack settings.