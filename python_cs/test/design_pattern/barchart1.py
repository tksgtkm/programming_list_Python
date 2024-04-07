import abc
import os
import re
import tempfile
import Qtrack
from PIL import Image, ImageFilter

@Qtrack.has_methods("initialize", "draw_caption", "draw_bar", "finalize")
class BarRenderer(metaclass=abc.ABCMeta): pass