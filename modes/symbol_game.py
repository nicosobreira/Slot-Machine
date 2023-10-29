from lib.strings import *
from lib.game import *
import data.data as dt
import data.config as cfg


def perSymbolGame():
    showText(
        f'You are playing: {colorsText(randomColorText("Symbols Game"), style="Underline")}!')

    bet_symbol = askSymbolBet()
    bet_price_symbol = askMoney('How much you will bet per symbol? ')

    all_lines = generateLines()
    special_index = (cfg.LINES - 1) // 2
    bet_result = 0
    for symbol in all_lines[special_index]:
        bet_result += cfg.SYMBOLS[symbol]
    bet_result *= bet_price_symbol
    showSymbolGame(all_lines, special_index)
    if bet_symbol in all_lines[special_index]:
        dt.balance += bet_result
        showText(
            f'You Win {colorsText(formatMoney(bet_result), "Green")}', '=')
    else:
        dt.balance -= bet_result
        if dt.balance <= 0:
            dt.money_lost = dt.balance
            dt.balance = 0
        showText(
            f'You Lost {colorsText(formatMoney(bet_result), "Red")} :(', '=')


def showSymbolGame(all_lines, special_index):
    from random import choice

    random_color = choice(cfg.COLORS_LIST)
    for current_index, current_line in enumerate(all_lines):

        if current_index == special_index:
            for symbol in current_line:
                print('| ', end='')
                print(colorsText(symbol, random_color) + ' ', end='')
            print('| ', end='')

        else:
            for symbol in current_line:
                print(colorsText('| ', style='Dark'), end='')
                print(colorsText(symbol, style='Dark') + ' ', end='')
            print(colorsText('| ', style='Dark'), end='')
        print()


def askSymbolBet():
    while True:
        line('-', 30)
        for symbol, value in cfg.SYMBOLS.items():
            print(
                f'{colorsText(symbol, "Blue")} values {colorsText(formatMoney(value), "Green")}')
        line('-', 30)
        bet = askUserInfo('What symbol is your choose? ').upper()
        if bet in cfg.SYMBOLS.keys():
            return bet
        else:
            errorMessage('Choose a valid symbol')
