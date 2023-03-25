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

        # Search Admin
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Guru_Data().search_placeholder_1)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)

        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Guru_Data().search_placeholder_2)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)

        # Search PIM
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Guru_Data().search_placeholder_3)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)
        
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Guru_Data().search_placeholder_4)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)

        # Search Leave
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Guru_Data().search_placeholder_5)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)

        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Guru_Data().search_placeholder_6)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)

        # Search Time
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Guru_Data().search_placeholder_7)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)

        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Guru_Data().search_placeholder_8)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)

        # Search Recruitment
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Guru_Data().search_placeholder_9)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)

        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Guru_Data().search_placeholder_10)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)

        # Search My Info
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Guru_Data().search_placeholder_11)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)

        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Guru_Data().search_placeholder_12)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)

        # Search Performance
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Guru_Data().search_placeholder_13)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)

        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Guru_Data().search_placeholder_14)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)

        # Search Dashboard
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Guru_Data().search_placeholder_15)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)

        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Guru_Data().search_placeholder_16)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)

        # Search Directory
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Guru_Data().search_placeholder_17)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)

        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Guru_Data().search_placeholder_18)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)

        # Search Maintenance
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Guru_Data().search_placeholder_19)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)

        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Guru_Data().search_placeholder_20)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)

        # Search Buzz
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Guru_Data().search_placeholder_21)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)

        self.driver.find_element(by=By.XPATH, value=Guru_Locators().search_input_box).send_keys(Guru_Data().search_placeholder_22)
        time.sleep(5)
        print("User should be able to search the Admin, PIM, Leave, Time, Recruitment, My Info, Performance, Dashboard, Directory, Maintenance & Buzz in both lower & upper case should be displayed under search text box")