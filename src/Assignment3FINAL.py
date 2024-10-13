"""
Author : Muhammad Zain Asad
Project : Chemical Flask Game
"""

import os
from bstack import BoundedStack
from bqueue import BoundedQueue

CHEMICAL_UNITS_PER_TYPE = 3

# Define ANSI color codes
ANSI_COLORS = {
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "BLUE": "\033[34m",
    "ORANGE": "\033[33m",
    "YELLOW": "\033[33;1m",
    "MAGENTA": "\033[35m",
    "RED_BG": "\033[41m",
    "GREEN_BG": "\033[42m",
    "BLUE_BG": "\033[44m",
    "ORANGE_BG": "\033[43m",
    "YELLOW_BG": "\033[43;1m",
    "MAGENTA_BG": "\033[45m",
    "UNDERLINE": "\033[4m",
    "RESET": "\033[0m",
    "CLEARLINE": "\033[0K",
    "CLEARSCREEN": "\033[2J"
}

CHEMICALS_TO_COLORS = {
    "AA": ANSI_COLORS["RED_BG"],
    "BB": ANSI_COLORS["BLUE_BG"],
    "CC": ANSI_COLORS["GREEN_BG"],
    "DD": ANSI_COLORS["ORANGE_BG"],
    "EE": ANSI_COLORS["YELLOW_BG"],
    "FF": ANSI_COLORS["MAGENTA_BG"],
}

os.system("")


def clear_screen():
    """
    Clears the terminal screen. Uses different commands based on the operating system.
    """
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')


def read_input(file_name):
    """
    Reads the game setup from a specified file and initializes flasks based on the contents.

    Args:
        file_name (str): The path to the file containing the game's initial setup.

    Returns:
        list[BoundedStack]: A list of initialized BoundedStack objects, each representing a flask filled with chemicals as specified in the input file.
    """

    with open(file_name, 'r') as file:
        first_line = file.readline().strip().split()
        num_flasks = int(first_line[0])

        flasks = [BoundedStack(4) for _ in range(num_flasks)]
        chemicals_queue = BoundedQueue(4)

        for line in file:
            line = line.strip()
            if 'F' in line and line.replace('F', '').isdigit():
                num, flask_index = map(int, line.split('F'))
                flask_index -= 1
                if 0 <= flask_index < len(flasks):
                    while num > 0 and not chemicals_queue.isEmpty():
                        chemical = chemicals_queue.dequeue()
                        if not flasks[flask_index].isFull():
                            flasks[flask_index].push(chemical)
                            num -= 1
                        else:
                            print("Flask is full, can't add more chemicals.")
                else:
                    print("Invalid flask index.")
            else:
                if not chemicals_queue.isFull():
                    chemicals_queue.enqueue(line)
                else:
                    print("Queue is full, can't add more chemicals.")
        return flasks


def display_flasks(flasks, source_flasks, dest_flasks):
    """
    Displays the current state of all flasks, highlighting the source and destination flasks if specified.

    Args:
        flasks (list[BoundedStack]): The flasks to be displayed.
        source_flasks (int): The index of the flask chosen as the source for the current operation. None if no source flask is selected.
        dest_flasks (int): The index of the flask chosen as the destination for the current operation. None if no destination flask is selected.

    Returns:
        None
    """
    max_height = 4
    max_flasks_per_line = 4
    for line_start in range(0, len(flasks), max_flasks_per_line):
        for i in range(max_height, 0, -1):
            for j in range(line_start, min(line_start + max_flasks_per_line, len(flasks))):
                flask = flasks[j]
                if i <= flask.size():
                    flask_items_reversed = flask.reversed_items()
                    chemical = flask_items_reversed[flask.size() - i]
                    color = CHEMICALS_TO_COLORS.get(chemical, "")
                    print(f'|{color}{chemical}{ANSI_COLORS["RESET"]}|  ', end='')
                elif is_sealed(flask):
                    print('+--+  ', end='')
                else:
                    print('|  |  ', end='')
            print()
        print(('+--+' + '  ') * min(max_flasks_per_line, len(flasks) - line_start))

        for i in range(line_start, min(line_start + max_flasks_per_line, len(flasks))):
            if i == source_flasks:
                print(f'{ANSI_COLORS["RED"]} {(i + 1):^3}{ANSI_COLORS["RESET"]}', end='  ')
            elif i == dest_flasks:
                print(f'{ANSI_COLORS["GREEN"]} {(i + 1):^3}{ANSI_COLORS["RESET"]}', end='  ')
            else:
                print(f" {i + 1:^3}", end="  ")
        print()


