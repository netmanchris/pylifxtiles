#Functions used to manipulate tiles
from operator import add
from functools import reduce


## Transform Functions
#Functions used to transform Tile Color maps back and forth between various states

#Section deals with single Tile transform functions
#Function to convert 64 element list into 8x8 matrix
#https://chrisalbon.com/python/data_wrangling/break_list_into_chunks_of_equal_size/
def map_to_matrix(color_map, n=8):
    #constructor used to transform single tile color map list of 64 characters into an 8x8 matrix
    # tile_color_map = [0]*64
    # example usage: tile_color = list(map_to_matrix(tile_color_map,8))
    # For item i in a range that is a length of l,
    for i in range(0, len(color_map), n):
        # Create an index range for l of n items:
        yield color_map[i:i+n]

def matrix_to_map(matrix):
    color_map = reduce(add, matrix)
    return color_map

#Section deals with multiple tiles transform functions
#function to combine two tiles into a single 8x16 matrix. Used with matrix moving functions above.
def combine_multiple_tiles(list_of_tiles):
    '''
    Create a 8x(n*8) matrix where n is the number of tiles in a list of tiles
    :param list_of_tiles:
    :return:
    '''
    temp_list = []
    for tile_num in range(len(list_of_tiles)):
        temp_list.append(list(map_to_matrix(list_of_tiles[tile_num],8)))
    combined_tiles =[]
    for i in range(8):
        new_row=[]
        for tile in range(len(temp_list)):
            new_row = new_row + temp_list[tile][i]
        combined_tiles.append(new_row)
    return combined_tiles

def split_combined_matrix(combined_matrix):
    '''
    :param combined_matrix: Output of combine_multiple_tiles(). NxN matrix.
    :return:
    '''
    tile1=[]
    tile2=[]
    tile3=[]
    tile4=[]
    tile5=[]
    for i in combined_matrix:
        temp_list = list(map_to_matrix(i,8))
        if len(temp_list) == 2:
            tile1.append(temp_list[0])
            tile2.append(temp_list[1])
            tiles = [tile1, tile2]
        if len(temp_list) == 3:
            tile1.append(temp_list[0])
            tile2.append(temp_list[1])
            tile3.append(temp_list[2])
            tiles = [tile1, tile2, tile3]
        if len(temp_list) == 4:
            tile1.append(temp_list[0])
            tile2.append(temp_list[1])
            tile3.append(temp_list[2])
            tile4.append(temp_list[3])
            tiles = [tile1, tile2, tile3, tile4]
        if len(temp_list) == 5:
            tile1.append(temp_list[0])
            tile2.append(temp_list[1])
            tile3.append(temp_list[2])
            tile4.append(temp_list[3])
            tile5.append(temp_list[4])
            tiles = [tile1, tile2, tile3, tile4, tile5]
    tc_color_map=[]
    for tile in tiles:
        temp = matrix_to_map(tile)
        tc_color_map.append(temp)
    return tc_color_map

#functions to work with multiple tcs

def combine_tilechains(tilechain_list):
    '''
    Function which takes a tilechain_list as exported by combine_multiple_tiles()
    :param tilechain_list:
    :return:
    '''
    combined_tcs = []
    for i in tilechain_list:
        combined_tcs = [*combined_tcs,*i]
    return combined_tcs

def split_tilechains(combined_tilechain_list):
    '''
    Function which takes the output of combine_tilechain lists and splits into appropriate
    number of 8xn tilechains
    :param combined_tilechain_list:
    :return: list of single tilechain lists in 8*n matrix format
    '''
    list_of_tcs = []

    row = 0
    num_chains = len(combined_tilechain_list)//8
    for i in range(num_chains):
        tile = (combined_tilechain_list[(row):(row + 8)])
        row = row+8
        list_of_tcs.append(tile)
    return list_of_tcs






### older functions which I think can be removed

def combine_two_tiles(tile1, tile2):
    '''

    :param tile1: first tile color map
    :param tile2: second tile color map
    :return: return 8x16 matrix
    '''
    tile1 = list(map_to_matrix(tile1,8))
    tile2 = list(map_to_matrix(tile2,8))
    combined_tiles = []
    for i in range(8):
        new_row = tile1[i] + tile2[i]
        combined_tiles.append(new_row)
    return combined_tiles

