import telegram.ext
import requests
import time
from bs4 import BeautifulSoup
import compareprice as cp

with open('token.txt','r') as f:
	TOKEN = f.read()

def start(update,context):
	update.message.reply_text("Hello! Welcome to PricerBot!")
	update.message.reply_text("Compare price of a product from different websites --- /compareprice Product name")

#price comparsion of a product from various websites
def compareprice(update,context):
	c = context.args[0]
	update.message.reply_text(f"{context.args[0]}")
	price_flipkart = cp.flipkart(c)
	price_ebay = cp.ebay(c)
	price_alibaba = cp.alibaba(c)
	update.message.reply_text(f"Flipkart: {price_flipkart}\nEbay: {price_ebay}\nalibaba: {price_alibaba}")

updater = telegram.ext.Updater(TOKEN,use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start",start))
disp.add_handler(telegram.ext.CommandHandler("compareprice",compareprice))
updater.start_polling()
updater.idle()