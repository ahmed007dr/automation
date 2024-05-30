
import os
from PIL import Image

data_folder = input('enter data file : ')
logo_name = input('enter logo name : ')
save_location = input('enter save folder : ')

# Use full path for the logo image
logo_path = os.path.join(data_folder, logo_name)

try:
    # Open logo
    logo_img = Image.open(logo_path)
    logo_width, logo_height = logo_img.size

    # Create save directory
    os.makedirs(save_location, exist_ok=True)

    for file in os.listdir(data_folder):
        if not file.endswith(('.png', '.jpg', 'jpeg')):
            continue

        image_path = os.path.join(data_folder, file)
        image = Image.open(image_path)
        width, height = image.size

        image.paste(logo_img, (width - logo_width, height - logo_height), logo_img)
        image.save(os.path.join(save_location, file))
        print(f'Added logo to {file}')

except FileNotFoundError as e:
    print(f'Error: {e}')
except Exception as e:
    print(f'An unexpected error occurred: {e}')


