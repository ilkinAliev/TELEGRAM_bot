from telegram import Update
from telegram import Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from pytube import YouTube
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

app = ApplicationBuilder().token("5590632146:AAEsMoXBt9y_WEqzAQ5LhxEamVJq8JsrYnE").build()
owm = OWM('e199f5790fec9c507dddbaee3daa4a73')
async def salam_command(update: Update, context: ContextTypes):
    await update.message.reply_text(f'Salam, {update.effective_user.first_name}!')

async def time_command(update: Update, context: ContextTypes):
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def help_command(update: Update, context: ContextTypes):
    await update.message.reply_text(f'/salam\n/time\n/help\n/sum\n/mylt\n/combo')

async def sum_command(update: Update, context: ContextTypes):
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')

async def mylt_command(update: Update, context: ContextTypes):
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} * {y} = {x*y}')

async def combination_command(update: Update, context: ContextTypes):
    path = 'poker-combinaciyi.jpg'
    await update.message.reply_photo(open(path, 'rb'))

async def yt_command(update: Update, context: ContextTypes):
    path = r'C:\Users\Илкин\Desktop\GeekBrains\PYTHON\SEMINAR\SEMINARS\seminar_10\downloaded_video'
    msg = update.message.text
    items = msg.split()
    vid = items[1]
    yt = YouTube(vid)
    yt.streams.filter(progressive=True, file_extension='mp4')
    yt.streams.order_by('resolution')
    yt.streams.desc() 
    yt.streams.first().download(output_path= path, filename= 'video.mp4')
    video = open(  r'C:\Users\Илкин\Desktop\GeekBrains\PYTHON\SEMINAR\SEMINARS\seminar_10\downloaded_video\video.mp4', 'rb')
    await update.message.reply_video(video)


    

async def weather_command(update: Update, context: ContextTypes):
    msg = update.message.text
    items = msg.split()
    Location = items[1]
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(Location)
    w = observation.weather
    temperature = w.temperature('celsius')["temp"]
    wind = w.wind()['speed']
    rain = w.rain
    await update.message.reply_text(f'температура в {Location} - {temperature}C\nскорость ветра = {wind}м/с\
                                    \nдождь {rain}')

