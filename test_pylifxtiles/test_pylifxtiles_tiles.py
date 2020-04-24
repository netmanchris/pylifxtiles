#import LIFxLAN object and get all LIFX lights and assign to lifx object
from lifxlan import LifxLAN
from unittest import TestCase
from unittest import mock
from nose.plugins.skip import SkipTest

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
class TestSingleTileFunctions(TestCase):
    """
    Test Case for pylifxtiles.tiles single matrix transformation functions
    """

    def test_single_tile_clockwise(self):
        target_tile = list(tiles.map_to_matrix(source_tile1, 8))
        for i in range(4):
            tiles.rotate90Clockwise(target_tile)
        target_tile = tiles.matrix_to_map(target_tile)
        self.assertEqual(source_tile1, target_tile)


    def test_single_tile_widdershins(self):
        target_tile = list(tiles.map_to_matrix(source_tile1, 8))
        for i in range(4):
            tiles.rotate90widdershins(target_tile)
        target_tile = tiles.matrix_to_map(target_tile)
        self.assertEqual(source_tile1, target_tile)

    def test_single_tile_shift_8_left(self):
        # convert to 2D 8x8 matrix
        target_tile = list(tiles.map_to_matrix(source_tile1, 8))
        target_tile = tiles.shift(target_tile, LEFT, 8)
        # convert back to 1D list
        target_tile = tiles.matrix_to_map(target_tile)
        # write back to source tile
        self.assertEqual(source_tile1, target_tile)








###Section to test multiple tile functions
class TestTwoTileFunctions(TestCase):
    """
    Test Case for pylifxtiles.tiles single matrix transformation functions
    """

    def test_shift_two_tile_16_left(self):
        #grab first 2 tiles from tilechain
        source_tiles = source_tilechain1[0:2]
        #convert to single 2D matrix
        target_tiles = tiles.combine_multiple_tiles(source_tiles)
        for i in range(16):
            target_tiles = tiles.shift(target_tiles, LEFT, 1)
        target_tiles = tiles.split_combined_matrix(target_tiles)
        self.assertEqual(source_tiles, target_tiles)

###Section to test multiple tile functions
class TestThreeTileFunctions(TestCase):
    """
    Test Case for pylifxtiles.tiles single matrix transformation functions
    """

    def test_shift_three_tile_24_left(self):
        #grab first 2 tiles from tilechain
        source_tiles = source_tilechain1[0:3]
        #convert to single 2D matrix
        target_tiles = tiles.combine_multiple_tiles(source_tiles)
        for i in range(24):
            target_tiles = tiles.shift(target_tiles, LEFT, 1)
        target_tiles = tiles.split_combined_matrix(target_tiles)
        self.assertEqual(source_tiles, target_tiles)

###Section to test multiple tile functions
class TestFourTileFunctions(TestCase):
    """
    Test Case for pylifxtiles.tiles single matrix transformation functions
    """

    def test_shift_four_tile_32_left(self):
        #grab first 2 tiles from tilechain
        source_tiles = source_tilechain1[0:4]
        #convert to single 2D matrix
        target_tiles = tiles.combine_multiple_tiles(source_tiles)
        for i in range(32):
            target_tiles = tiles.shift(target_tiles, LEFT, 1)
        target_tiles = tiles.split_combined_matrix(target_tiles)
        self.assertEqual(source_tiles, target_tiles)


###Section to test multiple tile functions
class TestFiveTileFunctions(TestCase):
    """
    Test Case for pylifxtiles.tiles single matrix transformation functions
    """

    def test_shift_five_tile_40_left(self):
        #convert to single 2D matrix
        target_tiles = tiles.combine_multiple_tiles(source_tilechain1)
        for i in range(40):
            target_tiles = tiles.shift(target_tiles, LEFT, 1)
        target_tiles = tiles.split_combined_matrix(target_tiles)
        self.assertEqual(source_tilechain1, target_tiles)