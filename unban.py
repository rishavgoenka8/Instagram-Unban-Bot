import time
from webbot import *
from selenium import webdriver
import pyautogui

import argparse
import sys

# To parse the arguments


def getOptions(args=sys.argv[1:]):

    parser = argparse.ArgumentParser(
        description="This bot helps unban instagram accounts.")
    parser.add_argument("-u", "--username", type=str,
                        default="", help="Username to unban.")
    parser.add_argument("-n", "--fullname", type=str,
                        default="", help="Fullname of user.")
    parser.add_argument("-e", "--email", type=str,
                        default="", help="Email of user.")
    parser.add_argument("-f", "--file", type=str, default="proxies.txt",
                        help="Proxies list")

    options = parser.parse_args(args)

    return options


args = getOptions()

fullname = args.fullname
username = args.username
email = args.email
proxies_file = args.file

proxies_list = open(proxies_file, "r").readlines()
proxies = [s.rstrip()for s in proxies_list]

if username == "":
	username = input("Username: ")

if fullname == "":
	fullname = input("Fullname: ")

if email == "":
	email = input("Email: ")

for proxy in proxies:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % proxy)
    chrome = webdriver.Chrome(chrome_options=chrome_options)
    chrome.get("https://help.instagram.com/contact/1652567838289083")

print(username)
print(fullname)
print(email)
print(proxies)