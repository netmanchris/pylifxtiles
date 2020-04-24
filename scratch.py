
from pylifxtiles.tiles import *
from pylifxtiles import objects
from pylifxtiles.tiles import shift

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
    y = shift(y, LEFT, 1)
    target_tile.set_tilechain_colors(split_combined_matrix(y), rapid=True)

for i in range(40):
    y = shift(y, UP, 1)
    y = shift(y, LEFT, 1)
    target_tile.set_tilechain_colors(split_combined_matrix(y))




def test_split_matrix_brian(combined_matrix):
    #create empty list to hold tiles
    tiles = []
    #combined matrix is 8xn where n is divisible by 8
    tile_count = len(combined_matrix[0]//8)
    #columns = len(combined_matrix[0])
    for n in range(tile_count):
        #create new tile_list in tiles
        tile = []
        for r in range(8):
            col = n*8
            tile.append(combined_matrix[r][(col):(col+8)])
        tiles.append(tile)
        return tiles



#Another try
 #   https: // www.pythoncentral.io / how - to - slice - listsarrays - and -tuples - in -python /