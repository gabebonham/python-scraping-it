import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv

load_dotenv() 
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')
login_button_x_path = '//*[@id="login-form"]/button'
services_button_x_path = '//*[@id="advanced"]'

options = uc.ChromeOptions()
options.binary_location = "/usr/bin/google-chrome"
driver = uc.Chrome(options=options)

driver.get("https://prenotami.esteri.it")

# Wait up to 10 seconds for the element to be present
email_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "login-email"))
)
password_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "login-password"))
)
form = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'login-form'))
)
login_button = form.find_element(By.TAG_NAME, 'button')

email_box.send_keys(email)
password_box.send_keys(password)
email_box.send_keys(Keys.ENTER)
time.sleep(5)
# Navigate to Services
driver.get("https://prenotami.esteri.it/Services")

# Wait for the table
table_id = 'dataTableServices'
table = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, table_id))
)

# Wait for tbody inside table
tbody = WebDriverWait(table, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, 'tbody'))
)
# Get all rows
trows = WebDriverWait(tbody, 10).until(
    EC.presence_of_all_elements_located((By.TAG_NAME, 'tr'))
)
# Iterate through rows and get cells
for row in trows:
    tds = row.find_elements(By.TAG_NAME, 'td')
    print([td.text for td in tds])

driver.quit()
