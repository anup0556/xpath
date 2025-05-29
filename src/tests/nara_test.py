# File: /nara-automation-testing/nara-automation-testing/src/tests/nara_test.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

class NaraAutomationTest:
    def __init__(self):
        self.driver = webdriver.Chrome()  # Ensure you have the ChromeDriver installed and in your PATH

    def setup(self):
        self.driver.get("https://www.makemytrip.com/")
        self.driver.maximize_window()

    def login(self, username, password):
        self.driver.find_element(By.XPATH, "//input[@name='username' and @type='text']").send_keys(username)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name='password' and @type='password']").send_keys(password)
        time.sleep(2)  # Wait for the password field to be filled
        self.driver.find_element(By.XPATH, "//button[@name='submitButton' or @type='submit']").click()
        time.sleep(2)  # Wait for login to complete
        
    # def search_flights(self, from_city, to_city, date):
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH, "//input[@id='toCity']").click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, "//input[@aria-controls='react-autowhatever-1']").send_keys("ind")
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, "//span[contains(text(),'IND')]").click()
    #     time.sleep(2)

    def search_flights(self, from_city, to_city, date):
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@id='fromCity']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@aria-autocomplete='list']").send_keys("del")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[text()='DEL']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='toCity']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@aria-controls='react-autowhatever-1']").send_keys("ind")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[contains(text(),'IND')]").click()
        time.sleep(2)
        
        
    # def register_user(self, username, email, password):
    #     self.driver.find_element(By.LINK_TEXT, "Register").click()
    #     self.driver.find_element(By.NAME, "username").send_keys(username)
    #     self.driver.find_element(By.NAME, "email").send_keys(email)
    #     self.driver.find_element(By.NAME, "password").send_keys(password)
    #     self.driver.find_element(By.NAME, "submit").click()

    # def check_homepage_images(self):
    #     images = self.driver.find_elements(By.TAG_NAME, "img")
    #     for img in images:
    #         assert img.is_displayed(), "Image not displayed"

    # def navigate_to_services(self):
    #     self.driver.find_element(By.LINK_TEXT, "Services").click()

    # def check_contact_faqs(self):
    #     self.driver.find_element(By.LINK_TEXT, "Contact").click()
    #     faqs = self.driver.find_elements(By.CLASS_NAME, "faq")
    #     for faq in faqs:
    #         assert faq.is_displayed(), "FAQ not displayed"

    # def interact_with_chat(self):
    #     chat_button = self.driver.find_element(By.ID, "chat-button")
    #     chat_button.click()
    #     time.sleep(2)  # Wait for chat to load
    #     chat_input = self.driver.find_element(By.ID, "chat-input")
    #     chat_input.send_keys("Hello")
    #     chat_input.send_keys(Keys.RETURN)

    # def verify_images_section(self):
    #     self.driver.find_element(By.LINK_TEXT, "Images").click()
    #     images = self.driver.find_elements(By.TAG_NAME, "img")
    #     for img in images:
    #         assert img.is_displayed(), "Image not displayed in images section"

    def teardown(self):
        self.driver.quit()

if __name__ == "__main__":
    test = NaraAutomationTest()
    test.setup()
    # test.login("testuser", "testpassword")
    test.search_flights("IND", "DEL", "2023-10-01")
    # test.check_homepage_images()
    # test.navigate_to_services()
    # test.check_contact_faqs()
    # test.interact_with_chat()
    # test.verify_images_section()
    test.teardown()
    # python nara_test.py

os.chdir(r"c:\Users\anup0\Downloads\nara-automation-testing\src\tests")