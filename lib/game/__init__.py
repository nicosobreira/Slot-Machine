from lib.strings import *

SYMBOLS = {
    'A': 2,
    'B': 3,
    'C': 5,
    'D': 7
}


def askBetLine():
    '''Ask what line to bet

    Returns:
        int: a number between 1 and 3, the bet
    '''

    while True:
        bet = askUserInfo('What would you like to bet on (1-3)? ')
        try:
            int(bet)
        except:
            errorMessage('This valeu must be a integer')
        else:
            int_bet = int(bet)
            if int_bet not in range(1, 4):  # 1 -> 4 - 1 = 3
                errorMessage('This valeu must be in range 1-3')
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
        answer = str(input(question)).split()
    except (KeyboardInterrupt):
        exitProgram()
    else:
        if answer in 'Qq':
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
            float(money)
        except ValueError:
            errorMessage('This valeu must be a float or integer')
        else:
            return float(money)


def askBetMoney(maximum):
    '''Ask bet Money

    Args:
        maximum (int): the maximum value for the bet

    Returns:
        int: the money per bet
    '''
    while True:
        bet_money = askMoney('What would you like to bet for each line? ')
        if 0 < bet_money <= maximum:
            return bet_money
        else:
            errorMessage(
                f'The bet must be in range (0 - {formatMoney(maximum)})')


def generateLines():
    '''Generates the lines for the game

    Returns:
        list: the whole symbols of the game
    '''

    from random import choice
    SYMBOLS_LIST = [key for key in SYMBOLS.keys()]
    all_lines = []

    for index in range(9):  # 0 -> 8
        random_symbol = choice(SYMBOLS_LIST)
        all_lines.append(random_symbol)
    return all_lines


def showLines(lines_list):
    '''Show Lines from the result

    Args:
        lines_list (list): 
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
