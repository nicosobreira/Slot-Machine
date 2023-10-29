OPTIONS = {
    'L': 'Line game',
    'S': 'Symbol game',
    'B': 'Add money to balance',
    'Q': 'Quit the game'
}

OPTIONS_LIST = [key for key in OPTIONS.keys()]


STYLE = {
    'None': 0,
    'Bold': 1,
    'Dark': 2,
    'Italic': 3,
    'Underline': 4,
    'Blink': 5,
    'Negative': 7,
    'Risk': 9
}

COLORS = {
    'Black': 0,
    'Red': 1,
    'Green': 2,
    'Orange': 3,
    'Yellow': 63,
    'Blue': 4,
    'Purple': 5,
    'Cyan': 6,
    'Gray': 7,
    'None': 9
}

COLORS_LIST = [key_color for key_color in COLORS.keys()]
COLORS_LIST.remove('Black')
COLORS_LIST.remove('Gray')


SYMBOLS = {
    'A': 2,
    'B': 3,
    'C': 5,
    'D': 7
}


LINES = 3
COLUMN = 3

TOTAL_SYMBOLS = COLUMN * LINES

MAXIMUM_MONEY = 1000
TYPE_MONEY = '$'
