from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl")
elem = driver.find_element_by_name("q")
elem.send_keys("아이유")
elem.send_keys(Keys.RETURN)

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1
for image in images:
    image.click()
    time.sleep(3)
    imgURL = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
    urllib.request.urlretrieve(imgURL, str(count)+".jpg")
    count = count + 1

# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()