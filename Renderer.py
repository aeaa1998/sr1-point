import struct


# ===============================================================
# Utilities
# ===============================================================

def char(c):
    """
    Input: requires a size 1 string
    Output: 1 byte of the ascii encoded char
    """
    return struct.pack('=c', c.encode('ascii'))


def word(w):
    """
    Input: requires a number such that (-0x7fff - 1) <= number <= 0x7fff
           ie. (-32768, 32767)
    Output: 2 bytes
    Example:
    >>> struct.pack('=h', 1)
    b'\x01\x00'
    """
    return struct.pack('=h', w)


def dword(d):
    """
    Input: requires a number such that -2147483648 <= number <= 2147483647
    Output: 4 bytes
    Example:
    >>> struct.pack('=l', 1)
    b'\x01\x00\x00\x00'
    """
    return struct.pack('=l', d)

"Function that parses a color"
def color(r, g, b):
    return bytes([b, g, r])


# ===============================================================
# Constants
# ===============================================================

BLACK = color(0, 0, 0)
GREEN = color(50, 168, 82)
BLUE = color(50, 83, 168)
RED = color(168, 50, 60)
WHITE = color(255, 255, 255)



class ViewPort(object):

    def setSize(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height



# ===============================================================
# Renders a BMP file
# ===============================================================



class Render(object):
    def __init__(self):
        self.paintColor = WHITE
        self.bufferColor = BLACK


    def glInit(self):
        self.viewPort = ViewPort()

    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
        self.glClear()


    def glViewPort(self, x, y, width, height):
        self.viewPort.setSize(x, y, width, height)

    def glClear(self):
        self.framebuffer = [
            [self.bufferColor for x in range(self.width)]
            for y in range(self.height)
        ]

    def glFinish(self, filename='out.bmp'):
        f = open(filename, 'bw')

        # File header (14 bytes)
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(14 + 40))

        # Image header (40 bytes)
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        # Pixel data (width x height x 3 pixels)
        for x in range(self.height):
            for y in range(self.width):
                f.write(self.framebuffer[x][y])

        f.close()

    def display(self, filename='out.bmp'):
        self.glFinish(filename)

        try:
            from wand.image import Image
            from wand.display import display

            with Image(filename=filename) as image:
                display(image)
        except ImportError:
            pass  # do nothing if no wand is installed


    # Now glVertex is not the encharged to print he only normalizes the cordenates of a single point
    def glVertex(self, x, y):
        currentYCordinate =  self.viewPort.y + (self.viewPort.height/2) * (y + 1)
        currentXCordinate = self.viewPort.x + (self.viewPort.width/2) * (x + 1)
        self.point(currentXCordinate, currentYCordinate)

    def point(self, normalizedX, normalizedY):
        self.framebuffer[int(normalizedX)][int(normalizedY)] = self.paintColor

    def glClearColor(self, r, g, b):
        self.bufferColor = color(r,g,b)

    def glColor(self, r, g, b):
        self.paintColor= color(r,g,b)

    def line(self, start, end):
        x1, y1 = start
        x2, y2 = end
        y1 = self.viewPort.y + (self.viewPort.height / 2) * (y1 + 1)
        y2 = self.viewPort.y + (self.viewPort.height / 2) * (y2 + 1)
        x1 = self.viewPort.x + (self.viewPort.width / 2) * (x1 + 1)
        x2 = self.viewPort.x + (self.viewPort.width / 2) * (x2 + 1)

        dy = abs(y2 - y1)
        dx = abs(x2 - x1)
        steep = dy > dx

        if steep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2

        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        dy = abs(y2 - y1)
        dx = abs(x2 - x1)

        offset = 0
        threshold = dx

        y = y1
        for x in range(int(x1), int(x2) + 1):
            if steep:
                self.point(y, x)
            else:
                self.point(x, y)

            offset += dy * 2
            if offset >= threshold:
                y += 1 if y1 < y2 else -1
                threshold += dx * 2


