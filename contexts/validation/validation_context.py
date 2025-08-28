from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.window import WindowTypes
class ValidationContext:
    def __init__(self, driver):
        self.driver = driver
        self.table_id = 'dataTableServices'
        self.target_button = None
        self.target_href = ''
        pass
    def locate_element(self):
        # table = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.ID, self.table_id))
        # )
        # tbody = WebDriverWait(table, 10).until(
        #     EC.presence_of_element_located((By.TAG_NAME, 'tbody'))
        # )
        # trows = WebDriverWait(tbody, 10).until(
        #     EC.presence_of_all_elements_located((By.TAG_NAME, 'tr'))
        # )
        # for index, row in enumerate(trows):
        #     tds = row.find_elements(By.TAG_NAME, 'td')
        #     if button_position == index + 1:
        #         for td in tds:
        #             if td.text=='PRENOTA':
        #                 a = WebDriverWait(td, 10).until(
        #                     EC.presence_of_element_located((By.TAG_NAME, 'a'))
        #                 )   
        #                 WebDriverWait(td, 10).until(
        #                     EC.element_attribute_to_include((By.TAG_NAME, 'a'), "href")
        #                 )
        #                 self.target_href = a.get_attribute("href")
                        
        #                 print(f"Botão encontrado para agendamento {self.target_href.split('/')[3]}")
        #                 return  
        return        
                          
            
    def validate_calendar(self, booking_id):
        self.driver.get(f'https://prenotami.esteri.it/Services/Booking/{booking_id}')
        if 'Booking' in self.driver.current_url:
            print('Agendamento disponível!')
            return True
        else:
            print('Agendamento não disponível')
            return False
            
            
    # def validate_loading(self):
    #     if self.driver.current_url=='https://prenotami.esteri.it/Services':
    #         print(f"Pagina carregada")
    #         return True
    #     elif self.driver.current_url=='https://prenotami.esteri.it/Services/Booking/5662':
    #         component = WebDriverWait(self.driver, 15).until(
    #             EC.presence_of_element_located((By.ID, "BookingForm"))
    #         )
    #         print(f"Pagina carregada")
    #         return True
    #     else:
    #         for attempt in range(5):
    #             try:
    #                 WebDriverWait(self.driver, 15).until(
    #                     EC.presence_of_element_located((By.ID, "BookingForm"))
    #                 )
    #                 print(f"Pagina carregada")
    #                 return True
    #             except:
    #                 print(f"Tentativa {attempt+1}: página não carregou, dando refresh...")
    #                 self.driver.refresh()
    #                 time.sleep(5)
    #         return False
