from motor.SimLink import *

def main():
    
    camara = cm.Camara(position=[0, 0.1, 20], direction=[0, 0, 1])
    scene = sc.Scene(camara)
    
    motor  = SimLink(title = "Plano cartesiano", cam=camara, sce=scene)
    motor.init()
    
    # Ejemplo
    
    q = -1.602e-19; 
    m = 9.1e-31;    
    B = 0.1;        
    v0 = 1e6;       
    
    w = q * B / m;
    xi = 0;
    xf = 5 * math.pi/abs(w)
    
    fc = lambda t: (v0/w * math.sin(w*t), (v0/w * (1 - math.cos(w*t))))
    f = lambda x, y: x**2 + y**2 
    
    obj = obj3d.FunctionMesh((0, 0, 1), f, (-2, 2), (-2, 2), resolution=20, wire=True)
    
    sphere = obj3d.Sphere((0, 1, 0), 0.1, [0, 0, 0], wire=False)
    animation = anim.Animation(sphere, fc, xi, xf, 0, 1, scale=1e4, infinite=False)
    
    scene.add(sphere)
    scene.add_animation(animation)
    scene.add(obj)
    
    motor.render()
    
if __name__ == "__main__":
      main()
      
      
