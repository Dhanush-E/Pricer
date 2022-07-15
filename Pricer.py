import telegram.ext
import requests
import time
from bs4 import BeautifulSoup
import compareprice as cp
import yahoo_fin.stock_info as y
import pandas as pd


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

def stockprice(update,context):
	sp1 = context.args[0]
	sp = y.get_live_price(sp1)
	update.message.reply_text(f"The stock price of {sp1} in NYSC is {sp} USD")



def goldprice(update,context):
	url = 'https://gadgets360.com/finance/gold-rate-in-india'
	r = requests.get(url)
	html_gp = r.content
	soup_gp = BeautifulSoup(html_gp,'html.parser')
	price_gp = soup_gp.find('li',class_ = '_crprw _flx')
	update.message.reply_text(price_gp.text)



updater = telegram.ext.Updater(TOKEN,use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start",start))
disp.add_handler(telegram.ext.CommandHandler("compareprice",compareprice))
disp.add_handler(telegram.ext.CommandHandler("stockprice",stockprice))
disp.add_handler(telegram.ext.CommandHandler("goldprice",goldprice))
updater.start_polling()
updater.idle()
