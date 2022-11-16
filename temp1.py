import streamlit as st

from bs4 import BeautifulSoup
from pyparsing import col
import requests
from difflib import get_close_matches
import webbrowser
from collections import defaultdict
import random
#import background_tracker

import price_tracker.temp1 as temp1

import os
import time    

# def exitval():
#     val=input('enter val')
#     if val==1:
#         pass




st.title('Eccomerce web tracker')


product_name = st.text_input("Enter the product name", "Type Here ...")

key=product_name
if(st.button('Submit')):
    result = product_name.title()
    #st.success(result)

url_flip = 'https://www.flipkart.com/search?q=' + str(
    key) + '&marketplace=FLIPKART&otracker=start&as-show=on&as=off'
map = defaultdict(list)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
source_code = requests.get(url_flip, headers=headers)
soup = BeautifulSoup(source_code.text, "html.parser")
#opt_title_flip = StringVar()
home = 'https://www.flipkart.com'
for block in soup.find_all('div', {'class': '_2kHMtA'}):
    title, price, link = None, 'Currently Unavailable', None
    for heading in block.find_all('div', {'class': '_4rR01T'}):
        title = heading.text
    for p in block.find_all('div', {'class': '_30jeq3 _1_WHN1'}):
        price = p.text[1:]
    for l in block.find_all('a', {'class': '_1fQZEK'}):
        link = home + l.get('href')

    
    
    map[title] = [price, link]
#print(list(map.keys()))
# print(list(map.values()))
products_found=st.selectbox("Products Found: ",list(map.keys()))
st.write("your selected product is:- ",products_found)
st.write("The Current price of the product is:- ",map[products_found][0])

st.header("Select your desired price")

level = st.slider("Select the level", 1,int(map[products_found][0].replace(",","")))
st.write('Selected: {}'.format(level))
