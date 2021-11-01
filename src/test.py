
import requests
from bs4 import BeautifulSoup
import os,sys,random,time
from selenium import webdriver
import pandas as pd

url = 'https://www.saucedemo.com/'

browser = webdriver.Chrome()
browser.get(url)

username = 'standard_user'              #Your email
password = 'secret_sauce'              #Your Password

elementID = browser.find_element_by_id('user-name')
elementID.send_keys(username)
time.sleep(3)
elementID = browser.find_element_by_id('password')
elementID.send_keys(password)
time.sleep(3)

elementID.submit()
time.sleep(3)


button = browser.find_element_by_id("add-to-cart-sauce-labs-backpack")
button.click()
time.sleep(3)

browser.get("https://www.saucedemo.com/cart.html")
time.sleep(3)
try:
    quantityCheck = browser.find_element_by_class_name("cart_quantity")
    print("Quantity is there")
except:
    print("Quantity is not there")
    
    
try:
    descriptionCheck = browser.find_element_by_class_name("inventory_item_desc")
    print("Description is there")
except:
    print("Description is not there")

    
removeButton = browser.find_element_by_id("remove-sauce-labs-backpack")
removeButton.click()
time.sleep(3)

continueButton = browser.find_element_by_id("continue-shopping")
continueButton.click()
time.sleep(3)
addAnotherItem = browser.find_element_by_id("add-to-cart-test.allthethings()-t-shirt-(red)")
addAnotherItem.click()

time.sleep(3)
browser.get("https://www.saucedemo.com/cart.html")
time.sleep(3)
checkoutButton = browser.find_element_by_id("checkout")
checkoutButton.click()
time.sleep(3)
submitButton = browser.find_element_by_id("continue")
submitButton.click()
time.sleep(3)

fname = 'Ram'
lname = 'Gopali'
postalcode = '534204'              

elementID1 = browser.find_element_by_id('first-name')
elementID1.send_keys(fname)
time.sleep(3)
elementID1 = browser.find_element_by_id('last-name')
elementID1.send_keys(lname)
time.sleep(3)
elementID1 = browser.find_element_by_id('postal-code')
elementID1.send_keys(postalcode)
time.sleep(3)
submitButton.click()
time.sleep(3)
browser.get(url)
