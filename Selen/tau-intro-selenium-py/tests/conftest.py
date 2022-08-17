
import json
import pytest
import selenium.webdriver

# Usando el JSON sin quemar, la forma recomendada


@pytest.fixture
def config(scope='session'):
    # Lee el JSON
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Se asegura que los valores son aceptables
    assert config['browser'] in ['Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Retorna config para su uso
    return config


@pytest.fixture
def browser(config):
    # inicializar la instancia del WebDriver
    if config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        #opts = selenium.webdriver.ChromeOptions()
        # opts.add_argument('headless')
        opts = selenium.webdriver.ChromeOptions.add_argument('--log-level=1')
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser"{config["browser"]} is not supported')

    # Crear espera implicita
    b.implicitly_wait(config['implicit_wait'])

    # Retornar la instancia del WebDriver para el SetUp
    yield b

    # Cerrar para la limpieza
    b.quit()


# Quemado el browser en el codigo, funciona pero no se recomienda
# @pytest.fixture  # Este decorador indica que esta función particular es un fixture
# def browser():
#
#    # Initialize chromedriver instance
#    chromeWebDriver = selenium.webdriver.Chrome()
#
#    # Waits for elements to appear for up to 10 seconds
#    chromeWebDriver.implicitly_wait(10)
#
#    # Return the WebDriver instance for the setup
#    yield chromeWebDriver
#
#    # Quit the instance for the cleanup
#    chromeWebDriver.quit()
#
