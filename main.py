from lib.strings import *


def main():
    balance = askMoney('How much to you want to deposit? ')
    showText(f'Current balance is ${formatMoney(balance)}', '~')
    continues = str(input('Press Enter to continue [q to quit]. '))
    if continues == 'q':
        exitProgram()
    while True:
        length_line = 0
        bet_lines = askBetLine()
        bet_price_line = askBetMoney(balance)   
        all_lines = generateLines()
        for cont in range(3):
            current_line = all_lines[length_line:length_line + 4]
            for element in current_line:
                for
            length_line += 4
        #print(all_lines[0:4])
        #print(all_lines[4:8])
        #print(all_lines[8:12])
        


def askBetLine():
    while True:
        bet = str(input('What would you like to bet on (1-4)? '))
        try:
            int(bet)
        except:
            errorMessage('ERROR! This valeu must be a integer')
        else:
            int_bet = int(bet)
            if int_bet not in range(1, 5):
                errorMessage('ERROR! This valeu must be in range 1-4')
            else:
                return int_bet


def askMoney(question):
    SYMBOLS_MONEY = ('R', '$')

    while True:
        money = str(input(question))
        for character in money:
            if character in SYMBOLS_MONEY:
                money = money.replace(character, '')

        try:
            money = money.replace(',', '.')
            float(money)
        except ValueError:
            errorMessage('ERROR! This valeu must be a float or integer')
        else:
            return float(money)


def askBetMoney(maximum):
    while True:
        bet_money = askMoney('What would you like to bet for each line? ')
        if bet_money <= maximum:
            return bet_money
        else:
            errorMessage(
                f'ERROR! The bet must be smaller then the balance ({formatMoney(maximum)})')


def generateLines():
    from random import choice
    SYMBOLS = ('A', 'B', 'C', 'D')
    all_lines = []
    
    for columns in range(0, 3):
        for line in range(0, 4):
            random_symbol = choice(SYMBOLS)
            all_lines.append(random_symbol)
            
            print(random_symbol, end='')
            if line == 3:
                print()
            else:
                print(' | ', end='')
    return all_lines


def formatMoney(money):
    str_money = f'{money:.2f}'
    str_money = str_money.replace('.', ',')
    return str_money


if __name__ == '__main__':
    main()
