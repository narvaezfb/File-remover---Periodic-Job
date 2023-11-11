# Author: Fabian Narvaez
from utilities.userInteractions import *
from utilities.functions import *
import logging
import time

logging.basicConfig(level=logging.INFO)

EXIT_COMMAND = "0"
CONFIRMATION_PROMPT = "\nAre you sure you want to delete these files? \nyes/no: "


def main():
    clear_console()
    logging.info("\t\tDuplicate File Remover\n")

    try:
        folderPath = ReceiveFolderPath()
        timeInfo = GetTimeInfo()

        DisplayInfoEntered(folderPath, timeInfo["hours"],
                           timeInfo["minutes"], timeInfo["seconds"])

        DisplayExitCommand()

        userInput = AskForConfirmation()
        confirmationAccepted = ConfirmDelete(userInput)

        if confirmationAccepted:
            if DoesFolderExists(folderPath):

                clear_console()
                duplicateFiles = GetDuplicateFiles(folderPath)

                if hasDuplicates(duplicateFiles):
                    DisplayFilesToDelete(duplicateFiles)
                else:
                    logging.error(
                        "\nNo duplicates files were found at this moment!\nEnter 'yes' to schedule the task ")

                userInput = AskForConfirmation()
                confirmationAccepted = ConfirmDelete(userInput)

                if confirmationAccepted:
                    totalSeconds = convertTimeToSeconds(
                        timeInfo["hours"], timeInfo["minutes"], timeInfo["seconds"])

                    while True:
                        clear_console()
                        duplicateFiles = GetDuplicateFiles(folderPath)
                        if hasDuplicates(duplicateFiles):
                            logging.info("\n")
                            RemoveDuplicates(duplicateFiles, folderPath)
                            print('\n')
                        else:
                            logging.info(
                                "\nNo files were removed in this batch!\n")

                        DisplayExitTask()
                        time.sleep(totalSeconds)
                else:
                    clear_console()
                    logging.info(
                        "Thanks for visiting, no files will be removed")

            else:
                logging.error("\nFolder Does not exists, try again")

        else:
            logging.error("\nNo files have been deleted.\n")

    except KeyboardInterrupt:
        logging.info("\nJob has been terminated! thanks.\n")


if __name__ == "__main__":
    main()

# documents/Python Course/challenges/periodic-job/duplicates
