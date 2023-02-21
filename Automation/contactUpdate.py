from selenium import webdriver
from time import sleep as w
import inputBox
import pandas as pd
import sendEmail
contacts_to_add = pd.read_excel(r"C:\Users\NathanMey\Documents\Vantage\Contracts\Unitrans\contactUpdates\contacts.xlsx")


username = inputBox.input_with_button('Please type in your username for the site')
password = inputBox.input_with_button('Please type in your password for the site')

browser = webdriver.Chrome()
browser.get('https://portal.prima.run')

# Lets the user see and also load the element
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
for index, row in contacts_to_add.iterrows():
    name = row['name']
    email = row['email']
    browser.get('https://portal.prima.run/contactlist/add')
    w(3)

    browser.find_element("xpath",'//*[@id="name"]').send_keys(name)
    browser.find_element("xpath",'//*[@id="email"]').send_keys(email)
    browser.find_element("xpath",'//*[@id="cellphoneNumber"]').send_keys('+27')
    browser.find_element("xpath",'//*[@id="smsBan"]').click()
    browser.find_element("xpath",'//*[@id="callBan"]').click()
    browser.find_element("xpath",'//*[@id="whatsappBan"]').click()
    w(1)
    browser.find_element("xpath", '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/form/div[6]/button').click()
    w(5)


