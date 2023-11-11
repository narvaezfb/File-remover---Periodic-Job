import logging
import os
import sys
from utilities.functions import *

logging.basicConfig(level=logging.INFO)
ENTER_DIRECTORY_MESSAGE = "\nPlease enter directory path: "
PATH_NOT_FOUND_MESSAGE = "Path does not exists, please try again!"
ENTER_HOURS_MESSAGE = "\nPlease enter the number of hours: "
ENTER_MINUTES_MESSAGE = "Please enter the number of minutes: "
ENTER_SECONDS_MESSAGE = "Please enter the number of seconds: "
CONTINUE_MESSAGE = "\nDo you want to continue? \nyes/no: "
EXIT_COMMAND_MESSAGE = f"\nCntrl + C to exit "
EXIT_TASK_MESSAGE = f"\nCntrl + C to finish the periodic job! "
ERROR_HOURS_MESSAGE = "hours can't be negative, please try again!"
ERROR_MINUTES_MESSAGE = "minutes must be between 1 and 60, please try again!"
ERROR_SECONDS_MESSAGE = "seconds must be between 1 and 60, please try again!"
ERROR_NUMBER_MESSAGE = "Invalid value, please try again!"
# User Interactions


def ReceiveFolderPath() -> str:
    while True:
        try:
            folderPath = removeLeadingSlash(input(ENTER_DIRECTORY_MESSAGE))
            if DoesFolderExists(folderPath):
                return folderPath
            else:
                logging.error(PATH_NOT_FOUND_MESSAGE)
        except KeyboardInterrupt:
            logging.info("User interrupted. Exiting.")
            sys.exit()


def GetTimeInfo() -> dict:
    hours = GetIntFromUser(ENTER_HOURS_MESSAGE, "hours")
    minutes = GetIntFromUser(ENTER_MINUTES_MESSAGE, "minutes")
    seconds = GetIntFromUser(ENTER_SECONDS_MESSAGE, "seconds")

    timeInfo = {
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds
    }
    return timeInfo


def DisplayFilesToDelete(files: list) -> None:
    print("\nFiles to delete: (" + str(len(files)) + "):\n")
    for file in files:
        print(file)


def ConfirmDelete(input: str) -> bool:
    return input.lower() == "yes"


def AskForConfirmation() -> str:
    userConfirmation = input(CONTINUE_MESSAGE)
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
    logging.info(EXIT_COMMAND_MESSAGE)


def DisplayExitTask():
    logging.info(EXIT_TASK_MESSAGE)


def clear_console():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')


def GetIntFromUser(text: str, time: str) -> int:
    while True:
        number = input(text)
        if validateInt(number):
            number = int(number)
            if time == "hours":
                if isValidHours(number):
                    return number
                else:
                    logging.error(ERROR_HOURS_MESSAGE)
            elif time == "minutes":
                if isValidMinutes(number):
                    return number
                else:
                    logging.error(ERROR_MINUTES_MESSAGE)
            elif time == "seconds":
                if isValidSeconds(number):
                    return number
                else:
                    logging.error(ERROR_SECONDS_MESSAGE)
        else:
            logging.error(ERROR_NUMBER_MESSAGE)
