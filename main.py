from motor.SimLink import *

def main():
    
    camara = cm.Camara(position=[0, 0.1, 20], direction=[0, 0, 1])
    scene = sc.Scene(camara)
    
    motor  = SimLink(title = "Plano cartesiano", cam=camara, sce=scene)
    motor.init()

    circle = obj.Circle(color=[1, 0, 0], x=-3, y=0, radius = 1, fill=True) 

    rectangle = obj.Rectangle(color=[0, 1, 0], x=0, y=0, width=2, height=2, fill=True)
    line = obj.Line(color=[1, 1, 1], x1=-2, y1=1.5, x2=2, y2=1.5)
    triangle = obj.Triangle(color=[0, 0, 1], vertex=[[2, -1], [4, -1],[3, 1]], fill=True)
    hexagon = obj.RegularPolygon(color=[0, 1, 1], x=0, y=-3, apothem=1, sides=6, fill=True)
    
    f = lambda x: math.sin(x) 
    function = obj.Function(color=[1, 1, 1], function=f, x_min=-5, x_max=5, width=1.5, step=0.1) 
    
    scene.add(circle)
    scene.add(rectangle)
    scene.add(line)
    scene.add(triangle)
    scene.add(hexagon)
    scene.add(function)
    
    motor.render()
    
if __name__ == "__main__":
      main()
      
      
