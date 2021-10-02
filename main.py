from telegram import Update
from telegram.ext import Updater,CommandHandler,CallbackContext
from config import TOKEN,PORT


def start(update:Update,context:CallbackContext):
	update.message.reply_text('hello  {}'.format(update.message.from_user.username))

for i in range(1000):
	updater = Updater(TOKEN)
	dp = updater.dispatcher
	dp.add_handler(CommandHandler('start',start))
	updater.start_webhook('0.0.0.0',PORT,TOKEN,webhook_url='https://none101.herokuapp.com/'+TOKEN)
	updater.idle()
