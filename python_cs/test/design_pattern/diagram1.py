import os
import sys
import tempfile

# def main():
#     if len(sys.argv) > 1 and sys.argv[1] == "-P":
#         create_diagram(DiagramFactory).save(sys.stdout)
#         create_diagram(SvgDiagramFactory).save(sys.stdout)
#         return
#     textFilename = os.path.join(tempfile.gettempdir(), "diagram.txt")
#     svgFilename = os.path.join(tempfile.gettempdir(), "diagram.svg")

#     txtDiagram = create_diagram(DiagramFactory)
#     txtDiagram.save(textFilename)
#     print("wrote", svgFilename)

#     svgDiagram = create_diagram(SvgDiagramFactory)
#     svgDiagram.save(svgFilename)
#     print("wrote", svgFilename)

class DiagramFactory:

    def make_diagram(self, width, height):
        return Diagram(width, height)
    
BLANK = " "
CORNER = "+"
HORIZONTAL = "-"
VERTICAL = "|"
    
def _create_rectangle(width, height, fill):
    rows = [[fill for _ in range(width)] for _ in range(height)]
    for x in range(1, width - 1):
        rows[0][x] = HORIZONTAL
        rows[height - 1][x] = HORIZONTAL
    for y in range(1, height - 1):
        rows[y][0] = VERTICAL
        rows[y][width - 1] = VERTICAL
    for y, x in ((0, 0), (0, width - 1), (height - 1, 0), (height - 1, width - 1)):
        rows[y][x] = CORNER
    return rows

class Rectangle:

    def __init__(self, x, y, width, height, fill, stroke):
        self.x = x
        self.y = y
        self.rows = _create_rectangle(width, height, BLANK if fill == "white" else "%")

class Text:

    def __init__(self, x, y, text, fontsize):
        self.x = x
        self.y = y
        self.rows = [list(text)]

