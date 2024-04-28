import os
import sys
import warnings
import Image
if sys.version_info[:2] >= (3, 2):
    warnings.simplefilter("ignore", ResourceWarning)
warnings.simplefilter("ignore", DeprecationWarning)

try:
    import png
except ImportError:
    png = None

def can_load(filename):
    return (80 if png is not None and os.path.splitext(filename)[1].lower() == ".png" else 0)

def can_save(filename):
    return can_load(filename)

if png is not None:
    def load(image, filename):
        reader = png.Reader(filename=filename)
        image.width, image.height, pixels, _ = reader.asRGBA8()
        image.pixels = Image.create_array(image.width, image.height)
        index = 0
        for row in pixels:
            for r, g, b, a in zip(row[::4], row[1::4], row[2::4], row[3::4]):
                image.pixels[index] = Image.color_for_argb(a, r, g, b)
                index += 1

    def save(image, filename):
        with open(filename, "wb") as file:
            writer = png.Writer(width=image.width, height=image.height, alpha=True)
            writer.write_array(file, list(_rgba_for_pixels(image.pixels)))

    def _rgba_for_pixels(pixels):
        for color in pixels:
            a, r, g, b = Image.argb_for_color(color)
            for component in (r, g, b, a):
                yield component