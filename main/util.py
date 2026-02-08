import os, constants

def print_welcome_message():
    print_line()
    print("Welcome to myGymClub!")
    print_line()
    print(f"Running on http://127.0.0.1:{constants.PORT}")
    print("Press CTRL + C in the terminal to close this application")


def clear_terminal():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Mac and Linux (POSIX systems)
    else:
        _ = os.system('clear')

def print_line(): 
    print("*******************************")
