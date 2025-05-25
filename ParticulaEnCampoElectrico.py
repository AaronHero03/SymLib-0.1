from motor.SimLink import *
import numpy as np

def main():
      camara = cm.Camara(position=[0, 0.1, 20], direction=[0, 0, 1])
      Scene = sc.Scene(camara)
      
      motor = SimLink(title="Plano cartesiano", cam=camara, sce=Scene)
      motor.init()
      
      q = 1
      b0 = 0.5
      m = 0.1
      
      v0 = np.array([0, 5, 0], dtype=float)   # velocidad en Y
      B = np.array([0,  0, 1], dtype=float)   # campo en X
      r0 = np.array([0, 0, 0], dtype=float)   # origen
      
      a = lambda t, v: (q / m) * np.cross(v, B)
      
      resultados = phy.runge_kutta2(a, 0, 5, r0, v0, 0.01)
      posiciones = [f1 for (_, _, f1, _) in resultados]
      
      resultados2 = phy.runge_kutta2(a, 0, 5, [0, 5, 2], [2, 10, 0], 0.01)
      posiciones2 = [f1 for (_, _, f1, _) in resultados2]
      
      
      esfera1 = obj3d.Sphere(radius=0.25, position=r0, color=[1, 0, 0])
      esfera2 = obj3d.Sphere(radius=0.25, position=[0, 5, 2], color=[1, 1, 1])
      
      Scene.add(esfera1)
      Scene.add(esfera2)
      
      animacion = anim.Move(esfera1, posiciones, duration=5)
      animacion2 = anim.Move(esfera2, posiciones2, duration=5)
      Scene.add_animation(animacion)
      Scene.add_animation(animacion2)
      
      motor.render()

if __name__ == "__main__":
      main()
