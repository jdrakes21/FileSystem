"""
File: file_system.py
Author: Jervon Drakes
Date: 17/11/2022
Lab Section: 32
Email:  jdrakes1@umbc.edu
Description:  This program returns various information cs it relates to the attendance of students
"""

DIRECTORIES_KEY = 'directories'
FILES_KEY = 'files'
HOME_DIRECTORY_NAME = 'home'


def mk_dir(path_input, path, current_directory):
    """
  This function creates directories within the file system
  :param path_input: A string which specifies the directory which will be made
  :param path: A string which consists of the path for a directory
  :param current_directory: A dictionary which contains directories and other contents
  :return: A directory within the file system
  """
    #  determines if a directory is within the file system
    if path_input not in current_directory[DIRECTORIES_KEY]:
        # once that directory does not exist it is created
        current_directory[DIRECTORIES_KEY][path_input] = {DIRECTORIES_KEY: {}, FILES_KEY: []}
        # updates the path
        path += path_input + "/"
    else:
        # otherwise this output is printed
        print("Directory already exists here")


def update_path(up_path):
    """
  This function updates the path within the file system
  :param up_path: A list which keeps track of the path
  :return: A list of the paths within the file system
  """
    # an empty list which updates the path
    u_path = []
    # loops through this list
    for i in up_path:
        # conditional to determine if anything within the list is not equal to an empty string
        if i != '':
            # adds elements to the list once the conditional is met
            u_path.append(i)
    return u_path


def update_directory(path, my_file_system, current_directory):
    """
  This function updates and keeps track of the current directory
  :param path: A list which contains the paths within the file system
  :param my_file_system: A dictionary which contains the directories and the files
  :param current_directory: A dictionary which contains directories and other contents
  :return: A directory within the file system
  """
    # sets the current directory as the contents within hom
    current_directory = my_file_system[HOME_DIRECTORY_NAME]
    # splits the path
    path_split = path.split("/")
    # assigns the updated path as the path split
    updated_path = path_split
    # calls the update path function with updated path and assigns it as path
    path = update_path(updated_path)
    # loops through the path
    for i in path:
        # assigns a value to the current directory which helps to keep track of the current directory
        current_directory = current_directory[DIRECTORIES_KEY][i]
    return current_directory


def relative_path(u_input, path, current_directory, my_file_system):
    """
  This function takes into consideration a relative path for a directory
  :param u_input: A string which specifies the directory that may be within the directories of the current directory
  :param path: A string which consists of the path for a directory
  :param current_directory: A dictionary which contains directories and other contents
  :param my_file_system: A dictionary which contains directories and other contents
  :return: The path for a directory
  """
    # determines if a directory exists and takes the relative path
    if u_input in current_directory[DIRECTORIES_KEY]:
        print(my_file_system)
        # returns that path
        return path
    else:
        print("No such directory")


def cd(user_input, path, current_directory, my_file_system):
    """
  This function creates directories within the file system
  :param user_input: A string which specifies the directory which will be changed
  :param path: A string which consists of the path for a directory
  :param current_directory: A dictionary which contains directories and other contents
  :param my_file_system: A dictionary which contains directories and other contents
  :return: The path of the directory and its contents
  """

    # conditional to determine if the user input is this specific input
    if user_input[1] == "..":
        # once the condition is met the path is split
        path = path.split("/")
        # the current path is then brought back to the previous path
        path = "/".join(path[:-2]) + "/"
        return path
    # conditional to determine if the user input is this specific input
    elif user_input[1] == "." or user_input[1] == "":
        # the current path is then returned if this is met
        return path
    # conditional to determine if the user input is this specific input
    elif user_input[1] == "/":
        # the path is then brought back to the initial path
        path = "/"
        return path
    # conditional for the relative path of any directory and it's contents
    elif relative_path(user_input[1], path, current_directory, my_file_system):
        # assigns this value as the path
        path = path + user_input[1] + "/"
        return path
    # conditional for the absolute path
    elif absolute_path(user_input[1], path, current_directory):
        # returns the path
        return path

    else:
        print("No such directory")


def absolute_path(input_user, path, current_directory):
    """
  This function takes into consideration a relative path for a directory
  :param input_user: A string which specifies the directory that is within the directories of the current directory
  :param path: A string which consists of the path for a directory
  :param current_directory: A dictionary which contains directories and other contents
  :return: The path for a directory
  """
    # conditional to determine if the input has a specific condition
    if input_user[1] in current_directory[DIRECTORIES_KEY] == "/":
        # splits the input user which has each path
        input_user = input_user.split("/")
        # loops through the input user
        for i in range(len(input_user)):
            # conditional to determine if contents within input user are within directories
            if input_user[i] in current_directory[DIRECTORIES_KEY]:
                # sets a value for current directory
                current_directory = current_directory[DIRECTORIES_KEY][input_user[i]]
    return current_directory


