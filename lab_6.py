                                    # LABORATORIO 6 DE IS-182

#Condicionales

"""(1) Pídale al usuario que ingrese su nombre y luego pídale que ingrese su apellido. Únalos
con un espacio entre ellos y muestre el nombre y la longitud del nombre completo."""

def nombres_apellido(nombre,apellido):
    print(f"Su nombre es {nombre}, {apellido}")
    print("La longitud es de su nombre es: ", len(nombre)+len(apellido))

nombres_apellido("Pepito","Flores Huaman")


"""
(2) Solicite al usuario que ingrese su nombre y apellido en minúsculas. Cambie el caso al
caso del título y únalos. Mostrar el resultado final."""

def nombresyape_minuscula(nombre,apellido):
    print(nombre.upper(), apellido.upper())#upper se utiliza para converitr en mayuscula
    
print("Tus nombres y apellidos deben ingresar en minuscula...")
nombre=input("Ingrse tu nombre: ")
apellido=input("Ingrsea tu apellido: ")
#llamamos a la funcion
nombresyape_minuscula(nombre,apellido)
    

    

"""
(3) Pida al usuario que escriba la primera línea de una canción infantil y muestre la longitud
de la cadena. Solicite un número inicial y un número final y luego muestre solo esa sección
del texto (recuerde que Python comienza a contar desde 0 y no desde 1)."""
#la canción que escogí es LA VACA LECHERA
#Laprimera linea es: Tengo una vaca lechera

def linea_cancion(linea, num_ini, num_fin):
    print("Longitud de la cadena:", len(linea))
    print("Sección del texto:", linea[num_ini:num_fin])

linea = input("Escribe la primera línea de una canción infantil: ")
num_ini = int(input("Escribe el número inicial: "))

"""
(5) Pide dos números. Si el primero es mas grande que el segundo, muestre primero el
segundo número y luego el primero, de lo contrario, muestre primero el primer número y
luego el segundo.
"""
def pedir_numeros(num1,num2):
    if num1 > num2:
        print(num2, num1)
    else:
        print(num1, num2)
        
num1=int(input("Ingrse un número: "))
num2=int(input("Ingrse un número: "))
pedir_numeros(num1,num2)

"""(6) Pida al usuario que ingrese un número menor a 20. Si ingresa un número mayor a 20,
muestre el mensaje "Demasiado alto", de lo contrario, muestre "Gracias"."""

def numero_menor20(numero):
    if numero>20:
        print("Demasiado alto..")
    else:
        print("Gracias...")
        
numero=int(input("Ingrse un numero menor a 20 : "))
numero_menor20(numero)

"""(7) Pida al usuario que ingrese un número entre 10 y 20 (inclusivo). Si ingresa un número
dentro de este rango, muestra el mensaje “Gracias”, de lo contrario muestra el mensaje
“Respuesta incorrecta”."""

def num_entre_10_20(num):
    if num>=10 and num<=20:
        print("Gracias...") 
    else:
        print("Respuesta incorrecta..")
        
num=int(input("Ingrse un numero entre 10 y 20 (incluido): "))
num_entre_10_20(num)

"""(8) Pida al usuario que introduzca su color favorito. Si ingresan “rojo”, “ROJO” o “Rojo”
mostrar el mensaje “También me gusta el rojo”, de lo contrario mostrar el mensaje “No me
gusta [color], prefiero el rojo”."""

def color_favorito(color):
    if color=="rojo" or color=="Rojo" or color=="ROJO":
        print(f"A mi tambien me gusta el color {color}")
    else:
        print(f"No me gusta {color}, prefiero el rojo")

color=input("Ingrese su color favorito: ")
color_favorito(color)

"""(9) Pregunta al usuario si está lloviendo y convierte su respuesta a minúsculas para que no
importe en qué caso lo escriba. Si responde "sí", pregunta si hace viento. Si responde “sí”
a esta segunda pregunta, muestre la respuesta “Hace demasiado viento para un
paraguas”, de lo contrario muestre el mensaje “Tome un paraguas”. Si no respondieron
que sí a la primera pregunta, mostrar la respuesta “Disfruta tu día”."""

