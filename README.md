# Engine

## Requisitos

### Cámara

La cámara debe estar conectada con el mouse y controlar las coordenadas de posición y el vector de dirección.

- El ángulo de visión puede ser fijo por ahora.
- Ejemplo de estructura:

class Camara {
    atributos -> x, y, vectorDireccion

    x -> float  
    y -> float  
    vectorDireccion -> (i, j, k)
}
Implementación usando gluLookAt:

python
gluLookAt(0, 0, 10,     # Cámara en (0, 0, 10)
          0, 0, 0,      # Mira al origen (0, 0, 0)
          0, 1, 0)      # El eje Y es "arriba"
El vector arriba determina cuál es el “arriba” de la cámara.

Funciones básicas para manejar la cámara con el mouse:

python
def motion(x, y):
    # Lógica de movimiento de la cámara al detectar click con mouse
    glutPostRedisplay()  # Refresca la pantalla

def mouse(button, x, y):
    # Lógica para manejo del mouse
Motor
Clase principal que administra la inicialización y ejecución del motor.

Inicialización:
python
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800, 600)
glutCreateWindow("Plano cartesiano 3D con cuadrícula XY".encode("utf-8"))

glEnable(GL_DEPTH_TEST)
glClearColor(0.1, 0.1, 0.1, 1.0)

glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutMouseFunc(mouse)
glutMotionFunc(motion)
glutIdleFunc(idle)

glutMainLoop()
Funciones principales:
DisplayFunc: Dibuja el contenido de la ventana.

ReshapeFunc: Administra la proyección y el redimensionamiento de la ventana.

Métodos:
Init: Inicializa el motor.

Add: Agrega un objeto a la escena.

Render Scene: Ejecuta el renderizado de la escena.

SaveAnimation: Guarda la animación en formato de video (pendiente).

Escena
Clase responsable de crear y administrar la escena actual.

Aquí se agregan y animan los objetos.

Contiene las funciones DisplayFunc y ReshapeFunc.

Ejemplo de funciones:
python
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Cámara alejada y rotaciones
    glTranslatef(0, 0, zoom_distance)
    glRotatef(angle_y, 1, 0, 0)  # Rotación vertical
    glRotatef(angle_z, 0, 0, 1)  # Rotación horizontal

    glutSwapBuffers()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, w / h, 1.0, 100.0)
    glMatrixMode(GL_MODELVIEW)

def idle():
    # Lógica de animación de la escena
    glutPostRedisplay()
En OpenGL, la cámara no es un objeto propio. Las transformaciones para simular cámara afectan toda la escena.

Objeto2D
Clase base para crear objetos 2D (círculos, líneas, puntos, funciones, etc.)

Sirve como interfaz común para todos los objetos 2D.

Cada objeto implementa su método de dibujo.

Clases derivadas:

Circulo

Linea

Punto

Función

Objeto3D
Clase base para crear objetos 3D (esferas, planos, mallas, superficies, etc.)

Sirve como interfaz común para todos los objetos 3D.

Cada objeto implementa su método de dibujo.

Clases derivadas:

Esfera

Plano

Función

Cara

Cómo usar
Inicializa el motor.

Crea la escena y añade objetos.

Controla la cámara con el mouse.

Ejecuta el loop principal para renderizar y animar.
