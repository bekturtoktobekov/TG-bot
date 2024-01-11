#TG bot
import asyncio
from aiogram import types
import logging
from pathlib import Path
from bot import bot, dp, scheduler
from handlers.picture import pic_router
from handlers.start import start_router
from handlers.echo import echo_router
from handlers.categories import categories_router
from handlers.cons import consultation
from handlers.delayed_answer import delayed_answer_router
from handlers.groupadmin import group_admin_router
from db.queries import init_db, create_table, populate_table
images_directory = Path('/Users/bektur/Downloads/cars sample')

async def on_startup(dispatcher):
    print('Bot is online')
    init_db()
    create_table()
    populate_table()

async def main():
    await bot.set_my_commands([
        types.BotCommand(command='start', description='начало'),
        types.BotCommand(command='random_pic', description='случайная картинка'),
        types.BotCommand(command='categories', description='модель авто'),
        types.BotCommand(command='consultation', description= 'Записаться на консультацию'),
        types.BotCommand(command='get_cars', description='cars'),
        types.BotCommand(command='get_flats', description='flats'),
        types.BotCommand(command='remind', description='напоминалка'),
    ])

    dp.include_router(pic_router)
    dp.include_router(start_router)
    dp.include_router(consultation)
    dp.include_router(categories_router)
    dp.include_router(delayed_answer_router)
    dp.include_router(group_admin_router)
    dp.include_router(echo_router)
    dp.startup.register(on_startup)
    #запуск планировщика
    scheduler.start()
    #обрабатываем все сообщения
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    #запускаем бота
    asyncio.run(main())