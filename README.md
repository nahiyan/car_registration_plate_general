# Install

It's best to create a virtual environment in this folder. Use python3 as the virtual environment's python.

Install packages using `pip install -r requirements.txt`.

# Usage

There are 2 directories: `raw_images` and `processed_images`.
Images which you want to process should be kept in `raw_images` directory.
To process them, run `python image_processor.py` and it should automatically detect the images in `raw_images` directory and store the processed images in `processed_images` directory.
