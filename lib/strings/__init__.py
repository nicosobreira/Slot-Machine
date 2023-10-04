def errorMessage(message):
    '''Show a error message

    Args:
        message (str): what message to show
    '''
    message = 'ERROR!', message
    showText(colorsText(message, 'Red'))


def line(type='-', length=30):
    '''_summary_

    Args:
        type (str, optional): the type of the lines. Defaults to '-'.
        length (int, optional): the range of the line. Defaults to 30.
    '''
    print(type * length)


def showText(text, type='-', length=30):
    '''Show some text in a pretty way

    Args:
        text (str): what to print prettier
        type (str, optional): the type of the lines. Defaults to '-'.
        length (int, optional): the length of the lines and center. Defaults to 30.
    '''
    if len(text) >= length:
        custom_length = len(text) + 2
        line(type, custom_length)
        print(text.center(custom_length))
        line(type, custom_length)

    else:
        line(type, length)
        print(text.center(length))
        line(type, length)


def colorsText(text, color='Normal'):
    '''Print text with color

    Args:
        text (str): the txt that will be print
        color (str, optional): What color to you want? Defaults to 'Normal'.

        Types of colors:
            Normal, Green, Yellow, Red, Blue, Purple, Cyan or Gray

    Returns:
        str: colorized version of the text
    '''

    COLORS = {
        'Normal': '\033[m',
        'Green': '\033[32m',
        'Yellow': '\033[33m',
        'Red': '\033[31m',
        'Blue': '\033[34m',
        'Purple': '\033[35m',
        'Cyan': '\033[36m',
        'Gray': '\033[37m'
    }
    color = color.strip().capitalize()
    return f"{COLORS[color]}{text}{COLORS['Normal']}"


def formatMoney(money):
    '''Format money

    Args:
        money (float): the value to be format

    Returns:
        str: a better looking number
    '''
    
    str_money = f'{money:.2f}'
    str_money = str_money.replace('.', ',')
    return '$' + str_money


def clearTerminal():
    '''Clears the terminal
    '''

    from os import system, name

    if name == 'posix':  # For Unix/Linux/Mac
        system('clear')
    elif name == 'nt':  # For sistemas Windows
        system('cls')
    else:
        pass


def showTuple(tuple):
    '''_summary_

    Args:
        tuple (tuple): show the values in a tuple
    '''
    
    for elemento in tuple:
        print(f'{colorsText(elemento, "Blue")}', end='')
        if elemento == tuple[-1]:
            print()
        else:
            print(', ', end='')


def exitProgram():
    '''Exit the program
    '''

    from sys import exit

    clearTerminal()
    showText('Come back later!')
    exit()
