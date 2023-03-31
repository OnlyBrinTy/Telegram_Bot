import os
import random
from datetime import datetime

from telegram.ext import Application, MessageHandler, filters, CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from dotenv import load_dotenv
# from config import BOT_TOKEN

# Запускаем логгирование
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
# )
#
# logger = logging.getLogger(__name__)

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Напишем соответствующие функции.

async def start(update, context):
    reply_keyboard = [['/dice', '/timer']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    await update.message.reply_text(
        "Я бот-помощник для настольных игр",
        reply_markup=markup
    )

async def help(update, context):
    await update.message.reply_text(
        "Я бот-помощник для настольных игр.")


async def dice(update, context):
    reply_keyboard = [['/one_dice', '/two_dices'],
                      ['/one_20_dice', '/back']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    await update.message.reply_text(
        "Выбирай",
        reply_markup=markup
    )

async def one_dice(update, context):
    num = random.randint(1, 6)
    await update.message.reply_text(num)


async def timer(update, context):
    await update.message.reply_text("Телефон: +7(495)776-3030")





async def close_keyboard(update, context):
    await update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("dice", dice))
    application.add_handler(CommandHandler("one_dice", one_dice))

    application.add_handler(CommandHandler("back", start))
    application.add_handler(CommandHandler("timer", timer))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("close", close_keyboard))
    application.run_polling()


if __name__ == '__main__':
    main()