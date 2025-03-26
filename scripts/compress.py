import os
from PIL import Image


def compress_and_convert_with_alpha(input_image_path, output_image_path, quality=80):
    # Open the image using Pillow
    with Image.open(input_image_path) as img:
        # Check if the image has an alpha channel (transparency)
        if img.mode == "RGBA":
            # Save the image with alpha channel for WebP
            img.save(output_image_path, format="WebP", quality=quality, lossless=True)
        else:
            # No alpha channel, proceed as normal
            img.save(output_image_path, format="WebP", quality=quality)


def batch_convert_to_webp(input_dir, output_dir, quality=80):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Loop through all files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(
            (".png", ".jpg", ".jpeg", ".bmp")
        ):  # You can add more formats here
            input_image_path = os.path.join(input_dir, filename)
            output_image_path = os.path.join(
                output_dir, f"{os.path.splitext(filename)[0]}.webp"
            )

            # Convert and compress the image
            compress_and_convert_with_alpha(
                input_image_path, output_image_path, quality
            )


# Example usage
batch_convert_to_webp("static/img_old", "static/images", quality=75)
