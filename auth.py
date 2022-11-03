from json import dumps
from tda import auth
import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# Function to write token to object in client
def token_write_func(token, refresh_token=None):
    global TOKEN_OBJECT
    TOKEN_OBJECT = token


# Authenticate using TDA-API and Chrome via Selenium/Chromedriver and return as JSON
def auth_service(api_key):
    s = Service(config.chromedriver_path)
    with webdriver.Chrome(service=s) as driver:
        c = auth.client_from_login_flow(
            driver, api_key, config.redirect_url, config.root, token_write_func=token_write_func)

    return dumps(TOKEN_OBJECT)
