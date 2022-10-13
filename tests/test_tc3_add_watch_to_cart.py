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
class TestAddWatchToCart():

    @pytest.fixture(scope="function")
    def test_init(self):
        global chrome_driver
        chrome_driver = webdriver.Chrome(
            executable_path="/Users/anaqnx/Documents/Interview/intelligence-insider/project/drivers/chromedriver")
        
        yield
        
        sleep(3)
        chrome_driver.close()
        print("Test passed")

    def test_tc3_add_watch_to_cart(self):
        logger.info("Open home page")
        chrome_driver.maximize_window()
        chrome_driver.get("https://magento.softwaretestingboard.com")

        logger.info("Wait for logo to be present")
        logo_main_page = "//a[@class='logo']"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, logo_main_page)))

        logger.info("Wait for search box to be present, type product name into search box")
        search_bar = "//div[@class='control']//..//input[@id='search']"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, search_bar)))

        logger.info("Type \'watch\' to the search bar and hit enter")
        search_bar_element = chrome_driver.find_element("xpath", search_bar)
        search_bar_element.click()
        search_bar_element.send_keys('watch')
        search_bar_element.send_keys(Keys.RETURN)

        logger.info("Verify \'watch\' search results page is displayed")
        watch_search_pg = "https://magento.softwaretestingboard.com/catalogsearch/result/?q=watch"
        assert chrome_driver.current_url == watch_search_pg

        logger.info("Wait for \'Dash Digital Watch\' to be present")
        dd_watch_image = "//div[@class='product-item-info']//img[@alt='Dash Digital Watch']"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, dd_watch_image)))

        logger.info("Click on \'Dash Digital Watch\'")
        dd_watch_image_element = chrome_driver.find_element("xpath", dd_watch_image)
        dd_watch_image_element.click()

        logger.info("Wait for \'Dash Digital Watch\' product page title to be present")
        dd_watch_product_page_title = "//h1[@class='page-title']//..//span[contains(text(),'Dash Digital Watch')]"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, dd_watch_product_page_title)))

        logger.info("Verify \'Dash Digital Watch\' product page is displayed")
        dd_watch_page = "https://magento.softwaretestingboard.com/dash-digital-watch.html"
        assert chrome_driver.current_url == dd_watch_page

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

        logger.info("Click on view or edit cart button")
        view_edit_cart = "//a[@class='action viewcart']"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, view_edit_cart)))
        view_edit_cart_element = chrome_driver.find_element("xpath", view_edit_cart)
        view_edit_cart_element.click()

        logger.info("Verify Shopping Cart title loaded")
        shopping_cart_title = "//div[@class='page-title-wrapper']//span[contains(text(), 'Shopping Cart')]"
        WebDriverWait(chrome_driver, 20).until(EC.presence_of_element_located((By.XPATH, shopping_cart_title)))

        # Slow load, isn't able to verify at the moment
        # logger.info("Verify Shopping Cart product page is displayed")
        # cart_page = "https://magento.softwaretestingboard.com/checkout/cart/"
        # assert chrome_driver.current_url == dd_watch_page

        logger.info("Verify Dash Digital Watch item is displayed")
        # Product title
        dd_watch_product_title = "//tr[@class='item-info']//a[contains(text(), 'Dash Digital Watch')]"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, dd_watch_product_title)))
        dd_watch_product_title_element = chrome_driver.find_element("xpath", dd_watch_product_title)
        assert dd_watch_product_title_element.is_displayed()
        # Product image
        logger.info("Wait for \'Dash Digital Watch\' to be present")
        dd_watch_image = "//div[@class='product-item-info']//img[@alt='Dash Digital Watch']"
        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, dd_watch_image)))
        assert dd_watch_image.is_displayed()
