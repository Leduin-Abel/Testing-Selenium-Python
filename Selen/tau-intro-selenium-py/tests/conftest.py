import pytest
import selenium.webdriver


@pytest.fixture  # Este decorador indica que esta función particular es un fixture
def browser():

    # Initialize chromedriver instance
    chromeWebDriver = selenium.webdriver.Chrome()

    # Waits for elements to appear for up to 10 seconds
    chromeWebDriver.implicitly_wait(10)

    # Return the WebDriver instance for the setup
    yield chromeWebDriver

    # Quit the instance for the cleanup
    chromeWebDriver.quit
