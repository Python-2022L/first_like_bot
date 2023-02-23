from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
import os

count_like = 0
count_dislike = 0

TOKEN=os.environ.get('TOKEN')


def start(update: Update, context:CallbackContext):
    bot = context.bot

    chat_id = update.message.chat.id

    btn1 = KeyboardButton(text=f"👍 {count_like}")
    btn2 = KeyboardButton(text=f"👎 {count_dislike}")

    keyboard = ReplyKeyboardMarkup([[btn1, btn2]], resize_keyboard=True)


    bot.sendMessage(chat_id, "LIKE and DISLIKE", reply_markup=keyboard)

def like_and_dislike(update: Update, context: CallbackContext):

    bot = context.bot
    chat_id = update.message.chat.id
    text = update.message.text[0]

    global count_like
    global count_dislike

    if text == "👍":
        count_like += 1

    if text == "👎":
        count_dislike += 1

    btn1 = KeyboardButton(text=f"👍 {count_like}")
    btn2 = KeyboardButton(text=f"👎 {count_dislike}")

    keyboard = ReplyKeyboardMarkup([[btn1, btn2]], resize_keyboard=True)


    bot.sendMessage(chat_id, "LIKE and DISLIKE", reply_markup=keyboard)
 

updater = Updater(TOKEN)
dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.text, like_and_dislike))

updater.start_polling()
updater.idle()