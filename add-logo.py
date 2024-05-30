import os
from PIL import Image

def get_valid_path(prompt):
    path = input(prompt).strip()
    while not os.path.exists(path):
        print(f"Path does not exist: {path}")
        path = input(prompt).strip()
    return path

data_folder = get_valid_path('enter data file: ')
logo_name = input('enter logo name: ').strip()
save_location = input('enter save folder: ').strip()

# Construct full path for the logo image
logo_path = logo_name  # Assuming full path provided for logo_name

# Debug print statements
print(f"Data folder: {data_folder}")
print(f"Logo path: {logo_path}")
print(f"Save location: {save_location}")

try:
    # Open logo
    logo_img = Image.open(logo_path).convert("RGBA")
    logo_width, logo_height = logo_img.size

    # Create save directory
    os.makedirs(save_location, exist_ok=True)

    for file in os.listdir(data_folder):
        if not file.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue

        image_path = os.path.join(data_folder, file)
        image = Image.open(image_path).convert("RGBA")
        width, height = image.size

        # Create a new image for the output with an alpha layer (RGBA)
        composite = Image.new('RGBA', (width, height))
        composite.paste(image, (0, 0))

        # Paste the logo onto the image
        composite.paste(logo_img, (width - logo_width, height - logo_height), logo_img)

        # Convert back to RGB if saving as JPEG
        if file.lower().endswith(('.jpg', '.jpeg')):
            composite = composite.convert("RGB")
        
        # Save the image
        save_path = os.path.join(save_location, file)
        composite.save(save_path)
        print(f'Added logo to {file}')

except FileNotFoundError as e:
    print(f'Error: {e}')
except Exception as e:
    print(f'An unexpected error occurred: {e}')
