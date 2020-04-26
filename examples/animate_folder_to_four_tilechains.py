# Main Program for Convert Single Image to Tiles

# Full running function with all dependencies
# imports RGB to HSBK conversion function from LIFX LAN library
import os
from lifxlan import LifxLAN
from lifxlan.utils import RGBtoHSBK
from pylifxtiles import tiles
from pylifxtiles import actions
from matplotlib import image
from PIL import Image

# modify this variable to the name of the specific LIFX Tilechain as shown in the LIFX app

source_folder = './images/supernova/'


def main():
    lan = LifxLAN()
    tilechain_lights = lan.get_tilechain_lights()
    print(len(tilechain_lights))
    if len(tilechain_lights) != 0:
        for tile in tilechain_lights:
            if tile.get_label() == 'T1':
                print(tile.get_label())
                T1 = tile
            if tile.get_label() == 'T2':
                print(tile.get_label())
                T2 = tile
            if tile.get_label() == 'T3':
                print(tile.get_label())
                T3 = tile
            if tile.get_label() == 'T4':
                print(tile.get_label())
                T4 = tile
    tc_list = [T1, T2, T3, T4]
    try:
        my_images = os.listdir(source_folder)
        my_images.sort()
        for walk in range(1):
            for i in my_images:
                display_image((source_folder + i), tc_list)
    except KeyboardInterrupt:
        print("Done.")


# combined function

# resize image and force a new shape and save to disk
def display_image(image_to_display, tilechain_list):
    # load the image
    my_image = Image.open(image_to_display)
    # report the size of the image
    # print(my_image.size)
    # resize image and ignore original aspect ratio
    img_resized = my_image.resize((40, 32))
    # changing the file extension from jpg to png changes output brightness. You might need to play with this.
    img_resized.save('./images/resized_image.jpg')
    data = image.imread('./images/resized_image.jpg')
    target_tcs = []
    for row in data:
        temp_row = []
        for pixel in row:
            temp_row.append(RGBtoHSBK(pixel))
        target_tcs.append(temp_row)
    tcsplit = tiles.split_tilechains(target_tcs)
    tilechain_list[0].set_tilechain_colors(tiles.split_combined_matrix(tcsplit[0]), rapid=True)
    tilechain_list[1].set_tilechain_colors(tiles.split_combined_matrix(tcsplit[1]), rapid=True)
    tilechain_list[2].set_tilechain_colors(tiles.split_combined_matrix(tcsplit[2]), rapid=True)
    tilechain_list[3].set_tilechain_colors(tiles.split_combined_matrix(tcsplit[3]), rapid=True)


if __name__ == "__main__":
    main()