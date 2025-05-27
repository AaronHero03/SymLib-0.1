from motor.SymLib import *
import numpy as np

def main():
      camara = cm.Camara(position=[0, 0, 20], direction=[0, 0, 1])
      Scene = sc.Scene(camara)
      
      motor = SimLink(title="Movimiento Armonico", cam=camara, sce=Scene)
      motor.init()
      
      k = 10.0  # constante del resorte
      m = 1.0  # masa del objeto
      
      a = lambda t, x, v: -k* np.array(x)/m
      
      resultados = phy.runge_kutta2(a, 0, 10, [5 ,2,3], [0, 0, 0], 0.01)
      
      posiciones = [f1 for (_, _, f1, _) in resultados]
      
      esfera = obj3d.Sphere((0, 1, 0), 0.1, [0, 0, 0], wire=False)
      cubo = obj3d.Cube((1, 0, 0), 1, [1, 0, 0], wire=True)
      
      Scene.add(esfera)
      Scene.add(cubo)
      
      animacion1 = anim.Move(esfera, posiciones, duration=10)
      animacion2 = anim.Move(cubo, posiciones, duration=10, draw_trail=True)
#      Scene.add_animation(animacion1)
      Scene.add_animation(animacion2)
      
      motor.render()
      
if __name__ == "__main__":
      main()