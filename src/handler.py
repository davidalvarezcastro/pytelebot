from dotenv import load_dotenv
import telegram
import os
import sys

# loading env vars
load_dotenv()


TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')


def send_message(msg):
    """ Functions to send a message to a chat

    Args:
        msg (str)
    Returns:
        None
    """
    print(msg)
    bot = telegram.Bot(token=TOKEN)
    bot.sendMessage(chat_id=CHAT_ID, text=msg)
