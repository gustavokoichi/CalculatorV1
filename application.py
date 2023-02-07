from util import *
from operations import *

MENU_DICT = {1: 'Sum', 2: 'Subtraction', 3: 'Multiply', 4: 'Division', 5: 'Power', 6: 'Factorial'}

menu(MENU_DICT)
option(int(input('Select an operation from menu: ')), MENU_DICT)