def split_two_combined_matrix(combined_matrix):
    '''

    :param combined_matrix: combined 8x16 matrix typically output of
    combine_two_tiles function.
    :return: list which contains to 8x8 Tile Color Matrices
    '''
    tile1 = []
    tile2 = []
    for i in combined_matrix:
        temp_list = list(map_to_matrix(i,8))
        tile1.append(temp_list[0])
        tile2.append(temp_list[1])
    return [tile1, tile2]


#matrix operations

# Python3 program to rotate a matrix by 90 degrees
# https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/

# An Inplace function to rotate
# N x N matrix by 90 degrees in
# anti-clockwise direction
def rotate_single_tile_image(tilechain, tile_num, dir, num_rotate=1):
    '''
    param tilechain LIFXLAN Tilechain object which represent the specific tile your working with
    param tile_num Int which represents the tile you're working with
    param: tile_color_matrix 8x8 2D array which represents the colors map of a single LIFX tile
    param: num_rotate number of 1/2 turns that the matrix should be rotated

    '''
    # get current source tile matrix from tilechain
    tile_color = tilechain.get_tile_colors(tile_num)
    # convert to 2D 8x8 matrix
    temp_matrix = list(map_to_matrix(tile_color[0], 8))
    # rotate in place
    if dir == 'widder':
        for i in range(num_rotate):
            rotate90widdershins(temp_matrix)
    if dir == 'clock':
        for i in range(num_rotate):
            rotate90Clockwise(temp_matrix)
    # convert back to 1D list
    target_tile_color = matrix_to_map(temp_matrix)
    # write back to source tile
    tilechain.set_tile_colors(tile_num, target_tile_color)



def rotate90widdershins(mat, N=8):
    # Consider all squares one by one
    # Considers a square matrix where N is the length of a single side
    for x in range(0, int(N / 2)):

        # Consider elements in group
        # of 4 in current square
        for y in range(x, N - x - 1):
            # store current cell in temp variable
            temp = mat[x][y]
            # move values from right to top
            mat[x][y] = mat[y][N - 1 - x]
            # move values from bottom to right
            mat[y][N - 1 - x] = mat[N - 1 - x][N - 1 - y]
            # move values from left to bottom
            mat[N - 1 - x][N - 1 - y] = mat[N - 1 - y][x]
            # assign temp to left
            mat[N - 1 - y][x] = temp

def rotate90Clockwise(A):
    #https://www.geeksforgeeks.org/rotate-a-matrix-by-90-degree-in-clockwise-direction-without-using-any-extra-space/
    N = len(A[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp




#https://stackoverflow.com/questions/19878280/efficient-way-to-shift-2d-matrices-in-both-directions
NONE, UP, DOWN, LEFT, RIGHT = 'unshifted', 'up', 'down', 'left', 'right'

def shift(matrix, direction, dist):
    """ Shift a 2D matrix in-place the given distance of rows or columns in the
        specified (NONE, UP, DOWN, LEFT, RIGHT) direction and return it.
    """
    NONE, UP, DOWN, LEFT, RIGHT = 'unshifted', 'up', 'down', 'left', 'right'
    if dist and direction in (UP, DOWN, LEFT, RIGHT):
        n = 0
        if direction in (UP, DOWN):
            n = (dist % len(matrix) if direction == UP else -(dist % len(matrix)))
        elif direction in (LEFT, RIGHT):
            n = (dist % len(matrix[0]) if direction == LEFT else -(dist % len(matrix[0])))
            matrix[:] = list(zip(*matrix))  # Transpose rows and columns for shifting.

        h = matrix[:n]
        del matrix[:n]
        matrix.extend(h)

        if direction in (LEFT, RIGHT):
            matrix[:] = map(list, zip(*matrix))  # Undo previous transposition.

    return matrix


def shift_image(tilechain, tile_num, direction, dist):
    '''
    param tilechain LIFXLAN Tilechain object which represent the specific tile your working with
    param tile_num Int which represents the tile you're working with
    param: tile_color_matrix 8x8 2D array which represents the colors map of a single LIFX tile
    param: num_rotate number of 1/2 turns that the matrix should be rotated

    '''
    # get current source tile matrix from tilechain
    tile_color = tilechain.get_tile_colors(tile_num)
    # convert to 2D 8x8 matrix
    temp_matrix = list(map_to_matrix(tile_color[0], 8))
    # shift i
    temp_matrix = shift(temp_matrix, direction, dist)
    # convert back to 1D list
    target_tile_color = matrix_to_map(temp_matrix)
    # write back to source tile
    tilechain.set_tile_colors(tile_num, target_tile_color)


