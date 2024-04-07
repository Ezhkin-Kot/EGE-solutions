import time
import keyboard
import psutil
import os

path = ""
list_of_buttons = []
seconds = 0
process_name = ""


def application_opened(proces_name):
    for proc in psutil.process_iter(attrs=['name']):
        try:
            pinfo = proc.as_dict(attrs=['name'])
            if pinfo['name'] == proces_name:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            return False
        return False


def block_buttons(list_of_buttons, seconds):
    for button in list_of_buttons:
        keyboard.block_key(button)
    time.sleep(seconds)


def open_app(path):
    os.startfile(path)


def input_data():
    print("Which program should be blocked")
    while True:
        process_name = input("Data should be like <your_app>.exe or <your_app>.app \n")
        if ".exe" in process_name or '.app' in process_name:
            break
        else:
            print("Incorrect name")
    # print("Which program should be opened")
    # path = input("Write path to app here...")
    while True:
        numOfButtons = int(input("How much button you would like to block \n"))
        if 0 < numOfButtons < 86:
            break
    for _ in range(numOfButtons):
        list_of_buttons.append(input("Button: "))
    print("For how much time you would like to block buttons")
    while True:
        seconds = int(input("Print time in seconds \n"))
        if 0 < seconds:
            break


def main():
    print("Welcome to my app")
    input_data()
    # open_app(path)
    while True:
        if application_opened(process_name):
            block_buttons(list_of_buttons, seconds)
        time.sleep(60)

main()
