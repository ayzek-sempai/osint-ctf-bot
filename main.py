import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

# Define specific responses
RESPONSES = {
    "flag" : "Get lost, lmao",
    "money" : "Send me some money then we talk)",
    "100$" : "Hint is...",
    "1000$" : "Hint is try harder",
    "I had a great stay at this hotel. Everything was spotless, from the lobby to the rooms, which were also very comfortable. The private beach, reserved for residents, added an extra layer of relaxation. The staff was attentive and provided excellent service. Overall, a very enjoyable experience!" : "Here is your reward Detective: \n itwalls_ctf{G00D_80Y_ \nAlso send me name and surname of manager that responded to me and I will give you other part of the reward you need.",
    "Sanjeev Patil":"Here its: \n3277235f34777c657b4a685f7b3e} \nThank you!"

}

@dp.message()
async def handle_message(message: Message):
    text = message.text.strip()

    for key in RESPONSES:
        if key in text:
            response = RESPONSES[key]
            break
    else:
        response = "Do not disturb me unless it's about money or tasks i gave you🤬"
    
    await message.answer(response)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
