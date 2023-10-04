from lib.strings import *

#               Character Measurement
# ---------------------- - -----------------------
PAGES = (
    f"""Slot-Machine is a gabling game, {colorsText('play with responsibility!', 'Red')}
To start you have to put money on your {colorsText('balance', 'Blue')} then you bet a line and the {colorsText('price for this bet', 'Purple')}.
If you win you will {colorsText('receive', 'Green')}: {colorsText('the value per bet', 'Purple')} * the value of the symbol
But if you lost you will {colorsText('lose', 'Red')}: the value per bet * the value of a random symbol (in the line you bet)
If""",
    f"""    (page 2)Still Make """
)


def tutorial():
    showText(' - TUTORIAL -', '~', 50)
    current_page = 0

    while True:
        showPage(current_page)

        page_choice = askPage()
        match page_choice:

            case 'quit':
                clearTerminal()
                break

            case 'next':
                if 0 <= current_page + 1 < len(PAGES):
                    current_page += 1
                else:
                    errorMessage('This value must be slower')

            case 'previous':
                if 0 <= current_page - 1 <= len(PAGES):
                    current_page -= 1
                else:
                    errorMessage('This value must be bigger')


def askPage():
    '''Ask the user for a page

    Returns:
        str: what is the action that will be taken
    '''

    while True:
        print(f'Next Key: {colorsText("+", "Blue")}')
        print(f'Previous Key: {colorsText("-", "Blue")}')
        key_user = str(
            input(f'>>> What page? [{colorsText("q", "Blue")} to quit] '))

        match key_user:
            case '+':
                return 'next'
            case '-':
                return 'previous'
            case _:
                if key_user == 'q':
                    return 'quit'
                else:
                    errorMessage('Digit a feasible value')


def showPage(current_page):
    '''Show the current page

    Args:
        current_page (int): what is the page that will be shown
    '''

    page_long_str = PAGES[current_page]
    interval = 50
    broken_lines = []

    # Loop through the page_long_string and break it into lines
    for count_line in range(0, len(page_long_str), interval):
        line = page_long_str[count_line:count_line + interval]
        line = line + '_'
        broken_lines.append(line)

    # Join the broken_lines in page_format using '\n' as separator
    page_format = '\n'.join(broken_lines)
    print(page_format)
