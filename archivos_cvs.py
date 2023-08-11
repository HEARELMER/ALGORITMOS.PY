# Cree un cuestionario de matemáticas 
# simple que le pedirá al usuario su
# nombre y luego generará dos preguntas
# aleatorias. Guarda su nombre,
# las preguntas que se le hicieron, 
# sus respuestas y su puntuación final en
# un archivo .csv. Cada vez que se ejecuta
# el programa, debe agregarse al
# archivo .csv y no sobrescribir nada.

import csv 
import random

def crear_archivo(file):
    try :
        with open(file, "r") as archivo:
            return file
        
    except FileNotFoundError:
        print("Archivo no encontrado,creando....")
        with open(file,"w",encoding="utf-8") as archivo:
            encabezado="NOMBRES, PREGUNTAS, RESPUESTAS, PUNTUACIÓN\n"
            archivo.write(encabezado)
            
        return file
    except Exception as e:
        return str(e)
    
def generar_pregun():
    num1=random.randint(1,20)
    num2=random.randint(1,20)
    operador=random.choice(["+","-","*"])
    pregunta=f"{num1} {operador} {num2} = "
    if operador=="+":
        respuesta=num1+num2
        
    elif operador=="-":
        respuesta=num1-num2
    else:
        respuesta=num1*num2
        
    return pregunta, respuesta

def guardar(nombre, preguntas, respuestas, puntuacion):
    archivo=crear_archivo("archivo.csv")
    with open(archivo,"a", newline="", encoding="utf-8") as salida:
        writer=csv.writer(salida)
        respuestas_str=[str(r) for r in respuestas]
        writer.writerow([nombre, ', '.join(preguntas), ','.join(respuestas_str), puntuacion])
        
        
def usuario():
    nombre=input("Ingrsea tu nombre: ")
    pregunta1, respuesta1=generar_pregun()
    pregunta2, respuesta2=generar_pregun()
    
    print(pregunta1)
    respuesta_usuario1=int(input())
    print(pregunta2)
    respuesta_usuario2=int(input())
    
    puntuacion=0
    preguntas_correctas=[]
    respuestas_correctas=[]
    if respuesta_usuario1==respuesta1:
        puntuacion+=1
        preguntas_correctas.append(pregunta1)
        respuestas_correctas.append(respuesta1)
        
    if respuesta_usuario2==respuesta2:
        puntuacion+=1
        preguntas_correctas.append(pregunta2)
        respuestas_correctas.append(respuesta2)
        
    guardar(nombre, preguntas_correctas,respuestas_correctas,puntuacion)
    
#mostramos la funcion usuario

usuario()
