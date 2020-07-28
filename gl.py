from Renderer import Render, GREEN, BLUE
from polygon import Polygon

bitmap = Render()
bitmap.glInit()
bitmap.glCreateWindow(500,500)
bitmap.glViewPort(0,0,420,420)
bitmap.glColor(50, 168, 82)
# bitmap.glVertex(0,1)
# bitmap.glVertex(1,1)
# bitmap.line(-1,0,1,0.2)
polyList = [(165, 380), (185, 360), (180, 330), (207, 345), (233, 330), (230, 360), (250, 380), (220, 385), (205, 410), (193, 383)]
poly = Polygon(polyList)
bitmap.drawLines(poly)
bitmap.glFinish()


