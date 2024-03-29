"""
YouTube link örnekleri:
http://youtu.be/Tz9W9-u_6dw,
www.youtube.com/watch?v=Tz9W9-u_6dw&feature=feedu,
http://www.youtube.com/embed/Tz9W9-u_6dw,
http://www.youtube.com/v/Tz9W9-u_6dw?version=3&amp;hl=en_US,
https://www.youtube.com/watch?v=rTHlyTphWP0&index=6&list=PLjeDyYvG6-40qawYNR4juzvSOg-ezZ2a6,
youtube.com/watch?v=Tz9W9-u_6dw,
https://www.youtube.com/watch?v=Tz9W9-u_6dw

YouTube link regex: https:\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)(?:[\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?
Link regex: (?P<url>https?://[^\s]+)
"""
from settings import API_TOKEN
from aiogram import Bot, Dispatcher, executor, types
from modules.youtube_transcript import YouTubeTranscript
from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.answer("Merhaba, YouTube videosu alt yazılarını almak için YouTube videosu linki gönderin.")


@dp.message_handler(regexp='https:\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)(?:[\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?')
async def yt_transcript(message: types.Message):
    try:
        yt = YouTubeTranscript(message["text"])
        ts_text = yt.get_transcript()

        while ts_text:
            ts_text_send = ts_text[:4096]
            ts_text = ts_text[4096:]
            await message.reply(ts_text_send)
    except ValueError:
        await message.reply("Lütfen YouTube adresinizi kontrol edin.")
    except TranscriptsDisabled:
        await message.reply("Videonun alt yazısı devredışı bırakılmış.")
    except NoTranscriptFound:
        await message.reply("Videonun alt yazısı bulunamadı.")



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
