import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestStoreCart(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_store_cart_transaction(self):
		driver = self.driver
		#store landing page.
		driver.get("https://store.23andme.com/en-us/cart/")
		print (driver.current_url)
		
		#store landing page verification. 
		assert "23andMe" in driver.title
		
		#add first kit.
		driver.find_element_by_xpath("//*[.='Add a kit.']").click()
		
		#add addtional kits.  
		for x in range(0,4):
			driver.find_element_by_css_selector(".add-remove-kits .js-add-kit").click()
		name_input_list = driver.find_elements_by_css_selector(".kit-list .js-kit-name")
		
		#give kits unique name. 
		count = 0
		for name_input in name_input_list:
			name_input.send_keys("Test%s" %count)
			count += 1
		
		#using sleep for now, but it works. refactor using wait.
		time.sleep(5) 
		driver.find_element_by_xpath("//input[contains(@value,'continue')]").click()

		#shipping address form.
		time.sleep(5)
		assert "23andMe" in driver.title
		print (driver.current_url)
		driver.find_element_by_xpath("//input[@id='id_first_name']").send_keys("Todd")
		driver.find_element_by_xpath("//input[@id='id_last_name']").send_keys("Mellors")
		driver.find_element_by_xpath("//input[@id='id_company']").send_keys("12andMe")
		driver.find_element_by_xpath("//input[@id='id_address']").send_keys("6571 Northridge Dr.")
		driver.find_element_by_xpath("//input[@id='id_address2']").send_keys("House")
		driver.find_element_by_xpath("//input[@id='id_city']").send_keys("San Jose")
		driver.find_element_by_xpath("//select[@id='id_state']").send_keys("California")
		driver.find_element_by_xpath("//input[@id='id_postal_code']").send_keys("95120")
		driver.find_element_by_xpath("//select[@id='id_country']")
		driver.find_element_by_xpath("//input[@id='id_email']").send_keys("trmellors@gmail.com")
		driver.find_element_by_xpath("//input[@id='id_int_phone']").send_keys("1 510-909-8774")
		driver.find_element_by_xpath("//input[@id='id_add_gift']").click()
		driver.find_element_by_xpath("//textarea[@id='id_gift_message']").send_keys("gift message gift message gift message gift message gift message gift message gift message gift message gift message gift message gift message gift message gift message gift message gift message gift message gift message gift message gift m")
		driver.find_element_by_xpath("//input[@class='submit button-continue']").click()

		#verify address page. using sleep for now, but it works. refactor using wait.
		time.sleep(5)
		assert "23andMe" in driver.title
		print (driver.current_url)
		driver.find_element_by_xpath("//input[@value='ship to verified address']").click()
		print (driver.current_url)

	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()