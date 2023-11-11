import logging
import os
import sys
from utilities.functions import *

logging.basicConfig(level=logging.INFO)

# User Interactions


def ReceiveFolderPath() -> str:
    while True:
        try:
            folderPath = input(
                "\nPlease enter directory path: ")
            if DoesFolderExists(folderPath):
                return folderPath
            else:
                logging.error("Path does not exists, please try again!")
        except FileNotFoundError:
            logging.error("Path does not exists, please try again!")


def GetTimeInfo() -> dict:
    hours = GetIntFromUser("\nPlease enter the number of hours: ")
    minutes = GetIntFromUser("Please enter the number of minutes: ")
    seconds = GetIntFromUser("Please enter the number of seconds: ")

    timeInfo = {
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds
    }
    return timeInfo


def IsByDays(input: str):
    return input == "1"


def GetDaysOrTime() -> str:
    validOptions = ["1", "2"]
    while True:
        answer = input(
            "\n- Enter 1 to schedule this task for days\n- Enter 2 to schedule this task for given time\nanswer:")
        if answer in validOptions:
            return answer
        else:
            logging.error("\nOnly 1 or 2 inputs are allowed, try again")


def DisplayFilesToDelete(files: list) -> None:
    print("\nFiles to delete: (" + str(len(files)) + "):\n")
    for file in files:
        print(file)


def ConfirmDelete(input: str) -> bool:
    return input.lower() == "yes"


def AskForConfirmation() -> str:
    userConfirmation = input(
        "\nDo you want to continue? \nyes/no: ")
    return userConfirmation


def DisplaySelectedPath(folderPath) -> None:
    logging.info(f"\nSelected Path: {folderPath} \n")


def DisplaySelectedTime(hours: int, minutes: int, seconds: int) -> None:
    logging.info(f"\nSelected Time: {hours}:{minutes}:{seconds} \n")


def DisplayInfoEntered(folderPath, hours, minutes, seconds) -> None:
    clear_console()
    DisplaySelectedPath(folderPath)
    DisplaySelectedTime(hours, minutes, seconds)


def DisplayExitCommand():
    logging.info(f"\nCntrl + C to exit ")


def DisplayExitTask():
    logging.info(f"\nCntrl + C to finish the periodic job! ")


def clear_console():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')


def GetIntFromUser(text: str) -> int:
    while True:
        number = input(text)
        if validateInt(number):
            return int(number)
        else:
            logging.error("Invalid value, please try again!")
