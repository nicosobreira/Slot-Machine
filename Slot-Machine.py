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
        if bet_result[-1] == 0:
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
            for each_list_line in bet_result[:3]:
                if len(each_list_line) == 0:
                    pass
                else:
                    bonus += SYMBOLS[each_list_line[0]]

            showText(
                f'You Win {colorsText(formatMoney(bet_price_total), "Green")} + {colorsText(formatMoney(bonus), "Yellow")} :)', '=')
            balance += (bet_price_total + bonus)


if __name__ == '__main__':
    main()
