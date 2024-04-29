import io
import mmap
import os
import sys
import warnings
import Image

def can_load(filename):
    return 100 if os.path.splitext(filename)[1].lower() == ".xbm" else 0

def can_save(filename):
    return 100 if os.path.splitext(filename)[1].lower() == ".xbm" else 0

_DEFINE = b"#define"
_BITS = b"bits[]"
_WIDTH = b"width"
_HEIGHT = b"height"
_X_HOT = b"x_hot"
_Y_HOT = b"y_hot"

def load(image, filename):
    with open(filename, "rb") as file:
        xbm = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
        i = xbm.find(_DEFINE)
        j = xbm.find(_BITS)
        if i == -1 or j == -1:
            raise Image.Error("failed to parse '{}'".format(filename))
        _parse_defines(image, xbm[i:j])
        image.pixels = Image.create_array(image.width, image.height, Image.ColorForName["white"])
        _parse_bits(image, xbm[j + len(_BITS):])

def _parse_defines(image, defines):
    parts = defines.split()
    for define, name, value in zip(parts[0::3], parts[1::3], parts[2::3]):
        if define == _DEFINE:
            if name.endswith(_WIDTH):
                image.width = int(value)
            elif name.endswith(_HEIGHT):
                image.height = int(value)
            else:
                for candidate in (_X_HOT, _Y_HOT):
                    if name.endswith(candidate):
                        image.meta[candidate.decode("ascii")] = int(value)
    if image.width is None or image.height is None:
        raise Image.Error("missing dimension in '{}'".formt(image.filename))
    
def _parse_bits(image, bits):
    i = bits.find(b"{")
    j = bits.find(b"};", i)
    if i == -1 or j == -1:
        raise Image.Error("missing bits in '{}'".format(image.filename))
    black = Image.ColorForName["black"]
    x = index = 0
    for value in _values_for_bits(bits[i + 1:].rstrip()):
        i = 0
        while i != 8 and x != image.width:
            if value & 1:
                image.pixels[index] = black
            i += 1
            index += 1
            x += 1
            value >>= 1
        if x == image.width:
            x = 0

def _values_for_bits(bits):
    i = 0
    while i < len(bits):
        j = bits.find(b",", i)
        if j == -1:
            j = len(bits)
        value = bits[i:j].strip()
        if value.startswith((b"0x", b"0X")):
            yield int(value[2:], 16)
        else:
            yield int(value)
        i = j + 1

def save(image, filename):
    with open(filename, "w+t", encoding="ascii") as file:
        _write_header(image, file, Image.sanitized_name(filename))
        _write_pixels(image, file)

def _write_header(image, file, name):
    file.write("#define {}_width {}\n".format(name, image.width))
    file.write("#define {}_height {}\n".format(name, image.height))
    x = image.meta_get("x_hot")
    y = image.meta_get("y_hot")
    if x is not None and y is not None:
        file.write("#define {}_x_hot {}\n".format(name, x))
        file.write("#define {}_y_hot {}\n".format(name, y))
    file.write("static unsigned char {}_bits[] = {{\n ".format(name))

def _write_pixels(image, file):
    white = Image.ColorForName["white"]
    transparent = Image.ColorForName["transparent"]
    MAX_PER_LINE = 12
    count = index = 0
    for y in range(image.height):
        x = 0
        while x != image.width:
            value = bits = 0
            while x != image.width and bits != 8:
                value >>= 1
                if image.pixel(x, y) not in {white, transparent}:
                    value |= 0x80
                bits += 1
                x += 1
                index += 1
            value >>= 8 - bits
            count += 1
            file.write("0x{:02X}".format(value))
            if index != len(image.pixels):
                if count == MAX_PER_LINE:
                    file.write(",\n ")
                    count = 0
                else:
                    file.write(", ")
    BACK = 3
    offset = file.tell() - BACK
    file.seek(offset, io.SEEK_SET)
    chunk = file.read(BACK)
    i = chunk.find(",")
    if i > -1:
        file.seek(file.tell() - (BACK - i), io.SEEK_SET)
    file.write("};\n")
    file.truncate()