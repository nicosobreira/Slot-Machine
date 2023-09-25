# Formatação - ~/Termpy/formatação/__init__.py


def errorMessage(message):
    showText(colors(message, 'Red'))



def line(type='-', range=30):
    print(type * range)


def showText(text='', type='-'):
    if len(text) >= 30:
        range = len(text.replace(' ', ''))
        line(type, range)
        print(text)
        line(type, range)

    else:
        range = 30
        line(type, range)
        print(text.center(30))
        line(type, range)


def colors(text, color):
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

    return f"{COLORS[color]}{text}{COLORS['Normal']}"


def clearTerminal():
    from os import system, name

    if name == 'posix':  # Para sistemas Unix/Linux/Mac
        system('clear')
    elif name == 'nt':  # Para sistemas Windows
        system('cls')
    else:
        pass


"""
def exibeTupla(tupla):
    for elemento in tupla:
        print(f'{colors(elemento, "Azul")}', end='')
        if elemento == tupla[-1]:
            print()
        else:
            print(', ', end='')
"""


def exitProgram():
    from sys import exit

    clearTerminal()
    showText('Volte Sempre!')
    exit()
