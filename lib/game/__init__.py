from lib.strings import *

SYMBOLS = {
    'A': 2,
    'B': 3,
    'C': 5,
    'D': 7
}


def askBalance():
    '''Ask the user for balance

    Returns:
        float: the amount of money to gambling
    '''

    line('~', 35)
    print(
        f'Press {colorsText("Q", "Blue")} any time to {colorsText("quit", "Yellow")} the game')
    balance = askMoney('How much to you want to deposit? ')
    clearTerminal()

    return balance


def askBetLine():
    '''Ask how many lines will bet

    Returns:
<<<<<<< Updated upstream
        int: a number between 1 and 3, the bet
    '''

    while True:
        bet = askUserInfo('What would you like to bet on (1-3)? ')
=======
        int: a number between 1 and 3
    '''

    while True:
        bet = askUserInfo(f'The number of lines to bet (1-3)? ')
>>>>>>> Stashed changes
        try:
            int(bet)
        except:
            errorMessage('This valeu must be a integer')
        else:
            int_bet = int(bet)
<<<<<<< Updated upstream
            if int_bet not in range(1, 4):  # 1 -> 4 - 1 = 3
                errorMessage('This valeu must be in range 1-3')
=======
            if int_bet not in range(1, 4):
                errorMessage('This valeu must be in range (1-3)')
>>>>>>> Stashed changes
            else:
                return int_bet


def askUserInfo(question):
    '''Aks the user for some info

    Args:
        question (str): What message will prompt

    Returns:
        str: the answer from the user
    '''

    try:
        answer = str(input(question)).strip()
    except (KeyboardInterrupt):
        exitProgram()
    else:
        if answer in 'Qq' and answer != '':
            exitProgram()
        else:
            return answer


def askMoney(question):
    '''Ask the user for money

    Args:
        question (str): what is the message that will prompt

    Returns:
        float: the correspond value of money
    '''

    SYMBOLS_MONEY = ('R', '$')

    while True:
        money = askUserInfo(question)
        for character in money:
            if character in SYMBOLS_MONEY:
                money = money.replace(character, '')

        try:
            money = money.replace(',', '.')
            money_float = float(money)
        except ValueError:
            errorMessage('This valeu must be a float or integer')
        else:
            if 1 <= money_float <= 1000:
                return money_float
            else:
                errorMessage('This value must be in range (1 - 1000)')


def askBetMoney(maximum):
    '''Ask bet Money

    Args:
        maximum (int): the maximum value for the bet

    Returns:
        int: the money per bet
    '''
    while True:
        bet_money = askMoney('What would you like to bet for each line? ')
        if 1 <= bet_money <= maximum:
            return bet_money
        else:
            errorMessage(
                f'The bet must be in range [$1 - {formatMoney(maximum)}]')


def generateLines():
    '''Generates the lines for the game

    Returns:
        list: the whole symbols of the game
    '''

    from random import choice
    SYMBOLS_LIST = [key for key in SYMBOLS.keys()]
    all_lines = []

<<<<<<< Updated upstream
    for index in range(9):  # 0 -> 8
=======
    for index in range(10):  # 0 -> 12
>>>>>>> Stashed changes
        random_symbol = choice(SYMBOLS_LIST)
        all_lines.append(random_symbol)
    return all_lines


def showLines(lines_list):
    '''Show Lines from the result

    Args:
        lines_list (list): The current game to be show
    '''

    count = 0
    for column in range(3):
        for line in range(3):
            symbol = lines_list[count]
            print(symbol, end='')
            if line == 2:
                print()
            else:
                print(' | ', end='')
            count += 1


def verifyBet(all_lines):
    '''Verify the current bet result

    Args:
        all_lines (list): the current values of the game

    Returns:
        list: the result of the game (gain or lost money)
    '''

    bet_result = [[], [], [], 0]
    cont = 0
    for current_index in range(0, 9, 3):
        current_line = all_lines[current_index:current_index + 3]

        if all(symbol == current_line[0] for symbol in current_line):
            bet_result[-1] += 1
            bet_result[cont].append(current_line[0])
        cont += 1

    return bet_result
