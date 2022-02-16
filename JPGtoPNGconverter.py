import sys
import os
from PIL import Image

# grab the first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if the  folder exist , if not create it
if not (os.path.exists(output_folder)):
    os.makedirs(output_folder)

# loop through the Pokedex folder
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]

    #convert jpg to png and save to a new folder
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print("all done!")