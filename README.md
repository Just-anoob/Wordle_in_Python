Here is how to use the code

from tabulate import tabulate
from wordle_functions import wordle, wordle_bot, word_picker
from random import choice


answer = word_picker()

board = [[" ", " ", " ", " ", " ", ], [ " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "] , [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "], [" ",  " ", " ", " ", " "]]


print(tabulate(board, tablefmt='fancy_grid'))
wordle(board, answer, 5)
