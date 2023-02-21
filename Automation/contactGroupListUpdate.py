from selenium import webdriver
from time import sleep as w
from selenium.webdriver.common.keys import Keys
from pathlib import Path
from datetime import date
import pandas as pd
import sendEmail
import inputBox
contacts_to_add = pd.read_excel(r"C:\Users\NathanMey\Documents\Vantage\Contracts\Unitrans\contactUpdates\contacts.xlsx")

username = inputBox.input_with_button('Please type in your username for the site')
password = inputBox.input_with_button('Please type in your password for the site')

browser = webdriver.Chrome()
browser.get('https://portal.prima.run')

# Let's the user see and also load the element
w(1)

# Fill username
usernameField = browser.find_elements("xpath", '//*[@id="email"]')
usernameField[0].send_keys(username)
# Fill password
passwordField = browser.find_elements("xpath", '//*[@id="password"]')
passwordField[0].send_keys(password)
# Press submit
submit = browser.find_element("xpath", '//button[@name="submit"]')
submit.click()

browser.maximize_window()
w(4)
n = 127
for index, row in contacts_to_add.iterrows():
    name = row['name']
    browser.get('https://portal.prima.run/contactgrouplist/'+str(n)+'?tab=Contacts')
    w(3)
    browser.find_element('xpath','//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/table/thead/tr[3]/th[2]/div/div/button').click()
    browser.find_element('xpath','//*[@id="mui-1416"]').send_keys(name,Keys.ARROW_DOWN,Keys.ENTER)
    w(1)
    browser.find_element('xpath','//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div/table/tbody/tr[1]/td[2]/div/div/button[1]').click()
    w(3)
    n=n+1


