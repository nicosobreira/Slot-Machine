from lib.strings import *
from lib.game import *
import data.data as dt
import data.config as cfg


def perLineGame():
    showText(f'You are playing: {colorsText("Line Game", style="Underline")}!')

    bet_lines = askBetLine()
    bet_price_line = askBetMoney()
    bet_price_total = bet_lines * bet_price_line

    all_lines = generateLines()
    print(
        f'You are betting {formatMoney(bet_price_line)} in {bet_lines} lines. Total = {formatMoney(bet_price_total)}')
    showLineGame(all_lines)
    bet_result = verifyBet(all_lines)
    if bet_result[0] != bet_lines:
        dt.balance -= bet_price_total
        if dt.balance <= 0:
            dt.money_lost = dt.balance
            dt.balance = 0
        showText(
            f'You Lost {colorsText(formatMoney(bet_price_total), "Red")} :(', '=')

    else:
        bonus = 0
        for symbol_value in bet_result[1:]:
            bonus += cfg.SYMBOLS[symbol_value]
        dt.balance += (bet_price_total + bonus)

        showText(
            f'You Win {colorsText(formatMoney(bet_price_total), "Green")} + {colorsText(formatMoney(bonus), "Yellow")} :)', '=')


def askBetLine():
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


def askBetMoney():
    while True:
        bet_money = askMoney('What would you like to bet for each line? ')
        if 1 <= bet_money <= dt.balance:
            return bet_money
        else:
            errorMessage(
                f'The bet must be in range $1 - {formatMoney(dt.balance)}')


def showLineGame(all_lines):
    from random import choice

    for current_line in all_lines:
        random_color = choice(cfg.COLORS_LIST)
        for index, symbol in enumerate(current_line):
            print(colorsText(symbol, random_color), end='')
            if index != cfg.COLUMN - 1:
                print(colorsText(' | ', style='Dark'), end='')
            else:
                print()


def verifyBet(all_lines):
    bet_result = [0]
    for current_line_index in range(cfg.LINES):
        current_line = all_lines[current_line_index]
        if all(symbol == current_line[0] for symbol in current_line):
            bet_result[0] += 1
            bet_result.append(current_line[0])

    return bet_result
