import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# wip
class TestStoreCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_store_cart_transaction(self):
        driver = self.driver

        # store landing page
        driver.get("https://store.23andme.com/en-us/cart/")
        self.assertEqual(driver.current_url,
                         "https://store.23andme.com/en-us/cart/")
        print(driver.current_url)

        # add first kit
        driver.find_element_by_link_text("Add a kit.").click()

        # add addtional kits
        WebDriverWait(driver, 12).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".add-remove-kits .js-add-kit")))
        for x in range(0, 4):
            driver.find_element_by_css_selector(
                ".add-remove-kits .js-add-kit").click()
        name_input_list = driver.find_elements_by_css_selector(
            ".kit-list .js-kit-name")

        # give kits unique name
        count = 0
        for name_input in name_input_list:
            name_input.send_keys("Test%s" % count)
            count += 1
        time.sleep(5)
        driver.find_element_by_xpath(
            "//input[@class='submit button-continue']").click()

        # Address form
        time.sleep(5)
        self.assertEqual(driver.current_url,
                         "https://store.23andme.com/en-us/shipping/")
        print(driver.current_url)
        driver.find_element_by_name("first_name").send_keys("Sandy")
        driver.find_element_by_name("last_name").send_keys("Thomson")
        driver.find_element_by_name("company").send_keys("self")
        driver.find_element_by_name("address").send_keys("6573 Northridge Dr.")
        driver.find_element_by_name("address2").send_keys("House")
        driver.find_element_by_name("city").send_keys("San Jose")
        driver.find_element_by_name("state").send_keys("California")
        driver.find_element_by_name("postal_code").send_keys("95120")
        driver.find_element_by_name("country")
        driver.find_element_by_name("email").send_keys("sthomson@netscape.net")
        driver.find_element_by_id("id_int_phone").send_keys("1 408-268-0001")
        driver.find_element_by_name("add_gift").click()
        driver.find_element_by_name("gift_message").send_keys(
            "gift message gift message gift message gift message gift message gift")                
        driver.find_element_by_xpath("//input[@class='submit button-continue']").click()

        # verify address page.
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='ship to verified address']")))
        self.assertEqual(driver.current_url,
                         "https://store.23andme.com/en-us/verifyaddress/")
        print(driver.current_url)
        driver.find_element_by_xpath(
            "//input[@value='ship to verified address']").click()
        
        # lands on payment page.
        self.assertEqual(driver.current_url,
                         "https://store.23andme.com/en-us/payment/")
        print(driver.current_url)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
