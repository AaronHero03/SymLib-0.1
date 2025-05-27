from motor.SymLib import *
import numpy as np

def main():
      camara = cm.Camara(position=[50, 0, 0], direction=[0, 0,0])
      Scene = sc.Scene(camara)
      
      motor = SimLink(title="Movimiento Armonico", cam=camara, sce=Scene)
      motor.init()
      
      g = np.array([0, 0, -9.81])  # aceleración de la gravedad
      v0 = [0, 0, 20]
      r0 = [0, 0, 10]  # posición inicial
      
      a = lambda t, x, v: g
      
      resultados = phy.runge_kutta2(a, 0, 5, r0, v0, 0.01)
      
      posiciones = [f1 for (_, _, f1, _) in resultados]
      
      esfera = obj3d.Sphere((0, 1, 0), 1, [0, 0, 0], wire=True)
      
      Scene.add(esfera)
      
      animacion1 = anim.Move(esfera, posiciones, duration=10)
      Scene.add_animation(animacion1)
      
      motor.render()
      
if __name__ == "__main__":
      main()