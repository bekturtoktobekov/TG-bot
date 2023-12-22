from aiogram import Router,F, types
from aiogram.filters import Command
from keyboard.keyboard_category import category_kb
from db.queries import get_categories

categories_router = Router()

@categories_router.message(Command('categories'))
async def show_categories(message: types.Message):

    # keyboard = types.ReplyKeyboardMarkup(
    #     keyboard = [
    #         [types.KeyboardButton(text='Sedan')],
    #         [types.KeyboardButton(text='SUV'),
    #         types.KeyboardButton(text='Van')],
    #         [types.KeyboardButton(text='Hatchback')]
    #     ],
    #     resize_keyboard=True
    # )
    await message.answer('Выберите категорию', reply_markup = category_kb())

@categories_router.message(Command('get_db'))
async def db_categories(message: types.Message):
    await message.answer(str(get_categories()))


@categories_router.message(F.text == 'Sedan')
async def show_sedan(message: types.Message):
    await message.answer('"Седан" - тип автомобиля с четырьмя дверьми, закрытым пассажирским отсеком и багажником. Удобный и распространенный.')

@categories_router.message(F.text == 'SUV')
async def show_suv(message: types.Message):
    await message.answer('"Кроссовер" - автомобиль с высоким клиренсом и характеристиками внедорожника.')

@categories_router.message(F.text == 'Hatchback')
async def show_hatch(message: types.Message):
    await message.answer('"Хэтчбэк" - автомобиль с задней дверью, открывающейся вверх.')

@categories_router.message(F.text == 'Van')
async def show_van(message: types.Message):
    await message.answer('"Минивэн" - многоместный автомобиль с увеличенным объемом салона.')

