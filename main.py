# Author: Fabian Narvaez
from utilities.userInteractions import *
from utilities.functions import *
import logging
import time

logging.basicConfig(level=logging.INFO)

EXIT_COMMAND = "0"
CONFIRMATION_PROMPT = "\nAre you sure you want to delete these files? \nyes/no: "
WELCOME_MESSAGE = "\t\tDuplicate File Remover\n"
NOT_FILES_FOUND_MESSAGE = "\nNo duplicates files were found at this moment!\nEnter 'yes' to schedule the task "
NOT_FILES_REMOVED = "\nNo files were removed in this batch!\n"
GOOD_BYE_MESSAGE = "\nThanks for visiting, no files will be removed"
JOB_TERMINATED_MESSAGE = "\nJob has been terminated! thanks.\n"


def main():
    clear_console()
    logging.info(WELCOME_MESSAGE)

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
                    logging.error(NOT_FILES_FOUND_MESSAGE)

                userInput = AskForConfirmation()
                confirmationAccepted = ConfirmDelete(userInput)

                if confirmationAccepted:
                    totalSeconds = convertTimeToSeconds(
                        timeInfo["hours"], timeInfo["minutes"], timeInfo["seconds"])

                    while True:
                        clear_console()
                        try:
                            duplicateFiles = GetDuplicateFiles(folderPath)
                            if hasDuplicates(duplicateFiles):
                                logging.info("\n")
                                RemoveDuplicates(duplicateFiles, folderPath)
                                print('\n')
                            else:
                                logging.info(NOT_FILES_REMOVED)

                            DisplayExitTask()
                            time.sleep(totalSeconds)
                        except KeyboardInterrupt:
                            logging.info(JOB_TERMINATED_MESSAGE)
                            break
                else:
                    clear_console()
                    logging.info(GOOD_BYE_MESSAGE)
        else:
            logging.error(GOOD_BYE_MESSAGE)

    except KeyboardInterrupt:
        logging.info(JOB_TERMINATED_MESSAGE)


if __name__ == "__main__":
    main()

# documents/Python Course/challenges/periodic-job/duplicates
