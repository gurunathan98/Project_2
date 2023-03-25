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
    
    def test_login(self, boot):
        self.driver.get(Guru_Data().url)
        self.driver.implicitly_wait(10)

        # Login
        self.driver.find_element(by=By.NAME, value=Guru_Locators().username_input_box).send_keys(Guru_Data().username)
        self.driver.find_element(by=By.NAME, value=Guru_Locators().password_input_box).send_keys(Guru_Data().password)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().submit_button).click()
        print("The user is logged in successfully")

        # Contact Details Page
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().pim_button).click()
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().pencil_icon).click()
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().contact_details_button).click()

        # Address
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().street_1_input_box).send_keys(Guru_Data().street_1)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().city_input_box).send_keys(Guru_Data().city)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().state_input_box).send_keys(Guru_Data().state)

        # Select Country
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().country).click()
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().select_country).click()

        # Enter Mobile Number
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().mobile_input_box).send_keys(Guru_Data().mobile)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().save_button).click()
        time.sleep(10)
        print("Successfully fill all details in Contact Details Page")