def ls(current_directory, path):
    """
  This function takes into consideration a relative path for a directory
  :param current_directory: A dictionary which contains directories and other contents
  :param path: A string which consists of the path for a directory
  :return: The contents within a path
  """
    """
    # loops through the directories within the current directory
    for i in current_directory[DIRECTORIES_KEY]:
        print(i)
    # loops through the files within the current directory
    for j in current_directory[FILES_KEY]:
        print(j)
    """
    # loops through contents within the current directory
    for i in current_directory:
        for j in current_directory[i]:
            print(j)


def touch(current_directory, user_input):
    """
  This function takes into consideration a relative path for a directory
  :param current_directory: A dictionary which contains directories and other contents
  :param user_input: A string which is a file
  :return: The file created within a directory
  """
    # conditional to determine if the input is within files of the current directory
    if user_input not in current_directory[FILES_KEY]:
        # once the conditional is met the input is added to the files key of the current directory
        current_directory[FILES_KEY].append(user_input)
        # returns the files
        return current_directory[FILES_KEY]
    else:
        print("File already exists")


def locate(user_input, my_file_system, path):
    """
  This function takes into consideration a relative path for a directory
  :param user_input: A string which specifies the file that should be located
  :param my_file_system: A dictionary which contains directories and other contents
  :param path: A string which consists of the path for a directory
  :return: The path of which instances of a file are found
  """
    # base case which determines if the input is withing the files of the home directory
    if user_input in my_file_system[FILES_KEY]:
        # prints this output which is the file
        print(path + "/" + user_input)
        # conditional to determine if the directories within the file system is not empty
    if my_file_system[DIRECTORIES_KEY] != {}:
        # loops through the directories withing the file system
        for i in my_file_system[DIRECTORIES_KEY]:
            # recursive call which allows for all the paths of the file to be returned
            locate(user_input, my_file_system[DIRECTORIES_KEY][i], path + "/" + i)


def remove_file(user_input, current_directory):
    """
  This function takes into consideration a relative path for a directory
  :param user_input: A string which specifies the file that should be removed
  :param current_directory: A dictionary which contains directories and other contents
  :return: The updated contents for a specific path once the file is removed
  """
    # conditional to determine if the input is within the files of the current directory
    if user_input[1] in current_directory[FILES_KEY]:
        # removes the specific file from the files of the current directory
        current_directory[FILES_KEY].remove(user_input[1])
    else:
        print(user_input[1], "not found")


def main():
    path = "/"

    # the structure of the file system
    my_file_system = {HOME_DIRECTORY_NAME: {DIRECTORIES_KEY: {}, FILES_KEY: []}}

    current_directory = my_file_system[HOME_DIRECTORY_NAME]
    flag = True

    # loops to allow the user to enter various inputs
    while flag:
        user_input = input()
        # conditional to determine if the input is pwd
        if user_input == "pwd":
            # prints the path
            print(path)
        # conditional to determine if the input is mkdir
        elif user_input[:5] == "mkdir":
            # splits the input
            user_input = user_input.split(" ")
            # calls the mkdir function
            mk_dir(user_input[1], path, current_directory)
        # conditional to determine if the input is cd

        elif user_input[0:2] == "cd":
            # splits the input
            user_input = user_input.split(" ")
            # calls the cd function as path
            path = cd(user_input, path, current_directory, my_file_system)
            # calls the update directory function as the current directory
            current_directory = update_directory(path, my_file_system, current_directory)

        # conditional to determine if the input is ls
        elif user_input == "ls":
            # prints the content for that path
            print("Contents for", path)
            # calls the ls function
            ls(current_directory, path)

        # conditional to determine if the input is touch
        elif user_input[0:5] == "touch":
            # splits the input
            user_input = user_input.split(" ")
            # calls the update directory function as the current directory
            current_directory = update_directory(path, my_file_system, current_directory)
            # calls the touch function
            touch(current_directory, user_input[1])

        elif user_input[0:2] == "rm":
            # splits the input
            user_input = user_input.split(" ")
            # calls the update directory function as the current directory
            current_directory = update_directory(path, my_file_system, current_directory)
            # calls the remove function
            remove_file(user_input, current_directory)

        # conditional to determine if the input is locate
        elif user_input[:6] == "locate":
            # splits the input
            user_input = user_input.split(" ")
            # sets home as the home directory
            home = my_file_system[HOME_DIRECTORY_NAME]
            # prints this output
            print("A file with that name was found at the following paths: ")
            # calls the function
            locate(user_input[1], home, "")

        # conditional to determine if the input is exit which ends the program
        elif user_input[:4] == "exit":
            print("The program ends")
            flag = False


main()
