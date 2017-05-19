from __future__ import print_function
from pyfiglet import *
import os
import json
import random
import time
import math
from termcolor import colored

basedir = os.path.dirname(os.path.realpath(__file__))

messegesdir = basedir + "/../messeges"
smileysdir = basedir + "/../smileys"
jsonfonts = basedir + "/fonts.json"
openingtxt = basedir + "/../opening.txt"
closingtxt = basedir + "/../closing.txt"

with open(jsonfonts) as f:
    fonts = json.load(f)
with open(openingtxt) as f:
    openingmsg = f.read()
with open(closingtxt) as f:
    closingmsg = f.read()

row, column = map(int,os.popen('stty size', 'r').read().split())

messeges = os.listdir(messegesdir)
smileys = os.listdir(smileysdir)

os.system('clear')
color = fonts["colors"][random.randint(0,(len(fonts["colors"]) - 1))]
print(colored(figlet_format(text=openingmsg, font=fonts["opening"], width=(column-1), justify="center"), color))
time.sleep(len(openingmsg.split()))

for m in messeges:
    os.system('clear')
    name = m.split(".")[0]
    with open(messegesdir + "/" + m) as f:
        messege = f.read()
    with open(smileysdir + "/" + str(smileys[random.randint(0,(len(smileys)-1))])) as f:
        smiley = f.read()
    font = fonts["messeges"][random.randint(0,(len(fonts["messeges"]) - 1))]
    color = fonts["colors"][random.randint(0,(len(fonts["colors"]) - 1))]
    print(colored(figlet_format(text=name, font=fonts["names"], width=(column-1), justify="center"), color))
    color = fonts["colors"][random.randint(0,(len(fonts["colors"]) - 1))]
    print(colored(smiley.center(column -1),color))
    color = fonts["colors"][random.randint(0,(len(fonts["colors"]) - 1))]
    print(colored(figlet_format(text=messege, font=font, width=(column-1), justify="center"), color))
    time.sleep(len(messege.split())/2)

os.system('clear')
color = fonts["colors"][random.randint(0,(len(fonts["colors"]) - 1))]
print(colored(figlet_format(text=closingmsg, font=fonts["closing"], width=(column-1), justify="center"), color))

