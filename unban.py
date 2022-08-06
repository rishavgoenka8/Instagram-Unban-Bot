import time
from webbot import *
import pyautogui

import argparse
import sys

# To parse the arguments


def getOptions(args=sys.argv[1:]):

    parser = argparse.ArgumentParser(
        description="This bot helps unban instagram accounts.")
    parser.add_argument("-u", "--username", type=str,
                        default="", help="Username to unban.")
    parser.add_argument("-u", "--fullname", type=str,
                        default="", help="Fullname of user.")
    parser.add_argument("-u", "--email", type=str,
                        default="", help="Email of user.")
    parser.add_argument("-f", "--file", type=str, default="acc.txt",
                        help="Accounts list ( Defaults to acc.txt in program directory ).")

    options = parser.parse_args(args)

    return options


args = getOptions()

fullname = args.fullname
username = args.username
email = args.email
