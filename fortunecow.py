#!/usr/bin/python3
# ©Featherton 2022 (Barry Piel)

import shutil
import os

cowsaypath = shutil.which("cowsay")
lolcatpath = shutil.which("lolcat")
fortunepath = shutil.which("fortune")

def custfort(lol=True):
    newfort = input("...")
    if newfort.strip() == "":
            pass
    else:
        os.system("clear")
        if lol == True:
            os.system("cowsay " + '"' + newfort + '" | lolcat')
        else:
            os.system("cowsay " + '"' + newfort + '"')
        custfort()
 

# Check if cowsay, fortune, and lolcat are installed
if cowsaypath != None and fortunepath != None:
    if lolcatpath != None:
        while True:
            try:
                os.system("clear")
                os.system("fortune | cowsay | lolcat")
                print("\n\n\n")
                newfort = input("...")
                if newfort.strip() == "":
                    pass
                else:
                    os.system("clear")
                    os.system("cowsay " + '"' + newfort + '" | lolcat')
                    custfort()       
            except:
                print("\nTerminated...")
                break
    else:
        while True:
            try:
                os.system("clear")
                os.system("fortune | cowsay")
                print("\n\n\n")
                newfort = input("...")
                if newfort.strip() == "":
                    pass
                else:
                    os.system("clear")
                    os.system("cowsay " + '"' + newfort + '"')
                    custfort(False)
            except:
                print("\nTerminated...")
                break
else:
    print("cowsay, fortune-mod, are required to run this, with lolcat being optional.")
