from motor.SimLink import *
import numpy as np

def main():
      
      camara = cm.Camara(position=[0, 0.1, 20], direction=[0, 0, 1])
      Scene = sc.Scene(camara)
      
      motor  = SimLink(title = "Plano cartesiano", cam=camara, sce=Scene)
      motor.init()
      
      q = 1;
      v0 = 20; 
      b0 = 0.5;
      
      v = np.array([4, 5, 0], dtype=float)
      B = np.array([b0, 0, 0], dtype=float)
      r = np.array([1, 2, 0], dtype=float)
      
      m = 0.1;
      dt = 0.001;
      
      sphere = obj3d.Sphere(radius=.5, position=r, color=[1, 0, 0])
      Scene.add(sphere)
      
      for i in np.arange(0, 1.1, dt):
            F = q * np.cross(v, B)
            a = F / m
            
            v = v + a * dt
            r = r + v * dt
            sphere.moveTo(r)
            
      motor.render()
      
if __name__ == "__main__":
      main()
      
      