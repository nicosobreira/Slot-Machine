from lib.strings import *
from lib.game import *
from lib.tutorial import tutorial


SYMBOLS = {
    'A': 2,
    'B': 3,
    'C': 5,
    'D': 7
}


def menu():
    OPTIONS = (
        f'Bb - Put money on your {colorsText("balance", "Blue")}',
        f'Qq - {colorsText("Quit", "Blue")} the program'
    )
    for option in OPTIONS:
        print(option)

    action_user = askUserInfo('>>> ')
    if action_user in 'Qq':
        exitProgram()
    else:
        clearTerminal()



def main():
    menu()
    showText('Welcome to Slot-Machine! Have fun :)', '~')
    balance = askMoney('How much to you want to deposit? ')
    clearTerminal()
    while True:
        showText(f'Current balance is {formatMoney(balance)}', '~')
        askUserInfo('Press Enter to continue [q to quit]. ')

        bet_lines = askBetLine()
        bet_price_line = askBetMoney(balance)
        all_lines = generateLines()
        match bet_lines:
            case 1:
                current_line = all_lines[0:3]
            case 2:
                current_line = all_lines[3:6]
            case 3:
                current_line = all_lines[6:9]
        showLines(all_lines)
        result = all(symbol == current_line[0] for symbol in current_line)
        if result == True:
            showText('You won :)')
        else:
            showText('You lost :(')
        print(result)
        print()
        print(current_line)
        # clearTerminal()


if __name__ == '__main__':
    main()
