from telegram import Bot
import os
from dotenv import load_dotenv
class Notify:
    def __init__(self):
        self.token = None
        self.chat_id = None
        self.bot = None
        self.configuration()
        pass
    def configuration(self):
        load_dotenv()
        self.token = os.getenv('TOKEN_BOT')
        self.chat_id = os.getenv('CHAT_ID')
        self.bot = Bot(token=self.token)
    async def send_notification_error_auth(self, message) :
        await self.bot.send_message(chat_id=self.chat_id, text=f'ERRO DE AUTENTICAÇÃO! {message}')
    async def send_notification_error_execution(self, message):
        await self.bot.send_message(chat_id=self.chat_id, text=f'ERRO NA EXECUÇÃO! {message}')
    async def send_notification_found(self, message):
        await self.bot.send_message(chat_id=self.chat_id, text=f'AGENDAMENTO ENCONTRADO! {message}')
        