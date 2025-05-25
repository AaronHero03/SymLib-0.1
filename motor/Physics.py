import math

def euler(f1, xi, xf, yi, h, ):
      
      y = yi
      x = xi
      i = 0;
      resultados = [(i, x, y)]
            
      while x < xf:
            y = y + h*f1(x, y)
            x = x + h

            i = i + 1
            resultados.append((i, x, y))

      return resultados

def runge_kutta(f1, xi, xf, yi, h):
      y = yi
      x = xi
      i = 0;
      resultados = [(i, x, y)]
            
      while x < xf:
            k1 = f1(x, y)
            k2 = f1(x + h/2, y + h/2 * k1)
            k3 = f1(x + h/2, y + h/2 * k2)
            k4 = f1(x + h, y + h * k3)

            y = y + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
            x = x + h

            i = i + 1
            resultados.append((i, x, y))

      return resultados

def euler2(f, xi, xf, f1i, f2i, h):
      
      f1 = f1i
      f2 = f2i
      x = xi
      i = 0;
      
      resultados = [(i, x, f1, f2)]
            
      while x < xf:
            f1 = f1 + h*f(x, f1)
            f2 = f2 + h*f1;
            x = x + h

            i = i + 1
            resultados.append((i, x, f1, f2))

      return resultados

def runge_kutta2(f, xi, xf, f1i, f2i, h):
      
      f1 = f1i
      f2 = f2i
      x = xi
      i = 0;
      
      resultados = [(i, x, f1, f2)]
            
      while x < xf:
            k1_2 = f(x, f1)
            k1_1 = k1_2
            
            k2_2 = f(x + h/2, f1 + h/2 * k1_2)
            k2_1 = x + h/2 * k1_1
            
            k3_2 = f(x + h/2, f1 + h/2 * k2_2)
            k3_1 = x + h/2 * k2_1
            
            k4_2 = f(x + h, f1 + h * k3_2)
            k4_1 = x + h * k3_1

            f2 = f2 + (h/6) * (k1_2 + 2*k2_2 + 2*k3_2 + k4_2)
            f1 = f1 + (h/6) * (k1_1 + 2*k2_1 + 2*k3_1 + k4_1)
            
            x = x + h
            i = i + 1
            
            resultados.append((i, x, f1, f2))

      return resultados