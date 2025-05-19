import time

class Animation:
      def __init__(self, object3d, path, xi, xf, z, duration, scale=1, infinite=False):
            self.object3d = object3d
            self.path = path
            self.xi = xi
            self.xf = xf
            self.z = z
            self.duration = duration
            self.start_time = time.time()
            self.scale = scale
            self.infinite = infinite

      def update(self):
            t =time.time() - self.start_time
            
            if self.infinite:
                  progress = (t % self.duration) / self.duration
            else:
                  progress = min(t/ self.duration, 1)
                  
            aux = self.xi + (self.xf - self.xi) * progress
            
            pos = self.path(aux)
            x = pos[0] * self.scale
            y = pos[1] * self.scale
            
            self.object3d.position[0] = x 
            self.object3d.position[1] = y 
            self.object3d.position[2] = self.z 

      
            