from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"


ACCOUNT_MAIL = "nadiraziziyah@gmail.com"
ACCOUNT_PASSWORD = "Shermina@123"
PHONE = "+91 9995957505"

CHROMEDRIVER_PATH = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(CHROMEDRIVER_PATH)
driver.get(URL)


sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()


time.sleep(5)

username_input = driver.find_element_by_id("username")
username_input.send_keys(ACCOUNT_MAIL)

password_input = driver.find_element_by_id("password")
password_input.send_keys(ACCOUNT_PASSWORD)
password_input.send_keys(Keys.ENTER)
time.sleep(2)
apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
apply_button.click()

phone_input = driver.find_element_by_class_name("fb-single-line-text__input")
if phone_input.text == "":
    phone_input.send_keys(PHONE)


submit_button = driver.find_element_by_css_selector("footer button")
submit_button.click()

review = driver.find_element_by_xpath('//*[@id="ember373"]')
review.click()

time.sleep(2)
submit_application = driver.find_element_by_xpath('//*[@id="ember383"]')
submit_application.click()

driver.quit()