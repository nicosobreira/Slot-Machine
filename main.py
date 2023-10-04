from lib.strings import *
from lib.game import *
from data.tutorial import tutorial


def main():
    tutorial()
    showText('Welcome to Slot-Machine! Have fun :)', '~')
    balance = askMoney('How much to you want to deposit? ')
    clearTerminal()
    while True:
        showText(f'Current balance is {formatMoney(balance)}', '~')
        exitProgram('Press Enter to continue [q to quit]. ')

        bet_lines = askBetLine()
        bet_price_line = askBetMoney(balance)
        all_lines = generateLines()
        match bet_lines:
            case 1:
                current_line = all_lines[0:2]
            case 2:
                current_line = all_lines[3:5]
            case 3:
                current_line = all_lines[6:8]
        showLines(all_lines)
        result = all(symbol == current_line[0] for symbol in current_line)
        if result == True:
            showText('You won :)')
        else:
            showText('You lost :(')
        # clearTerminal()


if __name__ == '__main__':
    main()
