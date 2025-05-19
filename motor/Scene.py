from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import motor.Camara as cm

class Scene:
      def __init__(self, camara):
            self.camara = camara
      
      def draw_axes(self, length=5.0):
            glLineWidth(2.0)
            glBegin(GL_LINES)

            # X - rojo
            glColor3f(1, 0, 0)
            glVertex3f(-length, 0, 0)
            glVertex3f(length, 0, 0)
            
            # Y - verde
            glColor3f(0, 1, 0)
            glVertex3f(0, -length, 0)
            glVertex3f(0, length, 0)
            
            # Z - azul
            glColor3f(0, 0, 1)
            glVertex3f(0, 0, -length)
            glVertex3f(0, 0, length)
            
            glEnd()
     
      def draw_grid(self, size=10, step=1):
            glDisable(GL_LIGHTING)
            glColor3f(0.5, 0.5, 0.5)
            glLineWidth(1.0)
            glBegin(GL_LINES)
            for i in range(-size, size + 1, step):
                  glVertex3f(-size, i, 0)
                  glVertex3f(size, i, 0)
                  glVertex3f(i, -size, 0)
                  glVertex3f(i, size, 0)
            glEnd()

      def display(self):
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()

            self.camara.apply()
            
            self.draw_axes()
            self.draw_grid(round(self.camara.radius * 0.5))

            glutSwapBuffers()
      
      def reshape(self, w, h):
            glViewport(0, 0, w, h)
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            gluPerspective(60, w / h, 0.1, 100.0)
            glMatrixMode(GL_MODELVIEW)      

      def mouse(self, button, state, x, y):
            self.camara.mouse(button, state, x, y)
            glutPostRedisplay()
            
      def motion(self, x, y):
            self.camara.motion(x, y)
      
      def idle():
            pass