from aiogram import Router, F, types
from aiogram.filters import Command
from bot import bot, scheduler
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

delayed_answer_router = Router()

class Form(StatesGroup):
    text = State()

@delayed_answer_router.message(Command('remind'))
async def get_reminder_text(message: types.Message, state: FSMContext):
    await state.set_state(Form.text)
    await message.answer('What should I notify?')

@delayed_answer_router.message(Form.text)
async def reminder(message: types.Message, state):
    data = await state.get_data()
    text = message.text

    scheduler.add_job(
        send_reminder,
        trigger='interval',
        seconds=10,
        kwargs={'chat_id': message.from_user.id, 'reminder_text': text}
    )
    await message.answer(f'I will remind {text} in 10 seconds')


async def send_reminder(chat_id: int, reminder_text: str):
    await bot.send_message(
        chat_id=chat_id,
        text=f'Reminder: {reminder_text}'
    )