from lifxlan import *
from random import randint, choice, betavariate
from time import sleep
from lifxlan.device import WorkflowException
from pylifxtiles import actions
from pylifxtiles import colors
from pylifxtiles import objects

# Populate list with the name of the Tilechains
tc_target = ['T1', 'T2', 'T3', 'T4']
# variable used to select the top tilechain where the moon will be displayed
moon_tc = 'T1'  # selects tilechain where mooon will be displayed
moon_tile = 2.  # selects specific tile where moon will be displayed
tc_list = []


# tc1_name='T3'
# tc2_name = 'T4'
# target_tile1 = None
# target_tile2 = None
def main():
    global target_tile1, target_tile2
    lan = LifxLAN()
    tilechain_lights = lan.get_tilechain_lights()
    if len(tilechain_lights) != 0:
        for tile in tilechain_lights:
            if tile.get_label() in tc_target:
                tc_list.append(tile)
                print(tile.get_label() + ' found')
    duration_ms = 1000
    try:
        for tile in tc_list:
            original_colors = actions.reset_tiles(tile)
        run = 0
        while (True):
            for tile in tc_list:
                if tile.label == moon_tc:
                    objects.draw_moon(tile, moon_tile)  # used to ensure that the moon is in the same position
            my_tiles = [0, 1, 2, 3, 4]
            # twinkle_stars(target_tile1,0,3)
            # twinkle_stars(target_tile2,0,3)
            # for tile in tc_list:
            #   twinkle_stars(tile,choice(my_tiles),2)
            rand_tc = choice(tc_list)
            rand_tile = choice(my_tiles)
            if rand_tc.label == moon_tc and rand_tile == moon_tile:
                pass
            else:
                twinkle_stars(rand_tc, rand_tile, 2)

    except KeyboardInterrupt:
        print("Done.")
    except WorkflowException:
        print('Workflow Exception fire')
        generate_stars()


def generate_stars():
    try:
        for tile in tc_list:
            if tile.label == top_tc:
                objects.draw_moon(tile, 4)
                my_tiles = [0, 1, 2, 3, 4]
                # twinkle_stars(target_tile1,0,3)
                # twinkle_stars(target_tile2,0,3)
                # for tile in tc_list:
                #   twinkle_stars(tile,choice(my_tiles),2)
                rand_tc = choice(tc_list)
                rand_tile = choice(my_tiles)
                if rand_tc.label == 'T1' and rand_tile == 4:
                    pass
                else:
                    twinkle_stars(rand_tc, rand_tile, 2)
    except KeyboardInterrupt:
        print("Done.")
    except WorkflowException:
        print('Workflow Exception fire')
        generate_stars()


def random_stars(num_stars):
    star_pos = []
    for led in range(num_stars):
        star_pos.append(randint(0, 63))
    return star_pos


def twinkle_stars(tilechain, tile, num_stars):
    star_pos = random_stars(num_stars)
    twinkle_list = [colors.twenty, colors.thirty, colors.fourty]
    new_tile = actions.blank_tile()
    for cycle in range(5):
        for led in star_pos:
            new_tile[led] = (colors.yellow, 60000, choice(twinkle_list), 4900)
            tilechain.set_tile_colors(tile, new_tile, rapid=True)
            sleep(.05)


if __name__ == "__main__":
    main()