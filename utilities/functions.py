import os
# Function to delete a single file


def deleteOneFile(folderPath: str, filename: str) -> None:
    # Construct the full path to the file
    file_path = os.path.join(folderPath, filename)
    try:
        # Attempt to remove the file
        os.remove(file_path)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except PermissionError:
        print(f"Permission denied when attempting to delete '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred while deleting '{filename}': {e}")

# Function to check if a file name contains a specified keyword


def IsFileADuplicate(filename: str, key: str) -> bool:
    return key in filename

# Function to check if a folder exists at the specified path


def DoesFolderExists(folderPath: str) -> bool:
    # Construct the full path to the folder
    fullPath = os.path.join(os.path.expanduser('~/'), folderPath)
    return (os.path.exists(fullPath) and os.path.isdir(fullPath))

# Function to check if a path corresponds to a folder


def IsFolder(path: str) -> bool:
    return os.path.isdir(path)

# Function to remove duplicate files from a list in a specified folder


def RemoveDuplicates(files: list, folderPath: str) -> None:
    # Construct the full path to the folder
    fullPath = os.path.join(os.path.expanduser('~/'), folderPath)
    for file in files:
        # Use deleteOneFile function to remove each file
        deleteOneFile(fullPath, file)
        print("- " + file + " has been removed")

# Function to get a list of duplicate files in a specified folder


def GetDuplicateFiles(folderPath: str) -> list:
    # In macOS, "copy" is the keyword to identify a duplicate file (for Windows, it must be changed)
    key = "copy"
    duplicates = []

    if DoesFolderExists(folderPath):
        # Construct the full path to the folder
        fullPath = os.path.join(os.path.expanduser('~/'), folderPath)
        # Get a list of all files in the folder
        files = os.listdir(fullPath)
        # Loop through all files and check for duplicates
        for file in files:
            if IsFileADuplicate(file, key):
                # Check if the item is not a folder and add it to duplicates
                if not IsFolder(file):
                    duplicates.append(file)
    else:
        print("Folder " + str(folderPath) +
              " does not exist or is not a directory.")
    return duplicates

# Function to check if a list of files contains duplicates

# checks for length of duplicates


def hasDuplicates(files: list) -> bool:
    return len(files) > 0

# checks for valid integer


def validateInt(number: str) -> bool:
    return number.isnumeric()

# removes leading slash from string


def removeLeadingSlash(folderPath: str) -> str:
    if folderPath and folderPath[0] == "/":
        return folderPath[1:]
    return folderPath

# converts time to seconds and return the result


def convertTimeToSeconds(hours: int, minutes: int, seconds: int) -> int:
    totalSeconds = (hours * 3600) + (minutes * 60) + seconds
    return totalSeconds

# validate hours


def isValidHours(hours: int) -> bool:
    return hours >= 0

# validate minutes


def isValidMinutes(minutes: int) -> bool:
    return 0 <= minutes <= 60

# validate seconds


def isValidSeconds(seconds: int) -> bool:
    return 10 <= seconds <= 60
