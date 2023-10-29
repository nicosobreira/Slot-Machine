import data.config as cfg


def errorMessage(message):
    clearTerminal()
    message = f'ERROR! {message}'
    showText(colorsText(message, 'Red'))


def line(type='-', length=30):
    print(type * length)


def showText(text, type='-', length=30):
    line(type, length)
    print(text.center(length))
    line(type, length)


def colorsText(text, color='None', background='None', style='None'):
    '''Print text with color
    Colors:
        None; Green; Yellow; Red; Blue; Purple; Cyan; Gray
    Style:
        None; Bold; Dark; Italic; Underline; Blink; Negative; Risk
    '''
    color_code = f'\033[{cfg.STYLE[style]};{cfg.COLORS[color] + 30};{cfg.COLORS[background] + 40}m'
    return f'{color_code}{text}\033[m'


def randomColorText(text):
    from random import choice
    color = choice(cfg.COLORS_LIST)
    return colorsText(text, color)


def rainbowText(text):
    RAINBOW = ('Red', 'Yellow', 'Green', 'Blue', 'Cyan', 'Purple')
    format_text = ''
    count = 0

    for character in text:
        if character == ' ':
            format_text += ' '
        else:
            format_text += colorsText(character, RAINBOW[count])
            if count == 5:
                count = 0
            else:
                count += 1
    return format_text


def formatMoney(money):
    str_money = f'{money:.2f}'
    return cfg.TYPE_MONEY + str_money


def clearTerminal():
    from os import system, name

    if name == 'posix':  # For Unix/Linux/Mac
        system('clear')
    elif name == 'nt':  # For Windows
        system('cls')
    else:
        pass


def exitProgram():
    from sys import exit

    clearTerminal()
    showText('Come back later!')
    exit()
