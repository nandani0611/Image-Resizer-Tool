import os
from PIL import Image

# === EDIT THESE ===
input_folder = 'input_images'
output_folder = 'output_images'
resize_to = (300, 300)  # target size: (width, height)
output_format = None     # None → keep original; use 'JPEG', 'PNG', etc. to convert
# ==================

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through each file in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
        in_path = os.path.join(input_folder, filename)
        with Image.open(in_path) as img:
            print(f"Processing {filename} (original: {img.size})")
            img_resized = img.resize(resize_to, Image.ANTIALIAS)

            # Set output filename and format
            base, _ = os.path.splitext(filename)
            fmt = output_format or img.format
            out_filename = f"{base}_{resize_to[0]}x{resize_to[1]}.{fmt.lower()}"
            out_path = os.path.join(output_folder, out_filename)

            img_resized.save(out_path, fmt)
            print(f"Saved → {out_filename}")

print("All done!")
