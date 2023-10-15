import os
import colorama
import sys
import time
import webbrowser
import pyautogui
from faker import Faker
from colorama import Fore

def menu():
    global onstart
    print(f"""
{Fore.MAGENTA}
███████╗ ██████╗ ███╗   ███╗██████╗ ██╗███████╗    ██╗  ██╗██╗   ██╗██████╗
╚══███╔╝██╔═══██╗████╗ ████║██╔══██╗██║██╔════╝    ██║  ██║██║   ██║██╔══██╗
  ███╔╝ ██║   ██║██╔████╔██║██████╔╝██║█████╗      ███████║██║   ██║██████╔╝
 ███╔╝  ██║   ██║██║╚██╔╝██║██╔══██╗██║██╔══╝      ██╔══██║██║   ██║██╔══██╗
███████╗╚██████╔╝██║ ╚═╝ ██║██████╔╝██║███████╗    ██║  ██║╚██████╔╝██████╔╝
╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚═╝╚══════╝    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝

{Fore.WHITE}
{"[help]    [SHOP]":^120}

{"[0] Exit":<30}{"[3] SWEAZY'S TOOL #3":<30}
{"[1] TOKEN GEN  #1":<30}{"[4] PUTTY  #4":<30}
{"[2] UNSTABLE DDOS #2":<30}{"[5] Message spammer":<30}
{"[6] Data Faker":<30} {"[7] Nitro sniper ":<30}

{Fore.WHITE}
""")

    command = input(">")

    if command == "0":
        print("> Do you really want to leave?")
        command = input("> Y/N $>")
        time.sleep(1)

        if command.lower() == "y":
            time.sleep(1)
            print("> Exiting... See you next time!")
            time.sleep(1)
            sys.exit(0)

        elif command.lower() == "n":
            time.sleep(1)
            print("> Nevermind... You're Back!")
            time.sleep(1)
            onstart()

    elif command == "help":
        time.sleep(1)
        print("""> Contact :

        DISCORD: https://dsc.gg/cool-shit
        USE COMMON SENSE...
        """)
        time.sleep(1)
        onstart()

    elif command == "SHOP":
        print("https://r69.mysellix.io")
        print('use "BLmXhjFxNsaHuYsJ" for 10% off, only 6 uses!!')
        time.sleep(3)
        onstart()

    elif command == "1":
        webbrowser.open('https://cdn.discordapp.com/attachments/966419814698590308/1003805238513389628/discord_token.genV3.exe')

    elif command == "2":
        webbrowser.open('https://github.com/iJoshoa/UnstableDDoS/archive/refs/heads/master.zip')

    elif command == "3":
        webbrowser.open('https://cdn.discordapp.com/attachments/1160065095695601755/1160068245018116177/Sweazy.bat?ex=653350be&is=6520dbbe&hm=7e982f79bf0a54797eeba70cd30d50423db4d57c7996e49e0921e3e757a4c064&')

    elif command == "4":
        webbrowser.open('https://the.earth.li/~sgtatham/putty/latest/w64/putty-64bit-0.79-installer.msi')

    elif command == "5":
        msg = input("Enter the message: ")
        n = input("How many times? : ")
        print("T minus")
        count = 5
        while count != 0:
            print(count)
            time.sleep(1)
            count -= 1
        print("Fire in the hole!!!")
        for i in range(0, int(n)):
            pyautogui.typewrite(msg + '\n')
        onstart()

    elif command == "6":
        # Data Faker
        fake = Faker()
        for i in fake.profile():
            print(i.upper(), ':', fake.profile()[i])
        time.sleep(5)
        onstart()

    elif command == "7":
        webbrowser.open('https://mega.nz/file/l2FByDLY')
        print("key is XvESGNG21pmBD1LaL-gZE-_NDssPtYJYtCcypdyOf1k     ENJOY!!!")
        time.sleep(4)
        onstart()

    else:
        print("Invalid command")

def onstart():
    cmd = 'mode 120,28'
    os.system(cmd)
    os.system("cls && title ZOMBIE - ")
    menu()

if __name__ == "__main__":
    onstart()
