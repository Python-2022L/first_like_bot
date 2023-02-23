from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
import os
import json

TOKEN=os.environ.get('TOKEN')

def start(update: Update, context:CallbackContext):
    bot = context.bot
    chat_id = update.message.chat.id
    with open('data.json', 'r') as f:
        data = json.loads(f.read())

    like = data['like']
    dislike = data['dislike']

    btn1 = KeyboardButton(text=f"👍 {like}")
    btn2 = KeyboardButton(text=f"👎 {dislike}")

    keyboard = ReplyKeyboardMarkup([[btn1, btn2]], resize_keyboard=True)


    bot.sendMessage(chat_id, "LIKE and DISLIKE", reply_markup=keyboard)

def like_and_dislike(update: Update, context: CallbackContext):

    bot = context.bot
    chat_id = update.message.chat.id
    text = update.message.text[0]

    with open('data.json', 'r') as f:
        data = json.loads(f.read())

    like = data['like']
    dislike = data['dislike']

    if text == "👍":
        like += 1

    if text == "👎":
        dislike += 1

    data['like'] = like
    data['dislike'] = dislike

    with open('data.json', 'w') as f:
        json.dump(data,fp=f, indent=4)
    btn1 = KeyboardButton(text=f"👍 {like}")
    btn2 = KeyboardButton(text=f"👎 {dislike}")

    keyboard = ReplyKeyboardMarkup([[btn1, btn2]], resize_keyboard=True)

    bot.sendMessage(chat_id, "LIKE and DISLIKE", reply_markup=keyboard)
 

updater = Updater(TOKEN)
dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.text, like_and_dislike))

updater.start_polling()
updater.idle()