from pylifxtiles.alphanum import *
from pylifxtiles.colors import *
from pylifxtiles import tiles
from matplotlib import image
from PIL import Image
from lifxlan.utils import RGBtoHSBK
from numpy import asarray

from PIL import GifImagePlugin


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


def display_jpg_image(image_to_display, image_size, tilechain_list):
    """
    Function which takes a jpg image and transforms to display over a ordered (top to bottom)
    set of LIFX tiles
    :param image_to_display: str of relative path to source jpg image
    :param image_size: tuple of len 2 - size of lifx tiles in Y by X quadrant example (40,56) would be
    7 5 tile tilechains on top of each other.
    :param tilechain_list: list of LIFX Tile objects top to bottom [T1, T2, T3]
    :return: None
    """
    # load the image
    my_image = Image.open(image_to_display)
    # report the size of the image
    # print(my_image.size)
    # resize image and ignore original aspect ratio
    img_resized = my_image.resize(image_size)
    # changing the file extension from jpg to png changes output brightness. You might need to play with this.
    data = asarray(img_resized)
    target_tcs = []
    for row in data:
        temp_row = []
        for pixel in row:
            temp_row.append(RGBtoHSBK(pixel))
        target_tcs.append(temp_row)
    # print ("length of target_tcs is " + str(len(target_tcs)))
    tcsplit = tiles.split_tilechains(target_tcs)
    # print ("legnth of tcssplit is " + str(len(tcsplit)))
    # print ("length tilelist is " + str(len(tilechain_list)))
    for tile in range(len(tilechain_list)):
        print(tile)
        tilechain_list[tile].set_tilechain_colors(tiles.split_combined_matrix(tcsplit[tile]), rapid=True)


def display_png_image(image_to_display, image_size, tilechain_list):
    """
    Function which takes a png image and transforms to display over a ordered (top to bottom)
    set of LIFX tiles
    :param image_to_display: str of relative path to source png image
    :param image_size: tuple of len 2 - size of lifx tiles in Y by X quadrant example (40,56) would be
    7 5 tile tilechains on top of each other.
    :param tilechain_list: list of LIFX Tile objects top to bottom [T1, T2, T3]
    :return: None
    """
    # load the image
    my_image = Image.open(image_to_display)
    # report the size of the image
    # print(my_image.size)
    # resize image and ignore original aspect ratio
    img_resized = my_image.resize(image_size)
    # changing the file extension from jpg to png changes output brightness. You might need to play with this.
    data = asarray(image)
    target_tcs = []
    for row in data:
        temp_row = []
        for pixel in row:
            temp_row.append(RGBtoHSBK(pixel))
        target_tcs.append(temp_row)
    # print ("length of target_tcs is " + str(len(target_tcs)))
    tcsplit = tiles.split_tilechains(target_tcs)
    # print ("legnth of tcssplit is " + str(len(tcsplit)))
    # print ("length tilelist is " + str(len(tilechain_list)))
    for tile in range(len(tilechain_list)):
        print(tile)
        tilechain_list[tile].set_tilechain_colors(tiles.split_combined_matrix(tcsplit[tile]), rapid=True)
