from db.queries import get_parser
from aiogram import Router,F, types
from aiogram.filters import Command

parser_router = Router()

@parser_router.message(Command('parser'))
async def parsed_info(message: types.Message):
    parsed_data = get_parser()
    for row in parsed_data:
        formatted_row = (
            f"{row[0]},\n"
            f"Description: {row[1].strip()},\n"
            f"Location: {row[2]},\n"
            f"Price: {row[3]},\n"
            f"Details: {row[4]}"
        )
        await message.answer(formatted_row)
