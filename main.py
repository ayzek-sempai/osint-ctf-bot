import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command

# Set up logging
logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")
# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher()
# Define specific responses
RESPONSES = {
    "flag" : "Get lost, lmao",
    "money" : "Send me some money then we talk)",
    "100$" : "Hint is...",
    "1000$" : "Hint is try harder",
    "I had a great stay at this hotel. Everything was spotless, from the lobby to the rooms, which were also very comfortable. The private beach, reserved for residents, added an extra layer of relaxation. The staff was attentive and provided excellent service. Overall, a very enjoyable experience!" : "Here is your reward Detective: \n bitwalls_ctf{G00D_80Y_ \nAlso send me name and surname of manager that responded to me and I will give you other part of the reward you need.",
    "Sanjeev Patil":"Here its: \n3277235f34777c657b4a685f7b3e} \nThank you!",
    "Miravere Hotel":"Nice, can you also give me other name of this hotel. My guys trying to find, but they have been in georgia several years ago, so they need the older name. But here is your half payment: bitwalls_ctf{D0_u_W0rk_4_NSA_",
    "Mira Vere Hotel":"Nice, can you also give me other name of this hotel. My guys trying to find, but they have been in georgia several years ago, so they need the older name. But here is your half payment: bitwalls_ctf{D0_u_W0rk_4_NSA_",
    "Hotel Europe":"Thank you, here is other part of payment: 603d7b4a45462876744a36272b}"

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
