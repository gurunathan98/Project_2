# Use Pytest using Page Object Model

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from Test_Data.data import Guru_Data
from Test_Locators.locators import Guru_Locators
import pytest
import time

class Test_Guru:

    # Booting method for running the Pytest test cases
    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        yield
    
    # Login
    def test_login(self, boot):
        self.driver.get(Guru_Data().url)
        self.driver.implicitly_wait(10)

        # Login
        self.driver.find_element(by=By.NAME, value=Guru_Locators().username_input_box).send_keys(Guru_Data().username)
        self.driver.find_element(by=By.NAME, value=Guru_Locators().password_input_box).send_keys(Guru_Data().password)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().submit_button).click()
        print("The user is logged in successfully")

        # Create New Employee 
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().pim_button).click()
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().add_button).click()

        # Employee Details
        self.driver.find_element(by=By.NAME, value=Guru_Locators().first_name_input_box).send_keys(Guru_Data().first_name)
        self.driver.find_element(by=By.NAME, value=Guru_Locators().middle_name_input_box).send_keys(Guru_Data().middle_name)
        self.driver.find_element(by=By.NAME, value=Guru_Locators().last_name_input_box).send_keys(Guru_Data().last_name)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().employee_id_input_box).send_keys(Guru_Data().employee_id)

        # Create Login Details
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().radio_button).click()
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().username_1_input_box).send_keys(Guru_Data().username_1)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().password_1_input_box).send_keys(Guru_Data().password_1)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().conform_password_input_box).send_keys(Guru_Data().conform_password)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().save_button).click()
        time.sleep(10)
        print("Successfully create new employee in PIM page")