import time

class Animation:
      def __init__(self, object3d, duration):
            self.object3d = object3d
            self.duration = duration
            self.start_time = time.time()
            
      def update(self):
            pass
            # t =time.time() - self.start_time
            
            # if self.infinite:
            #       progress = (t % self.duration) / self.duration
            # else:
            #       progress = min(t/ self.duration, 1)
                  
            # aux = self.xi + (self.xf - self.xi) * progress
            
            # pos = self.path(aux)
            # x = pos[0] * self.scale
            # y = pos[1] * self.scale
            
            # self.object3d.position[0] = x 
            # self.object3d.position[1] = y 
            # self.object3d.position[2] = self.z 


class Move(Animation):
      
      def __init__(self, object3d, posiciones, duration):
            super().__init__(object3d, duration)
            self.posiciones = posiciones
            self.totalFrames = len(posiciones)
            
      def update(self):
            elapsed_time = time.time() - self.start_time
            progress = elapsed_time / self.duration
            
            index = index = min(int(progress * self.totalFrames), self.totalFrames - 1)
            posicion_actual = self.posiciones[index]
            
            self.object3d.position[0] = posicion_actual[0]
            self.object3d.position[1] = posicion_actual[1]
            
            
            
            
      
