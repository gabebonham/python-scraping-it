from contexts.auth.auth_context import AuthContext
from contexts.validation.validation_context import ValidationContext
from contexts.app import App
import time
from contexts.notify.notify_context import Notify
import asyncio
from utils.exceptions.login_exception import LoginException 
async def execute():
    app = App()
    auth = AuthContext(driver=app.driver,email=app.email,password=app.password)
    validation = ValidationContext(driver=app.driver)
    notify = Notify()
    is_free = False
    app.driver.get("https://prenotami.esteri.it")
    try:
        print(f'Executando login')
        auth.login()
    except LoginException as le:
        print(f'Erro ao executar login: {e}')
        await notify.send_notification_error_auth(e)
        raise le
    except Exception as e:
        print(f'Erro ao executar login: {e}')
        await notify.send_notification_error_execution(e)
        app.driver.quit()
        raise e
        
    while not is_free:
        try:
            app.driver.get("https://prenotami.esteri.it/Services")
            validation.locate_element()
            is_free = validation.validate_calendar(app.booking_id)
            time.sleep(60*app.period)
        except LoginException as le:
            print(f'Erro de auth: {e}')
            await notify.send_notification_error_auth(e)
            raise le
        except Exception as e:
            print(f'Erro ao validar data: {e}')
            await notify.send_notification_error_execution(e)
            app.driver.quit()
            raise e
    await notify.send_notification_found('https://prenotami.esteri.it')
    input('Aperte ENTER para fechar o programa:')
    return is_free
async def run():
    error_counter = 0
    login_error_counter = 0
    is_done = False
    while error_counter < 3 and not is_done:
        try:
            is_done = await execute()
        except LoginException as le:
            print(f'Erro de auth: {le}')
            
            login_error_counter = login_error_counter + 1
            print(f'Contador de erro de login: {login_error_counter}')
            if login_error_counter >= 3:
                print(f'Pausando execução')
                time.sleep(60*30)
                login_error_counter = 0
                error_counter = error_counter + 1
        except Exception as e:
            error_counter = error_counter + 1
            print(f'Erro ao executar loop  externo: {e}')
            print(f'Número de erros: {error_counter} | Número máximo de erros: 3')
    print('Parando execução...')



if __name__ == "__main__":
    asyncio.run(run())