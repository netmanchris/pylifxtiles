import requests
import json
import inflect
#create a file called secrets.py and place your googleAPI key in a var called youtube_api_key DO NOT POSTS THIS TO GITHUB
from secrets import youtube_api_key
from lifxlan import *
# from random import randint, betavariate
from time import sleep
from secrets import youtube_api_key
from pylifxtiles import actions
from pylifxtiles import objects
from pylifxtiles.alphanum import nums
from pylifxtiles import colors

channel_name = 'UCQHfJyIROQhDFUOJKVBiLog'
my_tile = 'T1'


def main():
    target_tilechain = my_tile
    lan = LifxLAN()
    tilechain_lights = lan.get_tilechain_lights()
    print(len(tilechain_lights))
    if len(tilechain_lights) != 0:
        for tile in tilechain_lights:
            if tile.get_label() == target_tilechain:
                print(tile.label)
                # if tile.get_label() == 'TEST':
                target_tilechain = tile

    duration_ms = 1000

    try:
        # original_colors = reset_tiles(T1)
        run = 0
        target_color_map = actions.reset_tiles(target_tilechain)
        original_colors = [actions.blank_tile()] * 5
        objects.draw_youtube(target_tilechain, 0)
        while (True):
            # T1.set_tile_colors(0,youtube,rapid=True)
            subs = get_subs(channel_name, youtube_api_key)
            tile = 1
            for number in subs:
                blank_tile = actions.blank_tile()
                print(number)
                for led in nums[number]:
                    target_color_map[tile][led] = (colors.dblue, 65535, colors.fourty, 4900)
                target_tilechain.set_tile_colors(tile, target_color_map[tile])
                print(tile)
                tile += 1
            run += 1
            print('This is run ' + str(run) + ' with ' + str(subs) + ' subscribers')
            # sleeps for 1/2h
            sleep(1200)


    except KeyboardInterrupt:
        print("Done.")
    else:
        print("No TileChain lights found.")


def get_subs(channel_name, api_key):
    num_of_subs = []
    data = requests.get(
        "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + channel_name + "&key=" + api_key)
    subs = data.json()['items'][0]['statistics']['subscriberCount']
    for i in subs:
        p = inflect.engine()
        num_of_subs.append(p.number_to_words(int(i)))
    return num_of_subs


if __name__ == "__main__":
    main()