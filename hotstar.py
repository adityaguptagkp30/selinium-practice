from selenium import webdriver
import time
#locating the driver
driver=webdriver.Chrome("/Users/appinventiv/Downloads/chromedriver")

#website to load
driver.get("https://www.hotstar.com/in")
# driver.implicitly_wait(5) 
time.sleep(3)


# driver.maximize_window()

# driver.find_elements_by_id("searchField").send_keys("Movies")

driver.get("https://www.google.com")
# driver.find_element_by_name("q").send_keys("selenium")
# driver.find_element_by_name("btnK").click()


# driver.find_element_by_link_text("Premium").click()


# driver.find_elements_by_css_selector("searchField").send_keys("Sports")
# driver.find_element_by_partial_link_text("Premi").click()
# driver.find_element_by_xpath("//div[contains(text(),'LOGIN')]").click()
# driver.find_element_by_xpath("//input[@id='phoneNo']").click()

