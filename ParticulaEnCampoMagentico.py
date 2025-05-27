from motor.SymLib import *
import numpy as np

def main():
      camara = cm.Camara(position=[0, 0.1, 20], direction=[0, 0, 1])
      Scene = sc.Scene(camara)
      
      motor = SimLink(title="Campo Magnetico", cam=camara, sce=Scene)
      motor.init()
      
      q1 = -1
      q2 = 1
      b0 = 0.5
      m = 0.1
      
      v0 = np.array([5, 5,1], dtype=float)   # velocidad en Y
      B = np.array([0,  0, 1], dtype=float)   # campo en X
      r0 = np.array([0, 0, 0], dtype=float)   # origen
      
      a1 = lambda t, r, v: (q1 / m) * np.cross(v, B)
      a2 = lambda t, r, v: (q2 / m) * np.cross(v, B)
      
      resultados2 = phy.runge_kutta2(a1, 0, 5, [0, 5, 2], [2, 10, -1], 0.01)
      posiciones2 = [f1 for (_, _, f1, _) in resultados2]
      
      resultados1 = phy.runge_kutta2(a2, 0, 5, [0, 5, 2], [2, 10, -1], 0.01)
      posiciones1 = [f1 for (_, _, f1, _) in resultados1]
      
      esfera1 = obj3d.Sphere(radius=0.25, position=r0, color=[1, 0, 0])
      esfera2 = obj3d.Sphere(radius=0.25, position=[0, 5, 2], color=[1, 1, 1])
      
      Scene.add(esfera1)
      Scene.add(esfera2)
      
      animacion1 = anim.Move(esfera1, posiciones1, duration=5, draw_trail=True)
      animacion2 = anim.Move(esfera2, posiciones2, duration=5, draw_trail=True)
      Scene.add_animation(animacion1)
      Scene.add_animation(animacion2)
      
      motor.render()

if __name__ == "__main__":
      main()