pregunta=input("¿ Está lloviendo ?: ")
respuesta=pregunta.lower().strip()

if respuesta=="si":
    pregunta=input("¿ Hace viento ?: ")
    if pregunta=="si":
        print("Hace demasiado viento para un paraguas")
    else:
        print("Tome paraguas")

else:
    print("Disfruta tu día")

"""(10) Preguntar la edad del usuario. Si tienen 18 años o más mostrar el mensaje “Puedes
votar”, si tienen 17 años mostrar el mensaje “Puedes aprender a conducir”, si tienen 16
años mostrar el mensaje “Puedes comprar un billete de lotería”, si son menores de 16
años, mostrar el mensaje "Puedes ir a Trickor-Treating"."""

edad=int(input("¿Cual es tu edad?: "))

if edad >=18:
    print("Puedes votar.")
elif edad==17:
    print("Puedes aprendr a conducir")

elif edad==16:
    print("Puedes comprar un billete de lotería")

elif edad<16:
    print("Puedes ir a Trickor-Treating")

"""(11) Pídele al usuario que ingrese 1, 2 o 3. Si ingresa un 1, muestra el mensaje "Gracias",
si ingresa un 2, muestra "Bien hecho", si ingresa un 3, muestra "Correcto". Si ingresan algo
más, muestra "Mensaje de error"."""

numero=int(input("Ingresa el número 1,2 o 3: "))
if numero ==1:
    print("Gracias")
elif numero==2:
    print("Bien hecho")
elif numero==3:
    print("Correcto")

"""(12) Pida al usuario que introduzca un número. Si es inferior a 10, muestra el mensaje
"Demasiado bajo", si su número está entre 10 y 20, muestra "Correcto", de lo contrario,
muestra "Demasiado alto"."""

numero=int(input("Ingresa un número: "))

if numero<10:
    print("Demasiado bajo")
elif numero>10 and numero <=20:
    print("Correcto")
else:
    print("Demasiado alto")

"""(13) Escriba un código que le pida al usuario que ingrese una puntuación numérica (0-
100). En respuesta, debe imprimir el puntaje y la letra de calificación correspondiente, de
acuerdo con la tabla a continuación."""

puntuacion=int(input("Ingresa una puntuación (0-100): "))

if puntuacion >=90 and puntuacion <=100:
    print( puntuacion, "A")

elif puntuacion>=80 and puntuacion<90:
    print(puntuacion, "B")

elif puntuacion >=70 and puntuacion<80:
    print(puntuacion, "C")

elif  puntuacion >=60 and puntuacion <70:
    print(puntuacion, "D")

elif puntuacion<60:
    print(puntuacion, "F")


"""(14) Un año es bisiesto si es divisible por 4; sin embargo, si el año puede dividirse por
100, NO es un año bisiesto, a menos que el año también sea divisible por 400, entonces
es un año bisiesto. Escriba un código que le pida al usuario que ingrese un año y genere
True si es un año bisiesto, o False en caso contrario. Usar sentencias if.
Año ¿Salto?"""

def año_bisiesto(año):
    if año%4==0 and (año %400==0 or año%100!=0 ):
        print(bool)
    else:
        print(False)
    
año_bisiesto(1900)

"""(15) Proporcione los opuestos lógicos de estas condiciones, es decir, una expresión que
produzca Falso siempre que esta expresión produzca Verdadero, y viceversa. No se le
permite utilizar el operador not.
1. a > b
2. a >= b
3. a >= 18 and día == 3
4. a >= 18 or día != 3"""

a=13
b=10
dia=23

print(a>b)
print(a<=b)#opuesto logico

print(a>=b)
print(a<b)

print(a >= 18 and dia == 3)
print(a<18 or dia!=3)

print(not(a >= 18 and dia != 3))
print(a<18 or dia==3)
num_fin = int(input("Escribe el número final: "))


linea_cancion(linea, num_ini, num_fin)
