from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re

pattern = r'\?id=(\d+)&'

# Step0: Initial Webdriver Chrome (keep browser opening after code running completely)
ser = Service(r"C:\Users\Ba Truong Huu\Downloads\chromedriver_win32\chromedriver.exe")      #webdriver path
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
chrome_profile_path = r'C:\User Data'
chrome_option.add_argument('user-data-dir=' + chrome_profile_path)
chrome_option.add_argument('profile-directory=Profile 1')
#-----------------------------------------------------------------

url_post = input('Dán link của bạn vào đây:')
browser = webdriver.Chrome(service=ser,options=chrome_option)
browser.get(url_post)
time.sleep(10)
# Click Share button on browser
# elements_with_href = browser.find_elements(By.XPATH,"//*[@href]")
elements_with_href = browser.find_elements(By.CSS_SELECTOR,"a[href*='facebook'][href*='profile']:not([href*='comment'])")

# Print the href attribute of each element
id_string = []
for element in elements_with_href:
    href = element.get_attribute("href")
    match = re.search(pattern,href)
    if match:
        id_string.append(match.group(1))
print(set(id_string))