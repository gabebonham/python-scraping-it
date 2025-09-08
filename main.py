from contexts.auth.auth_context import AuthContext
from contexts.validation.validation_context import ValidationContext
from contexts.app import App
import time
from contexts.notify.notify_context import Notify
import asyncio
from utils.exceptions.login_exception import LoginException 
from utils.logger import setup_logger 
async def execute():
    app = App()
    auth = AuthContext(driver=app.driver,email=app.email,password=app.password)
    validation = ValidationContext(driver=app.driver)
    notify = Notify()
    log = setup_logger()
    is_free = False
    app.driver.get("https://prenotami.esteri.it")
    try:
        log.info(f'Executando login')
        auth.login()
    except LoginException as le:
        log.error(f'Erro ao executar login: {e}')
        await notify.send_notification_error_auth(e)
        raise le
    except Exception as e:
        log.error(f'Erro ao executar login: {e}')
        await notify.send_notification_error_execution(e)
        app.driver.quit()
        raise e
        
    while not is_free:
        try:
            if app.is_error():
                app.driver.quit()
                return False
            if app.need_login():
                app.driver.get("https://prenotami.esteri.it")
                auth.login()
                time.sleep(8)
            else:
                app.driver.get("https://prenotami.esteri.it/Services")
                validation.locate_element()
                is_free = validation.validate_calendar(app.booking_id)
                time.sleep(60*app.period)
        except LoginException as le:
            log.error(f'Erro de auth: {e}')
            await notify.send_notification_error_auth(e)
            raise le
        except Exception as e:
            log.error(f'Erro ao validar data: {e}')
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
    log = setup_logger()
    while error_counter < 3 and not is_done:
        try:
            is_done = await execute()
        except LoginException as le:
            log.error(f'Erro de auth: {le}')
            
            login_error_counter = login_error_counter + 1
            log.info(f'Contador de erro de login: {login_error_counter}')
            if login_error_counter >= 3:
                log.info(f'Pausando execução')
                time.sleep(60*30)
                login_error_counter = 0
                error_counter = error_counter + 1
        except Exception as e:
            error_counter = error_counter + 1
            log.error(f'Erro ao executar loop  externo: {e}')
            log.error(f'Número de erros: {error_counter} | Número máximo de erros: 3')
    notify = Notify()
    await notify.send_notification_error_execution('PARANDO EXECUÇÃO...')
    log.info('Parando execução...')
    



if __name__ == "__main__":
    asyncio.run(run())