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

        # Job Details Page
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().pim_button).click()
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().pencil_icon).click()
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().job_button).click()

        # Fill details in Job Details
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().job_title).click()
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().select_job_title).click()
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().job_category).click()
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().select_job_category).click()
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().sub_unit).click()
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().select_sub_unit).click()
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().location).click()
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().select_location).click()
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().employment_status).click()
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().select_employment_status).click()

        # Fill details in Employment Contract Details
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().radio_button).click()
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().contract_start_date_input_box).send_keys(Guru_Data().contract_start_date)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().contract_end_date_input_box).send_keys(Guru_Data().contract_end_date)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().save_button).click()
        time.sleep(10)
        print("Successfully fill all details in Job Details Page")