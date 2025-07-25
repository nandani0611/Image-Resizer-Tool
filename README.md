# Image-Resizer-Tool
🖼️ Image Resizer Tool - Python Project
This Python script resizes all images in a folder and saves them to an output directory using the Pillow (PIL) library.

✅ Features
Resize multiple images in batch

Supports .jpg, .jpeg, .png, .bmp, .gif

Automatically creates the output folder

Easy to configure size and format

📁 Folder Structure
bash
Copy
Edit
image_resizer_project/
│
├── resize_images.py        # Python script
├── input_images/           # Put your original images here
└── output_images/          # Resized images will be saved here
🔧 Requirements
Python 3.x

Pillow library

Install Pillow with:

bash
Copy
Edit
pip install pillow
▶️ How to Use
Place your images inside the input_images/ folder.

Open terminal or VS Code terminal inside the project directory.

Run the script:

bash
Copy
Edit
python resize_images.py
Resized images will appear in the output_images/ folder.

How It Works
Reads all files from the input_images/ folder.

Resizes each image to a fixed size (default: 300x300).

Saves them in the output_images/ folder.

⚙️ Configuration
To change the target size, modify this line in resize_images.py:

python
Copy
Edit
resize_to = (300, 300)
You can also change the output format or add image format conversion features.
