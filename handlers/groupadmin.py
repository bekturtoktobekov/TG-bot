from aiogram import Router, F, types
from aiogram.filters import Command


group_admin_router = Router()
BAD_WORDS = ('дурак')

@group_admin_router(F.chat.type == 'group')
@group_admin_router(Command('ban', prefix='!'))
async def ban(message: types.Message):
    await message.bot.ban_chat_member(
        chat_id=message.chat.id,
        user_id=message.from_user.id
    )


@group_admin_router.message(F.chat.type == 'group')
async def cencore(message: types.Message):
    text = message.text.lower()
    for word in text:
        if word in message.text:
            await message.reply('dont use bad words')
            await message.delete()
            break

