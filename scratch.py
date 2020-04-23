
from pylifxtiles.tiles import *
from pylifxtiles import objects
from pylifxtiles.tiles import __shift

my_word = 'Hello'
target_tile = T1
original_colors = reset_tiles(target_tile)
target_color_map = original_colors
tile = 0
for letter in my_word.lower():
                blank_tile= actions.blank_tile()
                print (len(blank_tile))
                for led in alpha[letter]:
                    target_color_map[tile][led] = (dblue, 65535, fourty, 4900)
                target_tile.set_tile_colors(tile, target_color_map[tile], rapid=True)
                tile += 1


x = target_tile.get_tilechain_colors()
y = combine_multiple_tiles(x)

for i in range(40):
    #y = __shift(y, UP, 1)
    y = __shift(y, LEFT, 1)
    target_tile.set_tilechain_colors(split_combined_matrix(y), rapid=True)

for i in range(40):
    y = __shift(y, UP, 1)
    y = __shift(y, LEFT, 1)
    target_tile.set_tilechain_colors(split_combined_matrix(y))