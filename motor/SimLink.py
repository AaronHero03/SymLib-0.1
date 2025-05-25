from OpenGL.GL import *
from OpenGL.GLUT import *
import motor.Scene as sc
import motor.Camara as cm
import motor.Object2D as obj
import math
import motor.Object3D as obj3d
import motor.Animation as anim

class SimLink:
      
      def __init__(self, title, cam, sce, width=800, height=800, fps=60):
            self.camara = cam
            self.scene = sce
            self.width = width
            self.height = height
            self.fps = fps
            self.title = title.encode("utf-8")
            
      def init(self):
            glutInit()
            glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
            glutInitWindowSize(self.width, self.height)
      
      
      def render(self):
            glutCreateWindow(self.title)
            glEnable(GL_DEPTH_TEST)
            glClearColor(0.1, 0.1, 0.1, 1.0)
            glutDisplayFunc(self.scene.display)
            glutReshapeFunc(self.scene.reshape)
            glutMouseFunc(self.scene.mouse)
            glutMotionFunc(self.scene.motion)
            glutIdleFunc(self.scene.idle)
            glutMainLoop()
      
      