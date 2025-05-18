from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import motor.Camara as cm

class Scene:
      def __init__(self):
            self.camara = cm.Camara()
      
      def display(self):
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()

            self.camara.apply()

            glutSwapBuffers()
      
      def reshape(self, w, h):
            glViewport(0, 0, w, h)
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            gluPerspective(60, w / h, 0.1, 100.0)
            glMatrixMode(GL_MODELVIEW)      

      def idle():
            pass