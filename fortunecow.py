#!/usr/bin/python3
# ©Featherton 2022 (Barry Piel)

import shutil
import os

cowsaypath = shutil.which("cowsay")
lolcatpath = shutil.which("lolcat")
fortunepath = shutil.which("fortune")

# Check if cowsay, fortune, and lolcat are installed
if cowsaypath != None and fortunepath != None:
    if lolcatpath != None:
        while True:
            try:
                os.system("clear")
                os.system("fortune | cowsay | lolcat")
                print("\n\n\n")
                input("...")
            except:
                print("\nTerminated...")
                break
    else:
        while True:
            try:
                os.system("clear")
                os.system("fortune | cowsay")
                print("\n\n\n")
                input("...")
            except:
                print("\nTerminated...")
                break
else:
    print("cowsay, fortune-mod, are required to run this, with lolcat being optional.")
