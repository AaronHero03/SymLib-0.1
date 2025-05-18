from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import motor.Scene as sc

class SimLink:
      
      def __init__(self):
            self.scene = sc.Scene()
            self.width = 800
            self.height = 600
            self.fps = 60
            self.title = "Plano cartesiano 3D con cuadrícula XY".encode("utf-8")
            
      def init(self):
            glutInit()
            glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
            glutInitWindowSize(self.width, self.height)
            glutCreateWindow(self.title)

            glEnable(GL_DEPTH_TEST)
            glClearColor(0.1, 0.1, 0.1, 1.0)

            glutDisplayFunc(self.scene.display)
            glutReshapeFunc(self.scene.reshape)

            glutMainLoop()
      
      def add():
            pass
      
      def render():
            pass
      
      