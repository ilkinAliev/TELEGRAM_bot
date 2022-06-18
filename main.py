from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_command import *



app = ApplicationBuilder().token("5590632146:AAEsMoXBt9y_WEqzAQ5LhxEamVJq8JsrYnE").build()

app.add_handler(CommandHandler("salam", salam_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("mylt", mylt_command))
app.add_handler(CommandHandler("combo", combination_command))

app.add_handler(CommandHandler("downvideo", yt_command))

app.add_handler(CommandHandler("weather", weather_command))

print('server start')

app.run_polling()