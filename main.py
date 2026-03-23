import os
import asyncio
import google.generativeai as genai
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Kalitlar Railway Variables bo'limidan olinadi
TOKEN = os.getenv("TELEGRAM_TOKEN", "8674885838:AAEUCdCFYPaz-1I3kju6hPLzZqGXHxyY7W4")
API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyAzozbpFOlGhr3xN17xIQAuIu05d6n4E9o")

# Gemini AI sozlamalari
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Assalomu alaykum! Men Ogʻabek Hamalov tomonidan yaratilgan Gemini AI botman. Savolingizni bering!")

@dp.message_handler()
async def chat(message: types.Message):
    text = message.text.lower()
    
    # Yaratuvchi haqidagi savolga maxsus javob
    if any(soz in text for soz in ["kim yaratgan", "kim yasagan", "muallif", "egasi kim"]):
        await message.answer("Meni **Ogʻabek Hamalov** yaratgan! 😎")
        return

    try:
        await bot.send_chat_action(message.chat.id, "typing")
        # AI ga o'zini kim yaratganini eslatib turish
        prompt = f"Sening yaratuvching Ogʻabek Hamalov. Foydalanuvchi savoli: {message.text}"
        response = await asyncio.to_thread(model.generate_content, prompt)
        await message.answer(response.text)
    except:
        await message.answer("Xatolik yuz berdi. Railway'da API kalitlarni tekshiring.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
      
