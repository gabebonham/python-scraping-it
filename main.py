from contexts.auth.auth_context import AuthContext
from contexts.validation.validation_context import ValidationContext
from contexts.app import App
import time
def execute():
    app = App()
    auth = AuthContext(driver=app.driver,email=app.email,password=app.password)
    validation = ValidationContext(driver=app.driver)
    is_free = False
    app.driver.get("https://prenotami.esteri.it")
    try:
        print(f'Executando login')
        auth.login()
    except Exception as e:
        print(f'Erro ao executar login: {e}')
        app.driver.quit()
        raise e
    while not is_free:
        try:
            app.driver.get("https://prenotami.esteri.it/Services")
            validation.locate_element(button_position=app.row_position)
            is_free = validation.validate_calendar()
            time.sleep(5)
        except Exception as e:
            print(f'Erro ao validar data: {e}')
            app.driver.quit()
            raise e
    print('Notificar')
    app.driver.quit()
def run():
    error_counter = 0
    while error_counter < 3:
        try:
            execute()
        except Exception as e:
            error_counter = error_counter + 1
            print(f'Erro ao executar loop  externo: {e}')
            print(f'Número de erros: {error_counter} | Número máximo de erros: 3')
   
run()
# todo validacao de sessao login
# todo notify section