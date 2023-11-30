# Ethan Gueck
# This application will convert an image white to alpha.

from PIL import Image

def convert_to_transparent_alpha(input_image_path, output_image_path):
    with Image.open(input_image_path) as im:
        rgba_im = im.convert('RGBA')
        alpha_im = Image.new('RGBA', rgba_im.size, (0, 0, 0, 0))

        for x in range(rgba_im.width):
            for y in range(rgba_im.height):
                r, g, b, a = rgba_im.getpixel((x, y))

                # Make pixel transparent if white
                if r == 255 and g == 255 and b == 255:
                    alpha_im.putpixel((x, y), (r, g, b, 0))
                else:
                    alpha_im.putpixel((x, y), (r, g, b, a))

        # Save the new image with transparent background
        alpha_im.save(output_image_path)

# Example usage:
input_image_path = "" # Insert Path
#input_image_path = input_image_path.replace("\\", "\\\\")
output_image_path = '../OUTPUT_DOCS/IMG.png'
convert_to_transparent_alpha(input_image_path, output_image_path)