def is_sealed(flask):
    """
    Determines if a flask is sealed, meaning it contains exactly the required units of the same chemical.

    Args:
        flask (BoundedStack): The flask to check.

    Returns:
        bool: True if the flask is sealed (contains exactly CHEMICAL_UNITS_PER_TYPE units of the same chemical), False otherwise.
    """
    if flask.size() < CHEMICAL_UNITS_PER_TYPE:
        return False
    return len(set(flask.items[-CHEMICAL_UNITS_PER_TYPE:])) == 1


def all_flasks_sealed(flasks):
    """
    Checks if all flasks in the game are sealed.

    Args:
        flasks (list[BoundedStack]): The list of flasks to be checked.

    Returns:
        bool: True if all flasks are sealed, False otherwise.
    """
    for flask in flasks:
        if CHEMICAL_UNITS_PER_TYPE > flask.size() > 0:
            return False
        if flask.size() >= CHEMICAL_UNITS_PER_TYPE and not is_sealed(flask):
            return False
    return True


def pouring(flasks, source_index, dest_index):
    """
    Attempts to pour the top chemical unit from the source flask into the destination flask.

    Args:
        flasks (list[BoundedStack]): The list of all flasks in the game.
        source_index (int): The index of the flask from which chemicals are to be poured.
        dest_index (int): The index of the flask into which chemicals are to be poured.

    Returns:
        bool: True if the pouring was successful, False otherwise. Pouring is unsuccessful if the source and destination are the same, the source is empty, or the destination is full or sealed.
    """
    source_flask = flasks[source_index]
    dest_flask = flasks[dest_index]

    if source_index == dest_index:
        error_message = "Source and destination flasks can't be the same."
    elif source_flask.isEmpty() or is_sealed(source_flask) or dest_flask.isFull() or is_sealed(dest_flask):
        error_message = "Can't pour from the selected flask."
    else:
        error_message = None

    if error_message is not None:
        print_at_position(0, 5, error_message, clear_line=True)
        return False

    chemical = source_flask.pop()
    dest_flask.push(chemical)
    return True


def print_at_position(x, y, text, clear_line=False):
    """
    Prints text at a specific position on the console, optionally clearing the line first.

    Args:
        x (int): The column number where the text starts.
        y (int): The row number where the text starts.
        text (str): The text to print.
        clear_line (bool): If True, clears the line before printing the text. Defaults to False.

    Returns:
        None
    """
    if clear_line:
        print(f"\033[{y};0H{ANSI_COLORS['CLEARLINE']}", end='')
    print(f"\033[{y};{x}H{text}", end='')


def get_user_input(prompt, valid_inputs, x, y):
    """
    Prompts the user for input, repeating until a valid response is given or the user chooses to exit.

    Args:
        prompt (str): The prompt message displayed to the user.
        valid_inputs (list[str]): A list of strings representing valid input values.
        x (int): The horizontal position (column) for the prompt.
        y (int): The vertical position (row) for the prompt.

    Returns:
        str: The user's input, guaranteed to be one of the valid inputs or 'EXIT' to quit the game.
    """
    while True:
        print_at_position(x, y, prompt + " ", clear_line=True)
        user_input = input().strip().upper()
        if user_input == "EXIT":
            exit()
        elif user_input in valid_inputs:
            print_at_position(0, 5, ANSI_COLORS['CLEARLINE'])
            return user_input
        else:
            print_at_position(0, 5, "Invalid Input. Try Again" + ANSI_COLORS['CLEARLINE'])


def main():
    """
    Main function to start and control the flow of the Chemical Flask Game.
    """
    clear_screen()

    file_name = input("Enter the name of the input file: ")
    flasks = read_input(file_name)

    valid_flask_numbers = [str(i) for i in range(1, len(flasks) + 1)]
    source_flasks = None
    dest_flasks = None

    while not all_flasks_sealed(flasks):
        clear_screen()
        print_at_position(0, 1, "Magical Flask Game")
        print_at_position(0, 6, "")
        display_flasks(flasks, source_flasks, dest_flasks)

        source_input = get_user_input("Select Source Flask:", valid_flask_numbers, 0, 3)
        if source_input.lower() == "exit":
            print("Exiting game.")
            return

        dest_input = get_user_input("Select Destination Flask:", valid_flask_numbers, 0, 4)
        if dest_input.lower() == "exit":
            print("Exiting game.")
            return

        source_index = int(source_input) - 1
        dest_index = int(dest_input) - 1

        operation_successful = pouring(flasks, source_index, dest_index)
        if operation_successful:
            source_flasks = source_index
            dest_flasks = dest_index

    if all_flasks_sealed(flasks):
        clear_screen()
        print_at_position(0, 1, "Magical Flask Game")
        print_at_position(0, 6, "")
        display_flasks(flasks, None, None)
        print_at_position(0, 5, "You win!", clear_line=True)


if __name__ == "__main__":
    main()
