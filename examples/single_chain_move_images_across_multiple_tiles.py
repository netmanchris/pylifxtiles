

# Full running function with all dependencies
from lifxlan import LifxLAN
from lifxlan.device import WorkflowException
from pylifxtiles import actions
from pylifxtiles import objects
from pylifxtiles import tiles
from pylifxtiles.tiles import UP, DOWN, LEFT, RIGHT

# modify this variable to the name of the specific LIFX Tilechain as shown in the LIFX app
tilechain_name = 'T2'
target_tile = None


def main():
    global target_tile
    lan = LifxLAN()
    tilechain_lights = lan.get_tilechain_lights()
    print(len(tilechain_lights))
    if len(tilechain_lights) != 0:
        for tile in tilechain_lights:
            if tile.get_label() == tilechain_name:
                target_tile = tile
    duration_ms = 1000
    if target_tile:
        try:
            original_colors = actions.reset_tiles(target_tile)
            # objects.draw_youtube(target_tile,1)
            # objects.draw_heart(target_tile,2)
            run = 0
            while (True):
                objects.draw_heart(target_tile, 0)
                objects.draw_youtube(target_tile, 1)
                objects.draw_heart(target_tile, 2)
                objects.draw_youtube(target_tile, 3)
                objects.draw_heart(target_tile, 4)
                for i in range(16):
                    # step1 grab current state of both tiles

                    tile0 = target_tile.get_tile_colors(0)[0]
                    tile1 = target_tile.get_tile_colors(1)[0]
                    tile3 = target_tile.get_tile_colors(3)[0]
                    tile4 = target_tile.get_tile_colors(4)[0]

                    # step2 convert 1d 64 element list into 8x8 matrices
                    # tile1 = list(chunks(tile1,8)) #no longer required - built into combine_two_tiles functions
                    # tile2 = list(chunks(tile2,8)) #no longer required - built into combine_two_tiles functions
                    # step3 Combine into a single 8x16 matrix
                    combine01 = tiles.combine_two_tiles(tile0, tile1)
                    combine34 = tiles.combine_two_tiles(tile3, tile4)
                    # step4 shift matrix to the left
                    temp_matrix1 = tiles.shift(combine01, LEFT, 1)
                    temp_matrix2 = tiles.shift(combine34, RIGHT, 1)
                    # temp_matrix=__shift(combine2,UP, 2)
                    # temp_matrix=shift(combine2,LEFT, 1)
                    # step5 split back into 2 1x64 matrices
                    split_list01 = tiles.split_combined_matrix(combine01)
                    split_list34 = tiles.split_combined_matrix(combine34)
                    # write back to single variables
                    target_tile_color0 = split_list01[0]
                    target_tile_color1 = split_list01[1]
                    target_tile_color3 = split_list34[0]
                    target_tile_color4 = split_list34[1]
                    # write back to source tile
                    target_tile.set_tile_colors(0, target_tile_color0, rapid=True)
                    target_tile.set_tile_colors(1, target_tile_color1, rapid=True)
                    target_tile.set_tile_colors(3, target_tile_color3, rapid=True)
                    target_tile.set_tile_colors(4, target_tile_color4, rapid=True)
                    tiles.rotate_single_tile_image(target_tile, 2, 'widder', 1)
        except KeyboardInterrupt:
            print("Done.")
        except WorkflowException:
            print('Workflow Exception fire')
            move_images(target_tile)


# function to restart animation if WorkFlowException fires from main()

def move_images(tilechain):
    try:
        while (True):
            objects.draw_heart(target_tile, 0)
            objects.draw_youtube(target_tile, 1)
            objects.draw_heart(target_tile, 2)
            objects.draw_youtube(target_tile, 3)
            objects.draw_heart(target_tile, 4)

            for i in range(16):
                # step1 grab current state of both tiles

                tile0 = target_tile.get_tile_colors(0)[0]
                tile1 = target_tile.get_tile_colors(1)[0]
                tile3 = target_tile.get_tile_colors(3)[0]
                tile4 = target_tile.get_tile_colors(4)[0]

                # step2 convert 1d 64 element list into 8x8 matrices
                # tile1 = list(chunks(tile1,8)) #no longer required - built into combine_two_tiles functions
                # tile2 = list(chunks(tile2,8)) #no longer required - built into combine_two_tiles functions
                # step3 Combine into a single 8x16 matrix
                combine01 = tiles.combine_two_tiles(tile0, tile1)
                combine34 = tiles.combine_two_tiles(tile3, tile4)
                # step4 shift matrix to the left
                temp_matrix1 = tiles.shift(combine01, LEFT, 1)
                temp_matrix2 = tiles.shift(combine34, RIGHT, 1)
                # temp_matrix=__shift(combine2,UP, 2)
                # temp_matrix=shift(combine2,LEFT, 1)
                # step5 split back into 2 1x64 matrices
                split_list01 = tiles.split_combined_matrix(combine01)
                split_list34 = tiles.split_combined_matrix(combine34)
                # write back to single variables
                target_tile_color0 = split_list01[0]
                target_tile_color1 = split_list01[1]
                target_tile_color3 = split_list34[0]
                target_tile_color4 = split_list34[1]
                # write back to source tile
                target_tile.set_tile_colors(0, target_tile_color0, rapid=True)
                target_tile.set_tile_colors(1, target_tile_color1, rapid=True)
                target_tile.set_tile_colors(3, target_tile_color3, rapid=True)
                target_tile.set_tile_colors(4, target_tile_color4, rapid=True)
                tiles.rotate_single_tile_image(target_tile, 2, 'widder', 1)
    except KeyboardInterrupt:
        print("Done.")
    except WorkflowException:
        print('Workflow Exception fire')
        move_images(target_tile)


if __name__ == "__main__":
    main()