# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# import time

# desired_cap = {
# 'browser': 'Chrome',
# 'browser_version': '84.0 beta',
# 'os': 'OS X',
# 'os_version': 'Catalina',
# 'resolution': '1024x768',
# 'name': 'Bstack-[Python] Sample Test'
# }

# driver = webdriver.Remote(
# 	command_executor ='https://adityaguptagkp_q3YXAS:yorhvfmrsjhFoz8qd7z5@hub-cloud.browserstack.com/wd/hub',
# 	desired_capabilities = desired_cap)
# driver.get('https://forms.gle/zX5NEumdXW4Z7SrC6')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
desired_cap = {
 'os_version': 'Catalina',
 'resolution': '1920x1080',
 'browser': 'Chrome',
 'browser_version': '84.0',
 'os': 'OS X',
 'name': 'BStack-[Python] Sample Test', # test name
 'build': 'BStack Build Number 1' # CI/CD job or build name
}
driver = webdriver.Remote(
    command_executor='https://adityaguptagkp_q3YXAS:yorhvfmrsjhFoz8qd7z5@hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=desired_cap)
driver.get("https://www.google.com")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
elem = driver.find_element_by_name("q")
elem.send_keys("BrowserStack")
elem.submit()
try:
    WebDriverWait(driver, 5).until(EC.title_contains("BrowserStack"))
    # Setting the status of test as 'passed' or 'failed' based on the condition; if title of the web page starts with 'BrowserStack'
    driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched!"}}')
except TimeoutException:
    driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title not matched"}}')
print(driver.title)
driver.quit() 