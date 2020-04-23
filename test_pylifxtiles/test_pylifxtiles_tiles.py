#import LIFxLAN object and get all LIFX lights and assign to lifx object
from lifxlan import LifxLAN
from constants import source_tile1, source_tilechain1
from pylifxtiles import tiles
from pylifxtiles.tiles import LEFT, RIGHT, UP, DOWN

'''
lifx = LifxLAN(30)
tilechain_lights = lifx.get_tilechain_lights()
len(tilechain_lights)
#Print out the list of LIFX Tile lights to find the one we're looking for
#TODO Should write a helper function that finds the right light and automatically assigns it to a variable
canvas = ['T1', 'T2', 'T3', 'T4']
for tile in tilechain_lights:
    if tile.get_label()  ==  'T1':
    #if tile.get_label() == 'TEST':
        T1 = tile
    if tile.get_label()  =='T2':
    #if tile.get_label() == 'TEST':
        T2 = tile
    if tile.get_label()  == 'T3':
    #if tile.get_label() == 'TEST':
        T3 = tile
    if tile.get_label()  == 'T4':
    #if tile.get_label() == 'TEST':
        T4 = tile
    if tile.get_label()  == 'LR1':
    #if tile.get_label() == 'TEST':
        LR = tile
test_tile = T2
'''

### Section to test single tile functions
def test_single_tile_clockwise(source_tile):
    target_tile  = list(tiles.map_to_matrix(source_tile, 8))
    for i in range(4):
        tiles.rotate90Clockwise(target_tile)
    target_tile = tiles.matrix_to_map(target_tile)
    print (source_tile == target_tile)

def test_single_tile_widdershins(source_tile):
    target_tile  = list(tiles.map_to_matrix(source_tile, 8))
    for i in range(4):
        tiles.rotate90widdershins(target_tile)
    target_tile = tiles.matrix_to_map(target_tile)
    print (source_tile == target_tile)

def test_single_tile_shift_8_left(source_tile):
    # convert to 2D 8x8 matrix
    target_tile = list(tiles.map_to_matrix(source_tile, 8))
    target_tile = tiles.__shift(target_tile, LEFT, 8)
    # convert back to 1D list
    target_tile = tiles.matrix_to_map(target_tile)
    # write back to source tile
    print(source_tile == target_tile)


test_single_tile_clockwise(source_tile1)
test_single_tile_widdershins(source_tile1)
test_single_tile_shift_8_left(source_tile1)

###Section to test multiple tile functions
