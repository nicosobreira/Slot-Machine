from lib.strings import *
import config as cfg


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
        int: a number between 1 and config.line, the bet
    '''

    while True:
        bet = askUserInfo(
            f'How many lines do you think will bet? (1-{cfg.LINES})? ')
        try:
            int(bet)
        except:
            errorMessage('This valeu must be a integer')
        else:
            int_bet = int(bet)
            if int_bet not in range(1, cfg.LINES + 1):
                errorMessage(f'This value must be in range 1-{cfg.LINES}')
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

    while True:
        money = askUserInfo(question)
        for character in money:
            if character in cfg.TYPE_MONEY:
                money = money.replace(character, '')

        try:
            money = money.replace(',', '.')
            money_float = float(money)
        except ValueError:
            errorMessage('This valeu must be a float or integer')
        else:
            if 1 <= money_float <= cfg.MAXIMUM_MONEY:
                return money_float
            else:
                errorMessage(
                    f'The amount of money must be in {cfg.TYPE_MONEY}1 - {formatMoney(cfg.MAXIMUM_MONEY)})')


def askBetMoney(balance):
    '''Ask bet Money

    Args:
        maximum (int): the maximum value for the bet

    Returns:
        int: the money per bet
    '''
    while True:
        bet_money = askMoney('What would you like to bet for each line? ')
        if 1 <= bet_money <= balance:
            return bet_money
        else:
            errorMessage(
                f'The bet must be in range $1 - {formatMoney(balance)}')


def generateLines():
    '''Generates the lines for the game

    Returns:
        list: the whole symbols of the game
    '''

    from random import choice
    SYMBOLS_LIST = [key for key in cfg.SYMBOLS.keys()]
    all_lines = []

    for index in range(cfg.TOTAL_SYMBOLS):
        #random_symbol = choice(SYMBOLS_LIST)
        random_symbol = choice(SYMBOLS_LIST)
        all_lines.append(random_symbol)
    return all_lines


def showLines(lines_list):
    '''Show Lines from the result

    Args:
        lines_list (list): The current game to be show
    '''

    count = 0
    for line in range(cfg.LINES):
        for column in range(cfg.COLUMN):
            symbol = lines_list[count]
            print(symbol, end='')
            if column == cfg.COLUMN - 1:
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
    
    bet_result = [0]
    cont = 0
    for current_index in range(0, cfg.TOTAL_SYMBOLS, cfg.COLUMN):
        current_line = all_lines[current_index:current_index + cfg.COLUMN]
        if all(symbol == current_line[0] for symbol in current_line):
            bet_result[0] += 1
            bet_result.append(current_line[0])
        cont += 1

    return bet_result
