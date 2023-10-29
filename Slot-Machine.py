from lib.strings import *
from lib.game import askMoney, showBalance, askUserInfo
from modes.line_game import perLineGame
from modes.symbol_game import perSymbolGame
import data.data as dt
import data.config as cfg


def needsMoreMoney():
    while True:
        line('~', 30)
        print(
            f'You {colorsText("ran out", "Red", style="Bold")} of {colorsText("money", "Green", style="Bold")}')
        print(
            f'You need add more {colorsText(formatMoney(-dt.money_lost), "Yellow")}')
        line('~', 30)
        dt.first_balance = dt.balance = askMoney(
            f'Add more {colorsText("money", "Green", style="Bold")} or [{colorsText("CTRL + C", "Blue")}] to {colorsText("quit", "Red")}: ')
        dt.money_lost += dt.balance
        if dt.money_lost <= 0:
            line('>', 35)
            print(
                f'You {colorsText("need", "Red", style="Bold")} to add more money!')
            line('<', 35)
        else:
            clearTerminal()
            break


if __name__ == '__main__':
    showText(f'Welcome to {rainbowText("Slot-Machine")}!', length=39)
    print(f'Play with {colorsText("responsibility", style="Risk")} fun!')
    dt.first_balance = dt.balance = askMoney(
        'How much you will add to your balance? ')
    clearTerminal()
    while True:
        if dt.balance == 0:
            needsMoreMoney()
        for option, message in cfg.OPTIONS.items():
            print(colorsText(option, 'Blue'), '<->', randomColorText(message))

        showBalance()

        user_option = askUserInfo(
            f'Choose a option [Letters in {colorsText("blue", "Blue")}]: ').upper()

        if user_option not in cfg.OPTIONS_LIST:
            errorMessage('Chose a valid letter')
        else:
            clearTerminal()
            if user_option == 'L':
                perLineGame()
            elif user_option == 'S':
                perSymbolGame()
            elif user_option == 'B':
                dt.balance += askMoney('How much do you want to add? ')
                dt.first_balance = dt.balance
            elif user_option == 'Q':
                exitProgram()
