import os
import asyncio
import google.generativeai as genai
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# 1. Railway Variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# 2. Gemini sozlash
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Salom! Men ishlayapman. Og'abek Hamalov meni sozladi.")

@dp.message()
async def ai_handler(message: types.Message):
    try:
        # AI dan javob olish
        response = model.generate_content(message.text)
        await message.answer(f"{response.text}\n\n🤖 Og'abek Hamalov yaratgan bot.")
    except Exception as e:
        # Agar AI xato bersa, bot baribir javob berishi uchun:
        await message.answer("Hozircha AI bilan bog'lanolmadim, lekin bot ishlayapti!")
        print(f"Xato: {e}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
