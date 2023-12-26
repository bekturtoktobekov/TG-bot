#FSM = Finite state machine - конечный автомат

from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from keyboard.keyboard_category import category_kb

consultation = Router()

class Form(StatesGroup):
    name = State()
    brand = State()
    engine = State()
    category = State()
    budget = State()
    phone = State()

@consultation.message(Command('consultation'))
async def start_cons(message: types.Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer('Как вас зовут?')

@consultation.message(Command('Stop'))
async def stop(message: types.Message, state: FSMContext):
    await state.clear()

@consultation.message(Form.name)
async def process_name(message: types.Message, state: FSMContext):
    if len(message.text) < 3:
        await message.answer('Cлишком короткое имя')
        return
    else:
        await state.update_data(name=message.text)
        await message.answer(f'Спасибо,{message.text}!')

        await state.set_state(Form.brand)
        await message.answer('Какого бренда автомобиль ищете?')

@consultation.message(Form.brand)
async def brand(message: types.Message, state: FSMContext):
    if len(message.text) < 2:
        await message.answer('Такого бренда не бывает!')
        return
    else:
        await state.update_data(brand=message.text)

        await state.set_state(Form.engine)
        await message.answer("Какой объём двигателя предпочитаете?")


@consultation.message(Form.engine)
async def process_age(message: types.Message, state: FSMContext):
    engine = message.text

    if engine.isalpha():
        await message.answer('Пожалуйста, вводите только цифры')
    elif float(engine)<0.3 or float(engine)>9.0:
        await message.answer('Таких объёмов не бывает!')
    else:
        await state.update_data(engine=float(engine))
        await state.set_state(Form.category)
        await message.answer('Какой тип кузова предпочитаете?',
                             reply_markup=category_kb())

@consultation.message(Form.category)
async def category_state(message: types.Message, state: FSMContext):
    await state.update_data(category=message.text)

    await state.set_state(Form.budget)
    await message.answer('Ваш бюджет в USD$?')

@consultation.message(Form.budget)
async def budget(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Только цифры!')
    else:
        await state.update_data(budget=message.text)

        await state.set_state(Form.phone)
        await message.answer("Ваш номер телефона?")

@consultation.message(Form.phone)
async def tel_number(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    data = message.answer(f'oo')
    await message.answer(f'Спасибо что прошли опроc, в скором времени с вами свяжется наш менеджер.')
    await state.clear()



