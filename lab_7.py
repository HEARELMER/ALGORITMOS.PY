#EXAMEN DE ALGORITMOS
#Para el siguiente programa, repsonda la pregunta asociada. Si son valores
#en ves de nueva linea escriba un espacion en blanco.Si es un bucle infinito
#escriba infinito.Si se produce error escriba error

# num_1=0
# num_rosas=2
# while num_1<10:
#     num_rosas*=2
#     num_rosas+=num_1
#     num_1+=5
    
# print(f"Num {num_rosas}")
#imprime Num 13

#PREGUNTA 2:

# #un contaador de programas 
# a)Cuenta el numero de operacion primitivas ejecutadas por el programa.
# b)cuenta el numero de operaciones primitivas que comprenden una operación compleja
# c)señala a la computadora la siguiente instruccion para jecutar el programa 
# d) recuerda cuantas veces se ah ejecutado el programa

# #Respuesta: Es la opcion d

#PREGUNTA 3:
# # ¿Que imprime la funcion continua(10)
# def cuenta():
#     c=0
#     for i in range(1,50641):
#         if i%3==0 and i%5==0:
#             c+=1
    
#     return c
# print(cuenta())

# #respuesta: 3376 es solamente hacer una divison entera 50640 entre 15(porque avanza+15)

# #PREGUNTA 4
# # ¿Cuál es el valor que retorna la funcion de raiz_cuadrada() cuyo argumento es 17?

# def raiz_cuadrada(x):
#     epsilon=0.01
#     paso=0.1
#     raiz=0.0
#     while abs(raiz**2-x)>=epsilon:
#         if raiz <=x:
#             print(raiz)
#             raiz+=paso
#         else:
#             break
        
#     if abs(raiz**2-x)>=epsilon:
#         return 'malo'
#     else:
#         return round(raiz,2)
    
# print(f'{raiz_cuadrada(10)}')

# #PREGUNTA 5
# # Para la siguiente expresión, indique el valor que se imprime cunado se evalua.
# # Si se produce error escriba :error
# var='Honda'
# if var=='honda':
#     print('moto!')
# elif var==" Honda":
#     print("Regalo!")
# else:
#     print("error")
    
# #Respuesta: Se imprime error

# #PREGUNTA 6
# # Para el siguiente programa, responda l apregutn asociada.Si son valores, en
# # vez de nueva linea escriba un espacio en blanco.Si es un bucle infinito escriba
# # infinito.Si se produce error escriba error

# # num=10
# # b=False
# # while not b:#aqui es la negacion de False
# #     if num<0:
# #         break
# # print(num)
# #Respuesta: infinito

# #Pregunta 7

# contador=0
# for letra in "UNSCH!!":
#     print(f"Letra # {contador} es {letra}.")
#     contador+=1
#     break
# print(contador)
# #Respuesta. Letra #0 es U.(antes de incrementar imprime, y luego se rompe el ciclo)

# #Pregunta 8:
# print(6//2*'bc')
# #Respuesta: bcbcbc(precdencia de izquierda a derecha)

# #PREGUNTA 9
# num=0
# while num<3:
#     print(num)
#     num+=1
    
# print("A")
# print(num)
# #Respuesta:0 1 2 A 3(porque primero se ejcuta el bucle hasta que sea falsa entonces pasa abajo)

# #PREGUNTA 10

# contador=0
# frase="hola, mundo"
# for i in range(5):
#     while True:
#         contador+=len(frase)
#         break
#     print(f"iteracion {i}; contador es: {contador}")
    
# print("#####")
# contador=0
# frase="hola, mundo"
# for i in range(5):
#     contador+=len(frase)
#     print(f"iteracion{i}; contsdor es: {contador}")

#repsuesta:Son iguales.

#pREGUNTA 11
# num=9
# while True:
#     if num<7:
#         print("B")
#         break
#     print(num)
#     num-=1
    
# print("F")

# #RESPUESTA: 9 8 7 B F(EL BREAK QUE ESTA DENTRO DEL IF ROMPE TODOEL CICLO WHILE)

# # PRGUNTA 12
# a=1
# b=10
# c=3
# def adivina(a,b,c):
#     for i in range(a,b,c):
#         print(i, end=" ")
        
# print(adivina(a,b,c))

# # respuesta:1 4 7 None(END SIRVE PARA JUNTAR LINEAS) 

# v="aeiou"
# for letra in "mujeres":
#     if letra not in v:
#         print(letra)
        
# num=0
# val=2
# while num <10:
#     val*=2
#     val+=num
#     num-=1
    
# print(f"{val}")

# divisor=2
# for num in range(0,6,2):
#     print(num/divisor)
    
# for variable in range(1,10):
#     if variable%4==0:
#         print(variable)
#     if variable%6==0:
#         print("F")
        
# def a(x):
#     return x+ 2.0
# print(a(a(a(a(6)))))

# nota=70
# if nota >85:
#     print("ALta")
# elif nota >100:
#     print("ALTA")
    
# elif nota >60:
#     print("Media")

# else:
#     print("Baja")
    
# vara=2
# varb=int(2.9)
# if (str==type(vara) and str==type(varb)):
#     print("cadenas")
    
# elif vara>varb:
#     print("Mayor")

# elif vara==varb:
#     print("igual")
    
# elif vara<varb:
#     print("pequeña")
# #int no redondea sino saca la parte entera 

# saludo="Hola!"
# contador=0
# for letra in saludo:
#     contador+=1
#     if contador %2==0:
#         print(letra)
#     print(letra)
    
# print("Fin")   


# def a(x):
#     return x+1

# def b(x):
#     return x*1.0
# def c(x,y):
#     return x+y
# def e(x,y,z):
#     return x>=y and x<=z
# print(e(a(3),b(4),c(3,4)))


x=12
def g(x):
    x=x+1
    def h(y):
        return x+y
    return 2*h(6)
print(g(x))