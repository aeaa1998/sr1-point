from Renderer import Render, GREEN, BLUE

bitmap = Render()
bitmap.glInit()
bitmap.glCreateWindow(200,200)
bitmap.glViewPort(50,50,100,100)
bitmap.glColor(50, 168, 82)
# bitmap.glVertex(0,0)
bitmap.glVertex(1,1)
bitmap.glVertex(-1,-1)

bitmap.glFinish()


