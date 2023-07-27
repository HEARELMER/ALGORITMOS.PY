#hare un juego de una carrera de tortugas en python

import turtle
import random

w=turtle.Screen()
w.bgcolor('black')

#creamos las torugas

pepe=turtle.Turtle()
pepe.color('blue')
pepe.penup()
pepe.shape('turtle')
pepe.goto(-100,20)
pepe.penup()

pollo=turtle.Turtle()
pollo.color('red')
pollo.penup()
pollo.shape('turtle')
pollo.goto(-100,-30)
pollo.penup()

#varibles para las puntuaciones
puntos_pepe=0
puntos_pollo=0

#etiquetas apra msotar la puntuacion

tex_pepe=turtle.Turtle()
tex_pepe.penup()
tex_pepe.color('white')
tex_pepe.goto(150, 100)
tex_pepe.hideturtle()

tex_pollo=turtle.Turtle()
tex_pollo.penup()
tex_pollo.color('white')
tex_pollo.goto(150, -100)
tex_pollo.hideturtle()

#creamos funciones para mover las tortugas
def mover_pepe():
    global puntos_pepe
    distancia=random.randint(1,6)
    pepe.fd(distancia)
    puntos_pepe+=distancia
    mostrar_puntuacion()
    
def mover_pollo():
    global puntos_pollo
    distancia_p=random.randint(1,6)
    pollo.fd(distancia_p)
    puntos_pollo+=distancia_p
    mostrar_puntuacion()
    
#creamos una funcion para mostar la puntuacion
def mostrar_puntuacion():
    tex_pepe.clear()
    tex_pepe.write(f' Pepe: {puntos_pepe}', font=('Arial',12,'normal'))
    
    #para la segunda tortuga
    tex_pollo.clear()
    tex_pollo.write(f'Pollo: {puntos_pollo}', font=('Arial', 12,'normal'))
    
#mostar l apuntuacion final en pantalla
mostrar_puntuacion()

#eventos para mover las tortugs
w.onkey(mover_pepe, 'e')
w.onkey(mover_pollo, 'p')

w.listen()
w.mainloop()
