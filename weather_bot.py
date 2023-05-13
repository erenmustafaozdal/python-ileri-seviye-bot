from settings import API_TOKEN
from aiogram import Bot, Dispatcher, executor, types

# botu oluşturalım
bot = Bot(token=API_TOKEN)
# mesajları yakalamak için dispatcher nesnesi oluşturalım
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_hello(message: types.Message):
    await message.reply("Merhaba, ben Hava Durumu Bot")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
