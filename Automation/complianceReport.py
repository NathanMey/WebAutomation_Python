from selenium import webdriver
from time import sleep as w
from selenium.webdriver.common.keys import Keys
from pathlib import Path
from datetime import date
import inputBox

# ----------------------------------------------------------------------------------------------------------------------


today=date.today()
f = "C:\\Users\\NathanMey\\Downloads\\Daily Compliance Report\\"+today.strftime("%Y-%m-%d")+".xlsx"

if Path(f).is_file():
    complianceReport = open(f,'w')
else:
    username = inputBox.input_with_button('Please type in your username for the site')
    password = inputBox.input_with_button('Please type in your password for the site')
    # Creating an instance webdriver
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

    analysisTab = browser.find_element("xpath", "//*[text()='Analysis']")
    analysisTab.click()

    w(1)

    reportList = browser.find_element("xpath", "//*[@id='root']/div/div[1]/div/div/div[2]/div[2]/div[4]/div[4]/li")
    reportList.click()

    w(4)

    filterName = browser.find_element("xpath","//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div/table/thead/tr[3]/th[3]/div/div/input")
    filterName.send_keys('Daily Compliance Report')
    filterName.send_keys(Keys.RETURN)

    w(3)

    expandReport = browser.find_element("xpath","/html/body/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div/table/tbody/tr/td[2]/div/button[1]")
    expandReport.click()

    w(2)

    generateTab = browser.find_element("xpath","//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div/button[2]")
    generateTab.click()

    dateField = browser.find_element("xpath","/html/body/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[1]/div[1]/div/div/div/input")

    w(2)

    dateField.send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ENTER)

    w(3)

    contractField = browser.find_element("xpath", "//*[@id='parameters[0].value']")
    contractField.send_keys('All')

    w(2)

    contractField.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

    w(2)

    generateButton = browser.find_element("xpath",
                                          "/html/body/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/button[1]")
    generateButton.click()

    w(20)
