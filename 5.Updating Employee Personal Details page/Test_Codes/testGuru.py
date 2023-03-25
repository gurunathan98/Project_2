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

        # Personal Details Page
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().pim_button).click()
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().pencil_icon).click()
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().nickname_input_box).send_keys(Guru_Data().nickname)
        
        # Select Nationality
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().nationality_box).click()
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().select_nationality).click()

        # Select Marital Status
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().marital_status_box).click()
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().select_marital_status).click()

        # Click Gender
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().gender_radio_button).click()

        # Fill Military Service Box
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().military_service_input_box).send_keys(Guru_Data().military_service)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().save_button).click()
        
        # Select Blood Group
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().blood_group_box).click()
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().select_blood_group).click()
        time.sleep(10)
        print("Successfully fill all details in Personal Details Page")
