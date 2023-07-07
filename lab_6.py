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
num_fin = int(input("Escribe el número final: "))

linea_cancion(linea, num_ini, num_fin)
