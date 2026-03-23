import os
import asyncio
import google.generativeai as genai
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# 1. Railway'dagi o'zgaruvchilarni yuklash
BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# 2. Gemini AI ni sozlash va "Xotira" (Instruction) berish
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    system_instruction="Sening isming Gemini. Seni Og'abek Hamalov yasadi. Foydalanuvchi har safar salom bersa yoki kimligingni so'rasa, albatta 'Meni Og'abek Hamalov yaratgan' deb javob ber."
)

# 3. Bot va Dispatcher ni yaratish
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# /start komandasi bosilganda
@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Assalomu alaykum! Men Og'abek Hamalov tomonidan yaratilgan aqlli botman. Savolingizni bering!")

# Har qanday xabar yozilganda (Salom va boshqalar)
@dp.message()
async def handle_message(message: types.Message):
    try:
        # Foydalanuvchi xabarini Gemini AI ga yuboramiz
        response = model.generate_content(message.text)
        
        # AI javobining boshiga yoki ichiga muallifni qo'shib yuboramiz
        final_answer = f"🤖 {response.text}\n\n✨ _Ushbu bot Og'abek Hamalov tomonidan yaratilgan._"
        
        await message.answer(final_answer, parse_mode="Markdown")
    except Exception as e:
        print(f"Xatolik: {e}")
        await message.answer("Xatolik yuz berdi. Iltimos, Railway'da API kalitlarni tekshiring.")

# Botni ishga tushirish funksiyasi
async def main():
    print("Bot muvaffaqiyatli ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
