from selenium import webdriver
from time import sleep as w
from selenium.webdriver.common.keys import Keys
from pathlib import Path
from datetime import date
import pandas as pd
import inputBox
import sendEmail
#--------------------------------------------------------------------------------------------------------------------------------------------------

#Check if file exists
def test():
    print('yeet')
    w(2)
    exit

today=date.today()
f="C:\\Users\\NathanMey\\Downloads\\Driver Media Status Report "+today.strftime("%Y-%m-%d")+".xlsx"

if Path(f).is_file() == False :
    # Creating an instance webdriver
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
    analysisTab = browser.find_element("xpath", "//*[text()='Analysis']")
    analysisTab.click()

    w(1)
    reportList = browser.find_element("xpath", "//*[@id='root']/div/div[1]/div/div/div[2]/div[2]/div[4]/div[4]/li")
    reportList.click()
    w(4)

    filterName = browser.find_element("xpath", "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div/table/thead/tr[3]/th[3]/div/div/input")
    filterName.send_keys('Driver Media Status Report')
    filterName.send_keys(Keys.RETURN)
    w(3)

    expandReport = browser.find_element("xpath", "/html/body/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div/table/tbody/tr/td[2]/div/button[1]")
    expandReport.click()
    w(2)
    generateTab = browser.find_element("xpath", "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div/button[2]")
    generateTab.click()
    w(2)
    dateField = browser.find_element("xpath", "/html/body/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[1]/div[1]/div/div/div/div/button[2]")
    dateField.send_keys('Last 7 Days (include today)', Keys.ARROW_DOWN, Keys.ENTER)
    w(2)
    contractField = browser.find_element("xpath", "//*[@id='parameters[0].value']")
    contractField.send_keys('CNTY')
    w(2)
    contractField.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

    w(2)

    generateButton = browser.find_element("xpath", "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/button[1]")
    generateButton.click()
    w(10)

toDriverisk = open(r"C:\Users\NathanMey\Documents\Driverisk\County Fair Mass Resolve " + today.strftime(
        '%Y%m%d') + ".csv", 'w')
df = pd.read_excel(f, 'DATA', usecols=("event_status", "external_customer_event_id_string"))
df = df.loc[df['event_status'] == "ACKNOWLEDGED", ]
df = df['external_customer_event_id_string']
df.to_csv(toDriverisk, index=False)


# emailContent = " Good day Thembani,\nI hope this email finds you well.\nPlease see attached the updates for the Driver Media Stauts Report Acknowledged status.\n\nKind regards,\nNathan Mey"
# sendEmail.send_email('thembani.ncalane@driverisk.com', 'Driver Media Status Report Update', r"C:\Users\NathanMey\Documents\Driverisk\County Fair Mass Resolve " + today.strftime(
#        '%Y%m%d') + ".csv", emailContent)
