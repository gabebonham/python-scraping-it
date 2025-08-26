from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class AuthContext:
    def __init__(self, driver, email, password):
        self.driver = driver
        self.login_button_x_path = '//*[@id="login-form"]/button'
        self.email_id = "login-email"
        self.password_id = "login-password"
        self.form_id = 'login-form'
        self.email = email
        self.password = password
        pass
    def login(self):
        email_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.email_id))
        )
        password_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.password_id))
        )
        form = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.form_id))
        )
        email_box.send_keys(self.email)
        password_box.send_keys(self.password)
        email_box.send_keys(Keys.ENTER)
        time.sleep(5)