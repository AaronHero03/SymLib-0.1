import numpy as np

def euler(f1, xi, xf, yi, h):
      
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
            f2 = f2 + h*f(x, f2)
            f1 = f1 + h*f2;
            x = x + h

            i = i + 1
            resultados.append((i, x, f1, f2))

      return resultados

def runge_kutta2(f, xi, xf, r0, v0, h):
      r = np.array(r0, dtype=float)
      v = np.array(v0, dtype=float)
      t = xi
      i = 0
      resultados = [(i, t, r, v)]

      while t < xf:
            k1v = f(t, r, v)
            k1r = v

            k2v = f(t + h/2, r + h/2 * k1r, v + h/2 * k1v)
            k2r = v + h/2 * k1v

            k3v = f(t + h/2, r + h/2 * k2r, v + h/2 * k2v)
            k3r = v + h/2 * k2v

            k4v = f(t + h, r + h * k3r, v + h * k3v)
            k4r = v + h * k3v

            v = v + (h / 6.0) * (k1v + 2*k2v + 2*k3v + k4v)
            r = r + (h / 6.0) * (k1r + 2*k2r + 2*k3r + k4r)


            t = t + h
            i += 1
            resultados.append((i, t, r, v))

      return resultados
