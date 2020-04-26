from pylifxtiles.alphanum import *
from pylifxtiles.colors import *


def write_word(word, color, tilechain):
    """
    Function to automatically
    :param word:
    :param tilechain:
    :return:
    """
    original_colors = reset_tiles(tilechain)
    for letter in word.lower():
        for led in alpha[letter]:
            original_colors[0][led] = (color, 65535, twenty, 4900)
    tilechain.set_tilechain_colors(original_colors, )

#function to reset the tiles to a blank/off state
def reset_tiles(my_tile):
    global original_colors
    original_colors = my_tile.get_tilechain_colors()
    for i in range(0,64):
        original_colors[0][i] = (0, 0, 0, 1500)
        original_colors[1][i] = (0, 0, 0, 1500)
        original_colors[2][i] = (0, 0, 0, 1500)
        original_colors[3][i] = (0, 0, 0, 1500)
        original_colors[4][i] = (0, 0, 0, 1500)
    my_tile.set_tilechain_colors(original_colors)
    return original_colors

def blank_tile():
    blank_tile = [0]*64
    for i in range(0,64):
        blank_tile[i] = (0, 0, 0, 1500)
    return blank_tile