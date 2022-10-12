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
class TestPurchaseItem():

    @pytest.fixture(scope="function")
    def test_init(self):
        global chrome_driver
        chrome_driver = webdriver.Chrome(
            executable_path="/Users/anaqnx/Documents/Interview/intelligence-insider/project/drivers/chromedriver")
        
        yield
        
        sleep(3)
        chrome_driver.close()
        print("Test passed")

    def test_tc1_purchase_item(self):
        logger.info("Open home page")
        chrome_driver.maximize_window()
        chrome_driver.get("https://magento.softwaretestingboard.com")

        logger.info("Wait for logo to be present")
        logo_main_page = "//a[@class='logo']"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, logo_main_page)))

        logger.info("Wait for search box to be present, type product name into search box")
        search_bar = "//div[@class='control']//..//input[@id='search']"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, search_bar)))

        logger.info("Type \'Breathe-Easy Tank\' to the search bar and hit enter")
        search_bar_element = chrome_driver.find_element("xpath", search_bar)
        search_bar_element.click()
        search_bar_element.send_keys('Breathe-Easy Tank')
        search_bar_element.send_keys(Keys.RETURN)

        logger.info("Verify \'Breathe-Easy Tank\' search results page is displayed")
        breathe_easy_search_pg = "https://magento.softwaretestingboard.com/catalogsearch/result/?q=Breathe-Easy+Tank"
        assert chrome_driver.current_url == breathe_easy_search_pg

        logger.info("Wait for \'Breathe-Easy Tank\' to be present")
        breathe_easy_tank_image = "//img[@class='product-image-photo']//..//img[@alt='Breathe-Easy Tank']"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, breathe_easy_tank_image)))

        logger.info("Click on \'Breathe-Easy Tank\'")
        search_bar_element = chrome_driver.find_element("xpath", breathe_easy_tank_image)
        search_bar_element.click()

        logger.info("Wait for \'Breathe-Easy Tank\' product page title to be present")
        breathe_easy_product_page_title = "//h1[@class='page-title']//..//span[contains(text(),'Breathe-Easy Tank')]"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, breathe_easy_product_page_title)))

        logger.info("Verify \'Breathe-Easy Tank\' product page is displayed")
        breathe_easy_tank_page = "https://magento.softwaretestingboard.com/breathe-easy-tank.html"
        assert chrome_driver.current_url == breathe_easy_tank_page

        logger.info("Wait for size S option to be present")
        size_s = 'option-label-size-143-item-167'
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.ID, size_s)))

        logger.info("Click on Size S")
        size_s_element = chrome_driver.find_element("id", size_s)
        size_s_element.click()

        logger.info("Wait until Size S is selected")
        size_s_selected = "//div[@class='swatch-option text selected']"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, size_s_selected)))

        logger.info("Wait until purple color square present")
        purple_shirt_color = "option-label-color-93-item-57"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.ID, purple_shirt_color)))
    
        logger.info("Click on purple color element")
        purple_shirt_color_element = chrome_driver.find_element("id", purple_shirt_color)
        purple_shirt_color_element.click()

        logger.info("Wait until purple is selected")
        purple_shirt_color_selected = "//div[@class='swatch-option color selected']"
        WebDriverWait(chrome_driver, 30).until(EC.presence_of_element_located((By.XPATH, purple_shirt_color_selected)))

        logger.info("Wait until add to card button present")
        add_to_card_button = "//button[@title='Add to Cart']"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, add_to_card_button)))

        logger.info("Click on add to cart element")
        add_to_card_button_element = chrome_driver.find_element("xpath", add_to_card_button)
        add_to_card_button_element.click()

        logger.info("Wait until one item in the cart is present")
        added_to_cart_1 = "//span[@class='counter qty']//..//span[contains(text(), '1')]" # can be made into a dynamic quantity function
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, added_to_cart_1)))

        logger.info("Click on my cart element to open my cart")
        my_cart = "//a[@class='action showcart']"
        my_cart_element = chrome_driver.find_element("xpath", my_cart)
        my_cart_element.click()

        logger.info("Wait until checkout cart button is present")
        checkout_cart_button = "top-cart-btn-checkout"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.ID, checkout_cart_button)))

        logger.info("Click on checkout cart button")
        checkout_cart_button_element = chrome_driver.find_element("id", checkout_cart_button)
        checkout_cart_button_element.click()

        logger.info("Wait until Shipping Address heading present")
        shipping_address = "//li[@id='shipping']"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, shipping_address)))

        logger.info("Verify Shipping page is displayed")
        shipping_page = "https://magento.softwaretestingboard.com/checkout/#shipping"
        assert chrome_driver.current_url == shipping_page

        logger.info("Verify Shipping page is elements are present, and type checkout user info")
        # Email
        email_input = "//div[@class='control _with-tooltip']//input[@id='customer-email']"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, email_input)))
        email_input_element = chrome_driver.find_element("xpath", email_input)
        email_input_element.send_keys("test22+u2@gmail.com")

        # # Password
        # password_input = "//input[@id='customer-password']"
        # WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, password_input)))
        # password_input_element = chrome_driver.find_element("xpath", password_input)
        # #password_input_element.click()
        # password_input_element.send_keys("BestPassword111*")

        # First name
        first_name_input = "//input[@name='firstname']"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, first_name_input)))
        first_name_input_element = chrome_driver.find_element("xpath", first_name_input)
        first_name_input_element.click()
        first_name_input_element.send_keys("Tom")
        # Last name
        last_name_input = "//input[@name='lastname']"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, last_name_input)))
        last_name_input_element = chrome_driver.find_element("xpath", last_name_input)
        last_name_input_element.click()
        last_name_input_element.send_keys("Jerry")
        # Address
        address_input = "//input[@name='street[0]']"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, address_input)))
        address_input_element = chrome_driver.find_element("xpath", address_input)
        address_input_element.click()
        address_input_element.send_keys("111 1st street")
        # City
        city_input = "//input[@name='city']"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, city_input)))
        city_input_element = chrome_driver.find_element("xpath", city_input)
        city_input_element.click()
        city_input_element.send_keys("Phoenix")
        # State
        state_az_option_dropdown = "//select[@name='region_id']//..//option[@data-title='Arizona']"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, state_az_option_dropdown)))
        state_az_option_dropdown_element = chrome_driver.find_element("xpath", state_az_option_dropdown)
        state_az_option_dropdown_element.click()
        # Zip code
        zip_code = "//input[@name='postcode']"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, zip_code)))
        city_input_element = chrome_driver.find_element("xpath", zip_code)
        city_input_element.click()
        city_input_element.send_keys("11111")
        # Country
        country_option_dropdown = "//select[@name='country_id']//..//option[@data-title='United States']"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, country_option_dropdown)))
        country_option_dropdown_element = chrome_driver.find_element("xpath", country_option_dropdown)
        country_option_dropdown_element.click()
        # Phone number
        phone_number = "//input[@name='telephone']"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, phone_number)))
        phone_number_element = chrome_driver.find_element("xpath", phone_number)
        phone_number_element.click()
        phone_number_element.send_keys("1231231234")
        # Shipping $5
        radio_5 = "//input[@name='ko_unique_1']"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, radio_5)))
        radio_5_element = chrome_driver.find_element("xpath", radio_5)
        radio_5_element.click()
        # Wait till radio 5 is selected
        radio_5_selected = "//input[@value='flatrate_flatrate']"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, radio_5_selected)))
        # Next button
        next_button = "//button[@class='button action continue primary']"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, next_button)))
        next_button_element = chrome_driver.find_element("xpath", next_button)
        next_button_element.click()

        sleep(10)

        logger.info("Verify Payment page is displayed")
        payment_page = "https://magento.softwaretestingboard.com/checkout/#payment"
        assert chrome_driver.current_url == payment_page

        # Place order button
        place_order_button = "//button[@class='action primary checkout']"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, place_order_button)))
        place_order_button_element = chrome_driver.find_element("xpath", place_order_button)
        place_order_button_element.click()

        sleep(10)

        logger.info("Verify Thank you page is displayed")
        thank_you_page = "https://magento.softwaretestingboard.com/checkout/onepage/success/"
        assert chrome_driver.current_url == thank_you_page

        logger.info("Verify Thank you heading is displayed")
        thank_you_heading = "//span[contains(text(), 'Thank you for your purchase!')]"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, thank_you_heading)))
        thank_you_heading_element = chrome_driver.find_element("xpath", thank_you_heading)
        assert thank_you_heading_element.is_displayed(), "Element not displayed"

        logger.info("Verify Continue Shopping is displayed")
        continue_shopping_button = "//span[contains(text(), 'Continue Shopping')]"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, continue_shopping_button)))
        continue_shopping_button_element = chrome_driver.find_element("xpath", continue_shopping_button)
        assert continue_shopping_button_element.is_displayed(), "Element not displayed"
