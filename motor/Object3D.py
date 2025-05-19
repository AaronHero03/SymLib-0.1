from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np

class Object3D():
      def __init__(self, color):
            self.color = (0, 0, 0)
            
      def draw(self):
            pass
      
class Sphere(Object3D):
      def __init__(self, color, radius, position, wire = False):
            super().__init__(color)
            self.color = color
            self.radius = radius
            self.position = position
            self.wire = wire
            
      def draw(self):
            glColor3f(self.color[0], self.color[1], self.color[2])    
            glPushMatrix()
            glTranslatef(self.position[0], self.position[1], self.position[2])
            if(self.wire == False):
                  glutSolidSphere(self.radius, 20, 20)
            else:
                  glutWireSphere(self.radius, 20, 20)
                  
            glPopMatrix()
            
             
class Cube(Object3D):
      def __init__(self, color, size, position, wire=False):
            super().__init__(color)
            self.color = color
            self.size = size
            self.position = position
            self.wire = wire
            
      def draw(self):
            glColor3f(self.color[0], self.color[1], self.color[2])    
            glPushMatrix()
            glTranslatef(self.position[0], self.position[1], self.position[2])
            if(self.wire == False):
                  glutSolidCube(self.size)
            else:
                  glutWireCube(self.size)

            glPopMatrix()

class FunctionMesh(Object3D):
      def __init__(self, color, func, x_range, y_range, resolution=20, wire=False):
            super().__init__(color)
            self.color = color
            self.func = func
            self.x_range = x_range
            self.y_range = y_range
            self.resolution = resolution
            self.wire = wire
            
            self.vertices, self.faces = self.generate_mesh()
            
      def generate_mesh(self):
            x_min, x_max = self.x_range
            y_min, y_max = self.y_range
            res = self.resolution
            
            # Crear malla de puntos (x, y)
            x_vals = np.linspace(x_min, x_max, res)
            y_vals = np.linspace(y_min, y_max, res)
            
            vertices = []
            for y in y_vals:
                  for x in x_vals:
                        z = self.func(x, y)
                        vertices.append([x, y, z])
            
            # Crear caras (como triángulos)
            faces = []
            for i in range(res - 1):
                  for j in range(res - 1):
                        idx = i * res + j
                        # Índices de los vértices del rectángulo actual
                        a = idx
                        b = idx + 1
                        c = idx + res
                        d = idx + res + 1
                        # Dos triángulos por celda
                        faces.append([a, b, d])
                        faces.append([a, d, c])
            
            return vertices, faces

      def draw(self):
            glColor3f(self.color[0], self.color[1], self.color[2])    
            glPushMatrix()
            
            glBegin(GL_LINES if self.wire else GL_TRIANGLES)
            for face in self.faces:
                  for vertex_idx in face:
                        vertex = self.vertices[vertex_idx]
                        glVertex3f(*vertex)
            glEnd()
            
            glPopMatrix()
