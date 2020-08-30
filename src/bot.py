from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv
import telegram
import os

# ENV
load_dotenv()
TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')


class Bot:

    def __init__(self):
        self.__updater = Updater(token=TOKEN, use_context=True)
        self.__dispatcher = self.__updater.dispatcher

        # handlers
        self.__dispatcher.add_handler(CommandHandler('start', self.start))
        self.__dispatcher.add_handler(MessageHandler(
            Filters.text & (~Filters.command), self.echo))
        self.__dispatcher.add_handler(
            MessageHandler(Filters.command, self.unknown))

    def start(self, update, context):
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

    def echo(self, update, context):
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=update.message.text)

    def unknown(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Sorry, I didn't understand that command.")

    def run(self):
        """ Function to start running the bot
        """
        self.__updater.start_polling()


bot = Bot()
bot.run()
