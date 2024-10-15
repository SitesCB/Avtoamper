from django.core.management.base import BaseCommand
from django.conf import settings

from aiogram import Bot, Dispatcher, executor
from aiogram.types import *

import os
import sqlite3
import json
import asyncio

bot = Bot('6993669434:AAGwSMLGIISh9yjjHZGZE5mBLzLiWpNTcxc')
dp = Dispatcher(bot)

class Command(BaseCommand):
    help = 'AvtoAmper backrequest tg bot'

    async def on_startup(self, dp):
        pass


    def handle(self, *args, **kwargs):
        # bot.enable_save_next_step_handlers(delay=2) # Сохранение обработчиков
        # bot.load_next_step_handlers()				# Загрузка обработчиков
        # bot.infinity_polling()						# Бесконечный цикл бота

        executor.start_polling(dp, on_startup=self.on_startup)

async def check_send_requests() -> None:
    connect = sqlite3.connect('db.sqlite3')
    cursor = connect.cursor()

    cursor.execute('SELECT * FROM main_requestsmodel')
    result = cursor.fetchall()

    with open('main/management/commands/data.json') as data_json:
        data = json.load(data_json)

    if int(data['result']) < len(result):
        data['result'] = len(result)
        with open('main/management/commands/data.json', 'w') as data_json:
            json.dump(data, data_json, indent=4, ensure_ascii=False)
        last_one = result[-1]
        text = f'''
        Вам пришла новая заявка \nИмя заявки: {last_one[1]} \nНомер телефона заявки: {last_one[2]} \nМарка авто заявки: {last_one[3]}\n{f'Выбранный товар: {last_one[5]}' if last_one[5] is not None else ''}\n{f'Текст заказчика: {last_one[4]}' if last_one[4] != '' else ''}
        '''
        await bot.send_message(794764771, text)

async def execute_check_send() -> None:
    while True:
        await check_send_requests()
        await asyncio.sleep(1)

asyncio.run(execute_check_send())

