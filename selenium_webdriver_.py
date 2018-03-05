"""
doc string
"""

import time
from selenium import webdriver

# Optional argument, if not specified will search path.
DRIVER = webdriver.Chrome('chromedriver.exe')
DRIVER.get('http://www.google.com/ncr')

time.sleep(5) # Let the user actually see something!

SEARCH_BOX = DRIVER.find_element_by_name('q')
SEARCH_BOX.send_keys('ChromeDriver')
SEARCH_BOX.submit()

time.sleep(5) # Let the user actually see something!
DRIVER.quit()
