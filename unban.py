from gettext import install
import time
from typing import KeysView
from webbot import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

import argparse
import sys

# To parse the arguments


def getOptions(args=sys.argv[1:]):

    parser = argparse.ArgumentParser(
        description="This bot helps unban instagram accounts.")
    parser.add_argument("-u", "--username", type=str,
                        default="", help="Username of user.")
    parser.add_argument("-n", "--fullname", type=str,
                        default="", help="Fullname of user.")
    parser.add_argument("-e", "--email", type=str,
                        default="", help="Email of user.")
    parser.add_argument("-m", "--mobile", type=str,
                        default="", help="MObile number of user.")
    parser.add_argument("-f", "--file", type=str, default="proxies.txt",
                        help="Proxies list")

    options = parser.parse_args(args)

    return options


args = getOptions()

fullname = "Sarah Johnson"
username = "katiewaify"
email = "marvelfan2706@gmail.com"
mobile = "9028002828"
appeal = """To whom it may concern,

I am not sure why you disabled my account. I was given no warnings about violating any of your terms and conditions.  you made a mistake because I sure I never violated any terms. Please reactivate my account I've spent countless days building that page and you guys just took it from me for no reason! I don't know why you have an option to appeal the case I've sent this over 50 times and still no response and my account is still not activated I did nothing wrong! 


Thanks"""
proxies_file = args.file

proxies_list = open(proxies_file, "r").readlines()
proxies = [s.rstrip()for s in proxies_list]

if username == "":
	username = input("Username: ")

if fullname == "":
	fullname = input("Fullname: ")

if email == "":
	email = input("Email: ")

if mobile == "":
    mobile = input("Mobile: ")

for proxy in proxies:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--proxy-server=%s' % proxy)
    chrome = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    print("driver done")

    chrome.get("https://help.instagram.com/contact/606967319425038")
    print("message received")

    time.sleep(1)

    # javaScript = "document.getElementsByClassName('_55sh uiInputLabelInput')[1].click();"
    # chrome.execute_script(javaScript)

    # print("no button clicked")

    # time.sleep(0.5)

    fullname_element = chrome.find_element(By.NAME, "name")
    fullname_element.send_keys(fullname)

    time.sleep(1)

    email_element = chrome.find_element(By.NAME, "email")
    email_element.send_keys(email)

    time.sleep(1)

    username_element = chrome.find_element(By.NAME, "instagram_username")
    username_element.send_keys(username)

    time.sleep(1)
    
    mobile_element = chrome.find_element(By.NAME, "mobile_number")
    mobile_element.send_keys(mobile)

    time.sleep(1)

    appeal_element = chrome.find_element(By.NAME, "appeal_reason")
    appeal_element.send_keys(appeal)

    time.sleep(1)

    send_button = chrome.find_element(By.TAG_NAME, 'button')
    send_button.click()

    time.sleep(5)

    print("Proxy completed")

    chrome.quit()

    time.sleep(1)