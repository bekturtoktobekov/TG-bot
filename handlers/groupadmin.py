from aiogram import Router, F, types
from aiogram.filters import Command

group_admin_router = Router()
BAD_WORDS = ("дурак", "тупой")


async def is_user_owner(bot, chat_id, user_id):
    chat_member = await bot.get_chat_member(chat_id, user_id)
    return chat_member.status == 'creator'


async def is_user_admin(bot, chat_id, user_id):
    chat_member = await bot.get_chat_member(chat_id, user_id)
    return chat_member.status == 'administrator'


@group_admin_router.message(F.chat.type == "group")
@group_admin_router.message(Command("ban", prefix="!/"))
async def ban_user(message: types.Message):
    reply = message.reply_to_message
    if reply is not None:
        if await is_user_owner(message.bot, message.chat.id, reply.from_user.id):
            await message.reply("Can't ban the chat owner.")
        else:
            await message.bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=reply.from_user.id
            )
            await message.answer(f"User {reply.from_user.username} banned")


@group_admin_router.message(F.chat.type == "group")
async def catch_bad_words(message: types.Message):
    if await is_user_admin(message.bot, message.chat.id, message.from_user.id):
        await message.reply("You are an admin. Using bad words is not allowed.")
    elif await is_user_owner(message.bot, message.chat.id, message.from_user.id):
        await message.reply("You are an owner. Using bad words is not allowed.")
        return
    else:
        for word in BAD_WORDS:
            if word in message.text.lower():
                await message.reply("Can't use bad words!")
                await ban_user(message)
                await message.delete()
                break