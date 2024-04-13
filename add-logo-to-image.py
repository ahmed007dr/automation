import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog

# Function to select a folder
def select_folder():
    folder_path = filedialog.askdirectory()
    return folder_path

# Function to select a file
def select_file():
    file_path = filedialog.askopenfilename()
    return file_path

# Initialize tkinter
root = tk.Tk()
root.withdraw()  # Hide the main window

# Select data folder
data_folder = select_folder()
if not data_folder:
    print("No folder selected. Exiting...")
    exit()

# Select logo image
logo_name = select_file()
if not logo_name:
    print("No logo selected. Exiting...")
    exit()

# Select save location
save_location = select_folder()
if not save_location:
    print("No save location selected. Exiting...")
    exit()

# Open logo
logo_image = Image.open(logo_name)
logo_width, logo_height = logo_image.size

# Create save location if it doesn't exist
os.makedirs(save_location, exist_ok=True)

# Iterate through files in data folder
for file in os.listdir(data_folder):
    if not file.endswith(('.jpg', '.png', '.jpeg', '.gif', '.webp')):
        continue

    image_path = os.path.join(data_folder, file)
    img = Image.open(image_path)
    width, height = img.size
    img.paste(logo_image, (width - logo_width, height - logo_height), logo_image)
    img.save(os.path.join(save_location, file))
    print(f'Added logo to {file}')

print("Process completed successfully.")
