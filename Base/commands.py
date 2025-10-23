from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
import os
from Logging.logger import get_logger


base_router = Router()
logger = get_logger(__name__)

@base_router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(text="Hello")


@base_router.message(Command("about"))
async def cmd_about(message: Message):
    version: str = os.getenv("VERSION_BOT")
    creator: str = os.getenv('CREATOR_BOT')

    await message.answer(text=f"{version}, {creator}", parse_mode='Markdown')
