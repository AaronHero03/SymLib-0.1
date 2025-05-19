from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import motor.Scene as sc
import motor.Camara as cm

class SimLink:
      
      def __init__(self, title, width=800, height=800, fps=60):
            self.camara = cm.Camara(position=[0, 0.1, 20], direction=[0, 0, 1])
            self.scene = sc.Scene(self.camara)
            self.width = width
            self.height = height
            self.fps = fps
            self.title = title.encode("utf-8")
            
      def init(self):
            glutInit()
            glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
            glutInitWindowSize(self.width, self.height)
            glutCreateWindow(self.title)

            glEnable(GL_DEPTH_TEST)
            glClearColor(0.1, 0.1, 0.1, 1.0)

            glutDisplayFunc(self.scene.display)
            glutReshapeFunc(self.scene.reshape)
            glutMouseFunc(self.scene.mouse)
            glutMotionFunc(self.scene.motion)

            glutMainLoop()
      
      def add():
            pass
      
      def render():
            pass
      
      