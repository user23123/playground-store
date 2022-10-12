import pytest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@pytest.mark.usefixtures("test_init")
class TestSubmitContactUs():

    @pytest.fixture(scope="function")
    def test_init(self):
        global chrome_driver
        chrome_driver = webdriver.Chrome(
            executable_path="/Users/anaqnx/Documents/Interview/intelligence-insider/project/drivers/chromedriver")
        
        yield
        
        sleep(3)
        chrome_driver.close()
        print("Test passed")

    def test_tc2_submit_contact_us(self):
        logger.info("Open home page")
        chrome_driver.maximize_window()
        chrome_driver.get("https://magento.softwaretestingboard.com")

        logger.info("Wait for logo to be present")
        logo_main_page = "//a[@class='logo']"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, logo_main_page)))

        logger.info("Wait for Contact Us to be present")
        contact_us = "//a[contains(text(), 'Contact Us')]"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, contact_us)))
        contact_us_element = chrome_driver.find_element("xpath", contact_us)
        contact_us_element.click()

        sleep(10)

        logger.info("Verify Contact Us page is displayed")
        contact_us_page = "https://magento.softwaretestingboard.com/contact-us"
        assert chrome_driver.current_url == contact_us_page

        logger.info("Switch to iframe of the form")
        chrome_driver.switch_to.frame(0)

        logger.info("Add information into contact form fields")
        # Contact Name
        contact_name = "//form[@class='jotform-form']//input[@name='q3_name']"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, contact_name)))
        contact_name_element = chrome_driver.find_element("xpath", contact_name)
        contact_name_element.click()
        contact_name_element.send_keys("Catherine Jones")
        # Contact Email
        contact_email = "//form[@class='jotform-form']//input[@name='q4_email']"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, contact_email)))
        contact_email_element = chrome_driver.find_element("xpath", contact_email)
        contact_email_element.click()
        contact_email_element.send_keys("catherine.test+u1@gmail.com")
        # Contact Number
        contact_number = "//form[@class='jotform-form']//input[@name='q5_contactNumber5']"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, contact_number)))
        contact_number_element = chrome_driver.find_element("xpath", contact_number)
        contact_number_element.click()
        contact_number_element.send_keys("+12223334444")
        # Contact Message
        contact_message = "//form[@class='jotform-form']//textarea[@name='q6_message']"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, contact_message)))
        contact_message_element = chrome_driver.find_element("xpath", contact_message)
        contact_message_element.click()
        contact_message_element.send_keys("Hello, my name is Test")

        logger.info("Switch to iframe of ReCaptcha")
        chrome_driver.switch_to.frame(0)

        logger.info("Click on ReCaptcha")
        contact_re_captcha = "//div[@id='rc-anchor-container']//span[@class='recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox']"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, contact_re_captcha)))
        contact_re_captcha_element = chrome_driver.find_element("xpath", contact_re_captcha)
        contact_re_captcha_element.click()

        # logger.info("Switch to iframe of Submit")
        # chrome_driver.switch_to.frame(0)
        # Contact Submit
        # contact_submit = "//button[@id='input_7']"
        # contact_submit = "//button[@class='form-submit-button submit-button jf-form-buttons jsTest-submitField']"
        # contact_submit = "//li[@class='form-line']//button[@class='form-submit-button submit-button jf-form-buttons jsTest-submitField']"
        # contact_submit = "//button[contains(text(), 'Submit')]"
        contact_submit = "//li[@class='form-line']//button[contains(text(), 'Submit')]"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, contact_submit)))
        contact_submit_element = chrome_driver.find_element("xpath", contact_submit)
        contact_submit_element.click()

        logger.info("Switch to iframe of Thank you message box")
        chrome_driver.switch_to.frame(0)

        thank_you_text = "//h1[@class='thankyou-main-text ty-text']"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, thank_you_text)))
        thank_you_text_element = chrome_driver.find_element("xpath", thank_you_text)
        assert thank_you_text_element.is_displayed(), "Element not displayed"
