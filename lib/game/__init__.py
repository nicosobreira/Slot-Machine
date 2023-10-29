from lib.strings import *
import data.data as dt
import data.config as cfg


def askUserInfo(question):
    try:
        answer = str(input(question)).strip()
    except (KeyboardInterrupt):
        exitProgram()
    else:
        return answer


def askMoney(question):
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


def showBalance():
    if dt.balance == dt.first_balance:
        balance_color = 'Yellow'
    elif dt.balance > dt.first_balance:
        balance_color = 'Green'
    else:
        balance_color = 'Red'

    showText(
        f'Current balance is {colorsText(formatMoney(dt.balance), balance_color)}', '~')


def generateLines():
    from random import choice

    SYMBOLS_LIST = [key for key in cfg.SYMBOLS.keys()]
    all_lines = [[] for _ in range(cfg.LINES)]

    for current_list in all_lines:
        for _ in range(cfg.COLUMN):
            current_list.append(choice(SYMBOLS_LIST))

    return all_lines
