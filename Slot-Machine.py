from lib.strings import *
from lib.game import *


def main():
    balance = first_balance = askBalance()

    clearTerminal()
    while True:
        if balance == first_balance:
            balance_color = 'Yellow'
        elif balance > first_balance:
            balance_color = 'Green'
        else:
            balance_color = 'Red'

        showText(
            f'Current balance is {colorsText(formatMoney(balance), balance_color)}', '~')
        askUserInfo('Press Enter to continue. ')

        bet_lines = askBetLine()
        bet_price_line = askBetMoney(balance)
        bet_price_total = bet_lines * bet_price_line

        all_lines = generateLines()
        print(
            f'You are betting {formatMoney(bet_price_line)} in {bet_lines} lines. Total = {formatMoney(bet_price_total)}')
        showLines(all_lines)
        bet_result = verifyBet(all_lines)
        if bet_result[0] == 0 or bet_result[0] != bet_lines:
            balance -= bet_price_total

            if balance <= 0:
                print(
                    f'You have {colorsText("NO MONEY", "Red")}. You need to add more!')
                balance = first_balance = askBalance()
            else:
                showText(
                    f'You Lost {colorsText(formatMoney(bet_price_total), "Red")} :(', '=')

        else:
            bonus = 0
            for each_symbol_line in bet_result[1:]:
                bonus += cfg.SYMBOLS[each_symbol_line]

            balance += (bet_price_total + bonus)
            showText(
                f'You Win {colorsText(formatMoney(bet_price_total), "Green")} + {colorsText(formatMoney(bonus), "Yellow")} :)', '=')


if __name__ == '__main__':
    main()
