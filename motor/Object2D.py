from OpenGL.GL import *
import math

class Object2D:
      def __init__(self, color):
            self.color = color
      
      def  draw(self):
            pass
      
      def rotate(self, angle):
            # Implementar la rotación del polígono
            pass
      
      def translate(self, dx, dy):
            # Implementar la traslación del polígono
            pass
      
      def scale(self, sx, sy):
            # Implementar el escalado del polígono
            pass
      
      def set_color(self, color):
            # Implementar el cambio de color del polígono
            pass
      
      def set_position(self, x, y):
            # Implementar el cambio de posición del polígono
            pass
      
class Circle(Object2D):
      def __init__(self, color, x, y, radius, segments = 1000, fill = False, z0 = 0):
            super().__init__(color)
            self.color = color
            self.radius = radius
            self.x = x
            self.y = y
            self.segments = segments
            self.fill = fill
            self.z0 = z0
      
      def draw(self):
            glColor3f(self.color[0], self.color[1], self.color[2])    
            glDisable(GL_DEPTH_TEST)
            if self.fill == False :
                  glBegin(GL_LINE_LOOP)
            else:
                  glBegin(GL_TRIANGLE_FAN)
                  glVertex3f(self.x, self.y, self.z0)

            for i in range (self.segments+1):
                  angle = 2 * math.pi * i / self.segments
                  x = (self.radius * math.cos(angle)) + self.x
                  y = (self.radius * math.sin(angle)) + self.y
                  glVertex3f(x, y, self.z0)
            glEnd()
            glEnable(GL_DEPTH_TEST)
            
class Rectangle(Object2D):
      def __init__(self, color, x, y, width, height, fill = False):
            super().__init__(color)
            self.color = color
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.fill = fill
      
      def draw(self):
            glColor3f(self.color[0], self.color[1], self.color[2])    
            glDisable(GL_DEPTH_TEST)
            if self.fill == False :
                  glBegin(GL_LINE_LOOP)
            else:
                  glBegin(GL_QUADS)

            glVertex3f(self.x - (self.width/2), self.y - (self.height/2), 0)
            glVertex3f(self.x + (self.width/2), self.y - (self.height/2), 0)
            glVertex3f(self.x + (self.width/2), self.y + (self.height/2), 0)
            glVertex3f(self.x - (self.width/2), self.y + (self.height/2), 0)
            
            glEnd()
            
class Line(Object2D):
      def __init__(self, color, x1, y1, x2, y2):
            super().__init__(color)
            self.color = color
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2
      
      def draw(self):
            glColor3f(self.color[0], self.color[1], self.color[2])    
            glDisable(GL_DEPTH_TEST)
            glBegin(GL_LINES)
            glVertex3f(self.x1, self.y1, 0)
            glVertex3f(self.x2, self.y2, 0)
            glEnd()
            
            
class Triangle(Object2D):
      def __init__(self, color,vertex, fill = False):
            super().__init__(color)
            self.color = color
            self.x1 = vertex[0][0]
            self.y1 = vertex[0][1]
            self.x2 = vertex[1][0]
            self.y2 =  vertex[1][1]
            self.x3 = vertex[2][0]
            self.y3 = vertex[2][1]
            self.fill = fill
      
      def draw(self):
            glColor3f(self.color[0], self.color[1], self.color[2])    
            glDisable(GL_DEPTH_TEST)
            if self.fill == False :
                  glBegin(GL_LINE_LOOP)
            else:
                  glBegin(GL_TRIANGLES)
            glVertex3f(self.x1, self.y1, 0)
            glVertex3f(self.x2, self.y2, 0)
            glVertex3f(self.x3, self.y3, 0)
            glEnd()
            glEnable(GL_DEPTH_TEST)
            
class Polygon(Object2D):
      def __init__(self, color, vertex, fill = False):
            super().__init__(color)
            self.color = color
            self.vertex = vertex
            self.fill = fill
      
      def draw(self):
            glColor3f(self.color[0], self.color[1], self.color[2])    
            glDisable(GL_DEPTH_TEST)
            if self.fill == False :
                  glBegin(GL_LINE_LOOP)
            else:
                  glBegin(GL_POLYGON)

            for vertex in self.vertex:
                  glVertex3f(vertex[0], vertex[1], 0)
                  
            glEnd()
            glEnable(GL_DEPTH_TEST)
            
class RegularPolygon(Object2D):
      def __init__(self, color, x, y, apothem, sides, fill = False):
            super().__init__(color)
            self.color = color
            self.x = x
            self.y = y
            self.apothem = apothem
            self.sides = sides
            self.fill = fill
      
      def draw(self):
            glColor3f(self.color[0], self.color[1], self.color[2])    
            glDisable(GL_DEPTH_TEST)
            if self.fill == False :
                  glBegin(GL_LINE_LOOP)
            else:
                  glBegin(GL_POLYGON)

            radius = self.apothem / math.cos(math.pi / self.sides)

            for i in range (self.sides):
                  angle = 2 * math.pi * i / self.sides
                  x = (radius * math.cos(angle)) + self.x
                  y = (radius * math.sin(angle)) + self.y
                  glVertex3f(x, y, 0)
                  
            glEnd()
            glEnable(GL_DEPTH_TEST)
            
class Function(Object2D):
      def __init__(self, color, function, x_min, x_max, width = 1, step = 0.1):
            super().__init__(color)
            self.color = color
            self.function = function
            self.x_min = x_min
            self.x_max = x_max
            self.step = step
            self.width = width
      
      def draw(self):
            glColor3f(self.color[0], self.color[1], self.color[2])    
            glDisable(GL_DEPTH_TEST)
            glLineWidth(self.width)
            glBegin(GL_LINE_STRIP)

            x = self.x_min
            while x <= self.x_max:
                  y = self.function(x)
                  glVertex3f(x, y, 0)
                  x += self.step
            
            glEnd()
            glEnable(GL_DEPTH_TEST)
      