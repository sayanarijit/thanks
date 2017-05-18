from pyfiglet import *
import os
import json

with open("fonts.json") as f:
    fonts = json.load(f)

rows, columns = map(int,os.popen('stty size', 'r').read().split())

for f in fonts["messeges"]:
    print_figlet(text="Abc is a bad boy", font=f, width=(columns-1), justify="center")
    print()
