from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class ValidationContext:
    def __init__(self, driver):
        self.driver = driver
        self.table_id = 'dataTableServices'
        self.target_button = None
        self.target_href = ''
        pass
    def locate_element(self, button_position):
        table = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.table_id))
        )
        tbody = WebDriverWait(table, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'tbody'))
        )
        trows = WebDriverWait(tbody, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, 'tr'))
        )
        for index, row in enumerate(trows):
            tds = row.find_elements(By.TAG_NAME, 'td')
            if button_position == index + 1:
                for td in tds:
                    if td.text=='PRENOTA':
                        a = WebDriverWait(td, 10).until(
                            EC.presence_of_element_located((By.TAG_NAME, 'a'))
                        )   
                        self.target_href = a.get_dom_attribute('href')
                        print(f'Botão encontrado para agendamendo {self.target_href.split('/')[3]}')
                        return
            
    def validate_calendar(self):
        # self.target_button.click()
        self.driver.get(f'https://prenotami.esteri.it{self.target_href}')
        time.sleep(4)
        if 'Booking' in self.driver.current_url:
            print('Agendamento disponível!')
            return True
        else:
            print('Agendamento não disponível')
            return False
            
