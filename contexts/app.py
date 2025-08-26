import undetected_chromedriver as uc
import os
from dotenv import load_dotenv
from contexts.auth.auth_context import AuthContext
class App:
    def __init__(self):
        self.email = ''
        self.password = ''
        self.driver = None
        self.row_position = 1
        self.configure()
        pass
    def configure(self):
        load_dotenv()
        self.email = os.getenv('EMAIL')
        self.password = os.getenv('PASSWORD')
        self.row_position = int(os.getenv('ROW_POSITION'))
        options = uc.ChromeOptions()
        options.add_argument('--incognito')
        options.binary_location = "/usr/bin/google-chrome"
        self.driver = uc.Chrome(use_subprocess=True, user_data_dir=None, options=options)
        self.driver.set_page_load_timeout(30)