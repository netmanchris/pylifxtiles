#file which represents objects which can be drawn by this library
from pylifxtiles.colors import *
from pylifxtiles.alphanum import *
from pylifxtiles.actions import blank_tile


#youtube logo single tile

def draw_youtube(tilechain, tile):
    youtube = {
        'red': [0, 1, 2, 3, 4, 5, 6, 7, 8, 15, 16, 23, 24, 31, 32, 39, 40, 47, 48, 49, 50, 51, 52,
                53, 54, 55],
        'white': [19, 28, 35]
    }
    my_colors = [0] * 64
    for i in range(0, 64):
        my_colors[i] = (0, 0, 0, 1500)
    for led in youtube['red']:
        my_colors[led] = (0, 65535, sixty, 4900)
    for led in youtube['white']:
        my_colors[led] = (0, 0, ninety, 4900)
    tilechain.set_tile_colors(tile, my_colors)

#function to draw a single heart
def draw_heart(tilechain, tile):
    heart = {'red': [10, 12, 17, 19, 21, 24, 30, 33, 37, 42, 44, 51]}
    my_colors = [0] * 64
    for i in range(0, 64):
        my_colors[i] = (0, 0, 0, 1500)
    for led in heart['red']:
        my_colors[led] = (0, 65535, sixty, 4900)
    tilechain.set_tile_colors(tile, my_colors)


#function to draw a single moon
def draw_moon(tilechain, tile):
    moon = {'yellow': [11,12,18,29,20,21,26,27,28,29,35,36]}
    my_colors = [0] * 64
    for i in range(0, 64):
        my_colors[i] = (0, 0, 0, 1500)
    for led in moon['yellow']:
        my_colors[led] = (yellow, 65535, fourty, 4900)
    tilechain.set_tile_colors(tile, my_colors)


def draw_letter(tilechain, tile, letter):
    letter = alpha[letter]
    my_colors = actions.blank_tile()
    for led in letter:
        my_colors[led] = my_colors[led] = (colors.dblue, 65535, colors.fourty, 4900)
    tilechain.set_tile_colors(tile, my_colors)