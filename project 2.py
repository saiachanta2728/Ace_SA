
import os
from PIL import Image
import rembg

# Input and output paths
input_path = "/Users/saiachanta/Desktop/pih_step08_elevation.jpg"
output_path = "result5.png"

# Check if input file exists
if os.path.exists(input_path):
    # Check if the file is readable
    if os.access(input_path, os.R_OK):
        # Open the input image
        input_image = Image.open(input_path)

        # Process the image
        output_image = rembg.remove(input_image)

        # Save the output image
        output_image.save(output_path)
        print("Background removed successfully!")
    else:
        print("Input file is not readable.")
else:
    print("Input file does not exist.")
    