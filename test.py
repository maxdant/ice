from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def test_sign_up_full_flow():
    driver_location = './drivers/geckodriver'
    browser = webdriver.Firefox(executable_path=driver_location)

    # check the quotation flow
    #
    # 1) open the page https://acc-interconnect.icepay.com/portal
    #     assert something about the page
    browser.get('https://acc-interconnect.icepay.com/portal')
    browser.maximize_window()

    try:
        login_button = browser.find_element(By.ID, 'btn-login')
        assert login_button.text == 'Login'
    except NoSuchElementException:
        print('Login button is not present')

    # 2) click Sign Up and assert the browser is on the right page and tab
    try:
        signup_link = browser.find_element(By.LINK_TEXT, 'Sign Up now!')
        assert signup_link.text == 'Sign Up now!'
        signup_link.click()

        browser.switch_to.window(browser.window_handles[1])

        signup_button = browser.find_element(By.NAME, 'button')
        assert signup_button.text == 'Sign Up'
        assert browser.current_url == 'https://acc-interconnect.icepay.com/portal/sign-up'

    except NoSuchElementException:
        print('Sign up link is not present')


    # 3. Fill the form and click Sign Up
    try:
        browser.find_element(By.NAME, 'email').send_keys('email@email.com')
        browser.find_element(By.NAME, 'companyName').send_keys('my company')
        browser.find_element(By.NAME, 'name').send_keys('nome')
        browser.find_element(By.NAME, 'prefix').send_keys('p')
        browser.find_element(By.NAME, 'surname').send_keys('cognome')

    except NoSuchElementException:
        print('A field in the Sign Up page is not present')
    # signup_button.click()

    # 4. Wait for email from ICEPAY. Hint: You might use some open source email api

    # 5. Open email, click Create Your User button or navigate (href)

    # 6. Input password and click Sign Up

    # 7. Go to ICEPAY portal https://acc-interconnect.icepay.com/portal

    # 8. Login using email and password

    browser.close()
