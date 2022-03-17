import requests
from bs4 import BeautifulSoup

def flipkart(product):
    try:
        url_flipkart = f"https://www.flipkart.com/search?q={product}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        r_flipkart = requests.get(url_flipkart)
        html_flipkart = r_flipkart.content
        soup_flipkart = BeautifulSoup(html_flipkart,'html.parser')
        price_flipkart = soup_flipkart.find('div',class_='_30jeq3 _1_WHN1')
        return price_flipkart.text
    except:
        return'product not found'
def ebay(product):
    try:
        url_ebay = f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={product}&_sacat=0'
        r_ebay = requests.get(url_ebay)
        html_ebay = r_ebay.content
        soup_ebay = BeautifulSoup(html_ebay,'html.parser')
        price_ebay = soup_ebay.find('span', class_ = 's-item__price')
        return price_ebay.text
    except:
        return "Product not found"
def alibaba(product):
    try:
        url_alibaba = f'https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText={product}&viewtype=&tab=&SearchScene='
        r_alibaba = requests.get(url_alibaba)
        html_alibaba = r_alibaba.content
        soup_alibaba = BeautifulSoup(html_alibaba,'html.parser')
        price_alibaba = soup_alibaba.find('span',class_ = 'elements-offer-price-normal__price')
        return price_alibaba.text
    except:
        return 'Product Not found'
