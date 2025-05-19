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
    
    heptagono = [
        [1.1481, 6.0],
        [0.5667, 7.0359],
        [-0.4450, 7.4709],
        [-1.3789, 6.8516],
        [-1.4957, 5.7119],
        [-0.7376, 4.8436],
        [0.3224, 5.0501]
    ]
    
    polygon = obj.Polygon(color=[1, 1, 0], vertex=heptagono, fill=True)
    
    scene.add(circle)
    scene.add(rectangle)
    scene.add(line)
    scene.add(triangle)
    scene.add(hexagon)
    scene.add(polygon)
    
    motor.render()
    
if __name__ == "__main__":
      main()
      
      
