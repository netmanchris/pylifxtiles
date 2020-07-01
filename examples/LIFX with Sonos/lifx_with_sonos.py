import _thread as thread
import os
from lifxlan import LifxLAN
# from pylifxtiles import tiles
from pylifxtiles import actions
import soco
from soco.discovery import by_name
from time import sleep
import requests
from lifxlan.errors import WorkflowException
from lifxlan.tilechain import TileChain

my_speaker = 'SNS Bookshelves'
my_speaker_ip = '10.101.30.127'


def main():
    T1 = TileChain('d0:73:d5:39:47:95', '10.101.30.224')
    T2 = TileChain('d0:73:d5:3c:48:38', '10.101.30.223')
    T3 = TileChain('d0:73:d5:3c:55:df', '10.101.30.246')
    T4 = TileChain('d0:73:d5:3c:5f:e5', '10.101.30.212')
    T5 = TileChain('d0:73:d5:3c:4d:93', '10.101.30.211')
    T6 = TileChain('d0:73:d5:3d:fb:2d', '10.101.30.167')
    T7 = TileChain('d0:73:d5:3d:f6:06', '10.101.30.205')
    tc_list = [T2, T3, T4, T5, T6]
    current_album = None
    target_speaker = soco.SoCo(my_speaker_ip)
    last_track = None
    track_name = None
    try:
        while (True):
            if target_speaker == None:
                target_speaker = soco.SoCo(my_speaker_ip)
            if last_track == None:
                print("Last Track Path")
                last_track = target_speaker.get_current_track_info()['title']
            current_track = target_speaker.get_current_track_info()['title']
            if last_track == current_track:
                print("matching tracks path")
                sleep(5)
                continue
            else:
                print("new track path")
                last_track = current_track
                get_current_album_cover(target_speaker)
                actions.display_jpg_image(('album_cover.jpg'), (40, 40), tc_list)
                sleep(1)
                actions.display_jpg_image(('album_cover.jpg'), (40, 40), tc_list)
                sleep(1)
                actions.display_jpg_image(('album_cover.jpg'), (40, 40), tc_list)
                sleep(1)
                actions.display_jpg_image(('album_cover.jpg'), (40, 40), tc_list)
            sleep(1)
    except KeyboardInterrupt:
        print("Done.")
    except WorkflowException:
        main()


def get_current_album_cover(target_speaker):
    track_name = target_speaker.get_current_track_info()['title']
    try:
        source_image = requests.get(target_speaker.get_current_track_info()['album_art'])
        # print (source_image)
        file = open("album_cover.jpg", "wb")
        file.write(source_image.content)
        file.close()
        return target_speaker
    except:
        pass


if __name__ == "__main__":
    main()