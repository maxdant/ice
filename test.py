from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import pytest
from pages.loginPage import *
from pages.signupPage import *


@pytest.fixture(scope="class")
def firefox_init(request):
    driver_location = './drivers/geckodriver'
    firefox_driver = webdriver.Firefox(executable_path=driver_location)
    request.cls.driver = firefox_driver
    yield
    firefox_driver.quit()


@pytest.mark.usefixtures("firefox_init")
class BasicTest:
    pass


class TestSignUpFlow(BasicTest):
    timeout_wait_for_element = 10

    def open_log_in_page(self, browser):
        browser.get(login_page_url)

        browser.maximize_window()

        try:
            login_button = browser.find_element(By.ID, login_button_id)
            assert login_button.text == login_button_text
        except NoSuchElementException:
            print('Login button is not present')

    def open_sign_up_page(self, browser):
        try:
            sign_up_link = browser.find_element(By.LINK_TEXT, signup_link_text)
            assert sign_up_link.text == signup_link_text
        except NoSuchElementException:
            print('Sign up link is not present')

        sign_up_link.click()

        browser.switch_to.window(browser.window_handles[1])

        wait = WebDriverWait(browser, self.timeout_wait_for_element)
        wait.until(ec.visibility_of_element_located((By.NAME, email_textbox_name)))

        assert browser.current_url == signup_page_url

    def fill_signup_page_fields_and_signup(self, browser):
        try:
            browser.find_element(By.NAME, email_textbox_name).send_keys('email@email.com')
            browser.find_element(By.NAME, company_textbox_name).send_keys('My company' + str(time.time()))
            browser.find_element(By.NAME, name_textbox_name).send_keys('Nome')
            browser.find_element(By.NAME, prefix_textbox_name).send_keys('p')
            browser.find_element(By.NAME, surname_textbox_name).send_keys('Cognome')

        except NoSuchElementException:
            print('A field in the Sign Up page is not present')

        try:
            browser.find_element(By.NAME, signup_button_name).click()
        except NoSuchElementException:
            print('The Sign Up button is not present')

        wait = WebDriverWait(browser, self.timeout_wait_for_element)
        wait.until(ec.visibility_of_element_located((By.CLASS_NAME, alert_successful_signup_class_name)))

        alert_successful_registration = browser.find_element(By.CLASS_NAME, alert_successful_signup_class_name)
        assert alert_successful_registration.text == alert_successful_signup_text

    def test_signup_flow(self):
        browser = self.driver
        self.open_log_in_page(browser)
        self.open_sign_up_page(browser)
        self.fill_signup_page_fields_and_signup(browser)



        # Missing steps

        # 4. Wait for email from ICEPAY. Hint: You might use some open source email api

        #trashspam.com can be a good one to use, simple GET on an email address and emails are in a JSON file

        # 5. Open email, click Create Your User button or navigate (href)

        # 6. Input password and click Sign Up

        # 7. Go to ICEPAY portal https://acc-interconnect.icepay.com/portal

        # 8. Login using email and password
