from OpenGL.GLU import *
from OpenGL.GLUT import *

class Camara:
      def __init__(self, position = [0, 0, 10], direction = [0, 0, 0], up= [0, 1, 0]):
            self.position = position
            self.direction = direction
            self.up = up
            
            self.mouse_down = False
            self.last_x = 0
            self.last_y = 0
            
      def apply(self):
            x, y, z = self.position
            dx, dy, dz = self.direction
            ux, uy, uz = self.up

            gluLookAt(x, y, z, dx, dy, dz, ux, uy, uz)
      
      # def mouse(self, button, state, x, y):
      #       if button == GLUT_LEFT_BUTTON:
      #             self.mouse_down = (state == GLUT_DOWN)
      #             self.last_x = x
      #             self.last_y = y
      
      # def mouse_rotation(self, x, y):
      #       if self.mouse_down:
      #             dx = x - self.last_x
      #             dy = y - self.last_y

      #             angle_z += dx * 0.5  # Rotar alrededor de Z con movimiento horizontal
      #             angle_y += dy * 0.5  # Rotar alrededor de Y con movimiento vertical

      #             self.last_x = x
      #             self.last_y = y
      #             glutPostRedisplay()
      