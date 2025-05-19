from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

class Camara:
      def __init__(self, position=[0, 0.1, 10], direction=[0, 0, 0], up=[0,  0, 1]):
            self.radius = math.dist(position, direction)
            self.theta = math.atan2(position[1] - direction[1], position[0] - direction[0])  # Horizontal angle
            self.phi = math.acos((position[2] - direction[2]) / self.radius)                # Vertical angle

            self.direction = direction
            self.up = up

            self.mouse_down = False
            self.last_x = 0
            self.last_y = 0

      def apply(self):
            # Convert spherical coordinates back to cartesian
            x = self.radius * math.sin(self.phi) * math.cos(self.theta) + self.direction[0]
            y = self.radius * math.sin(self.phi) * math.sin(self.theta) + self.direction[1]
            z = self.radius * math.cos(self.phi) + self.direction[2]

            gluLookAt(x, y, z,
                        self.direction[0], self.direction[1], self.direction[2],
                        self.up[0], self.up[1], self.up[2])

      def mouse(self, button, state, x, y):
            if button == GLUT_LEFT_BUTTON:
                  self.mouse_down = (state == GLUT_DOWN)
                  self.last_x = x
                  self.last_y = y    
            elif button == 3 and state == GLUT_DOWN:
                  self.radius -= 1  # o usa un valor más pequeño para control fino
                  self.radius = max(1, self.radius) 
                  
            # Scroll abajo (alejar)
            elif button == 4 and state == GLUT_DOWN:
                  self.radius += 1
                  

      def motion(self, x, y):
            if self.mouse_down:
                  dx = x - self.last_x
                  dy = y - self.last_y

                  # Sensibilidad
                  sensitivity = 0.005
                  self.theta -= dx * sensitivity
                  self.phi -= dy * sensitivity

                  # Limitar phi para evitar voltearse
                  epsilon = 0.01
                  self.phi = max(epsilon, min(math.pi - epsilon, self.phi))

                  self.last_x = x
                  self.last_y = y

                  glutPostRedisplay()
