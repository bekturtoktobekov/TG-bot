from aiogram import Router, F,  types
from aiogram.filters import Command

start_router = Router()

@start_router.message(Command('start'))
async def start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text='Главная страница', callback_data='main_page')],
            [types.InlineKeyboardButton(url='https://go.2gis.com/mrucvi', text='Адрес'),
            types.InlineKeyboardButton(text='Контакты', callback_data='contacts')],
            [types.InlineKeyboardButton(text='О нас', callback_data='about'),],
            [types.InlineKeyboardButton(text='Консультация', callback_data='consult')]
        ]
    )
    await message.answer(f'Привет, {message.from_user.full_name}', reply_markup=keyboard)

'''обработчик кнопки ABOUT US'''

@start_router.callback_query(F.data == 'contacts')
async def contacts(callback: types.CallbackQuery):
    await callback.message.answer('Справочная: 0999 88 77 66\nОтдел продаж: 0222 33 34 44')

@start_router.callback_query(F.data == 'about')
async def about_us(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer(f'Привет, {callback.from_user.first_name} Мы автосалон, у нас ты точно найдешь подходящюю машину!')

@start_router.callback_query(F.data == 'main_page')
async def main_page_callback(callback: types.CallbackQuery):
    await callback.message.answer("Вы нажали кнопку 'Главная страница. Чтобы перейти нажмите /categories'")

@start_router.callback_query(F.data == 'consult')
async def consulting(callback: types.CallbackQuery):
    await callback.message.answer('Чтобы записаться на консультацию нажмите /consultation')


