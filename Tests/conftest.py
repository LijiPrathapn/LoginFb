from selenium import webdriver
import pytest

driver= None
@pytest.fixture()
def setup():

    driver=webdriver.Chrome(executable_path="C:\\Users\\lijin\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
    driver.maximize_window()
    return driver

