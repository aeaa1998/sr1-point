from Renderer import Render, GREEN, BLUE
from polygon import Polygon

bitmap = Render()
bitmap.glInit()
bitmap.glCreateWindow(1000,500)
bitmap.glViewPort(30,30,800,800)
# bitmap.glColor(50, 168, 82)
# bitmap.glVertex(0,1)
# bitmap.glVertex(1,1)
# bitmap.line(-1,0,1,0.2)
# polyList = [(165, 380), (185, 360), (180, 330), (207, 345), (233, 330), (230, 360), (250, 380), (220, 385), (205, 410), (193, 383)]
# polyList2 = [(413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37), (660, 52),
# (750, 145), (761, 179), (672, 192), (659, 214), (615, 214), (632, 230), (580, 230),
# (597, 215), (552, 214), (517, 144), (466, 180)]
# poly = Polygon(polyList)
# poly2 = Polygon(polyList2)
# bitmap.drawLines(poly)
# bitmap.drawLines(poly2)
bitmap.load("./cube2.obj", (4, 3), (100, 100))
bitmap.glFinish()


