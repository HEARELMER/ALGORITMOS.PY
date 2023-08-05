# ejercicio 3:
# Abra el archivo Nombres.txt y visualice los datos en Python. Abra el
# archivo Nombres.txt. Pídale al usuario que ingrese un nuevo nombre.
# Agregue esto al final del archivo y muestre el archivo completo.

#NOTA: El archivo nombre debe tner 5 lineas con nombres

def nombres(file, nombres):
    try:
        # Verifica si nombres no está vacío o sea un numero o caracter
        if len(nombres.strip()) > 0 and nombres.replace(" ", "").isalpha(): 
            
            print(nombres)
            #esto escribe una nueva linea, exista o no el archivo
            with open(file, "a") as archivo: 
                archivo.write(nombres + "\n")    
            
            #esto lee el archivo y retorna el contenido
            with open(file, "r") as archivo:
                contenido = archivo.read().strip()
                return contenido
            
        #si no s ecumple el if
        else:
            return "Nombre incorrecto, vuelve a intentar"
            
            
    except  Exception as e:#si sucede algun error 
        return str(e)

usuario=input("Nombre: ")
print(nombres("nombres.txt", usuario))#imprime lo que retorna la funcion nombres


# # EJERCICIO 4.

# Muestre el siguiente menú al usuario:
# # 1) Crear un nuevo archivo
# # 2) Mostrar el archivo
# # 3) Y un nuevo elemento para el archivo
# # Haga una selección 1,2 o 3.
# # Pida al usuario que ingrese 1, 2 o 3. Si seleccionan cualquier cosa que no
# # sea 1, 2 o 3, debería mostrar un mensaje de error adecuado. Si seleccionan
# # 1, pídale al usuario que ingrese una materia escolar y la guarde en un
# # nuevo archivo llamado "Asunto.txt". Debería sobrescribir cualquier archivo
# # existente con un archivo nuevo. Si seleccionan 2, muestran el contenido

# # del archivo "Topico.txt". Si seleccionan 3, pídale al usuario que ingrese un
# # nuevo tópico y lo guarde en el archivo y luego muestre todo el contenido
# # del archivo. Ejecute el programa varias veces para probar las opciones.

#FUNCIONES PARA EL MENEJO DE LAS OPCIONES DEL MENU
def crear_archivo(file):
    curso=input("Ingresa un curso: ")
    with open(file, "w") as texto:
        texto.write(curso)


def leer(file):
    with open(file, "r") as topico:
        contenido=topico.read().strip()

    return contenido


def opcion3(file):
    topico=input("Ingrse un nuevo tòpico: ")
    with open(file, "a") as archivo:
        archivo.write("\n" + topico)

def menu():
    #dicciorario del menú
    menu={
            "1":"Crear un nuevo archivo",
            "2":"Mostar el archivo",
            "3":"Nuevo elemnto para el archivo"
          }
    
    print("MENU")
    c=0
    for i in menu.values():
        c=c+1
        print(f"{c}) {i}")

    print("="*30)
  
def usuario():
        menu()
        opcion=input("Elige una opción del menú: ")
        if opcion=="1":
            crear_archivo("asunto.txt")
        elif opcion=="2":
            print(leer("topico.txt"))

        elif opcion=="3":
            opcion3("topico.txt")
            print(leer("topico.txt"))
        else:
            print("Opción inválida, vuelve a intentarlo")
            print("="*30)   
            usuario()  
try:
    usuario()
except Exception as e:
    print(e)
    


# # 5. Con el archivo Nombres.txt que creó anteriormente, muestre la lista de
# # nombres en Python. Pida al usuario que escriba uno de los nombres y
# # luego guarde todos los nombres excepto el que ingresó en un nuevo
# # archivo llamado Nombres2.txt.

# # Fantástico trabajo, guardar datos en archivos externos es una habilidad
# # de programación importante
