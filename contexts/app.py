import undetected_chromedriver as uc
import os
from dotenv import load_dotenv
from contexts.auth.auth_context import AuthContext
class App:
    def __init__(self):
        self.email = ''
        self.password = ''
        self.driver = None
        self.booking_id = None
        self.period = None
        self.configure()
        pass
    def configure(self):
        load_dotenv()
        self.email = os.getenv('EMAIL')
        self.password = os.getenv('PASSWORD')
        self.booking_id = int(os.getenv('BOOKING_ID'))
        self.period = int(os.getenv('PERIOD_MIN'))
        options = uc.ChromeOptions()
        options.add_argument('--incognito')
        options.binary_location = "/usr/bin/google-chrome"
        self.driver = uc.Chrome(use_subprocess=True, user_data_dir=None, options=options)
        self.driver.set_page_load_timeout(60)
    def need_login(self):
        return 'ReturnUrl' in self.driver.current_url
    def is_error(self):
        return 'Error' in self.driver.current_url