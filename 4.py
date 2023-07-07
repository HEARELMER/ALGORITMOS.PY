"""
(4) Pida al usuario que introduzca su nombre. Si la longitud de su primer nombre es inferior
a cinco caracteres, pídales que ingresen su apellido y los unan (sin espacios) y muestren
el nombre en mayúsculas. Si la longitud del nombre es de cinco o más caracteres, muestre
su nombre en minúsculas.
"""
nombre=input("Ingrese su nombre: ")

if len(nombre) <5:
    apellido=input("Ingrse su apellido: ")
    print((f"{nombre}{apellido}").upper()) #upper para convertir a mayuscula
else:
    print(nombre.lower())#lower es para convertir a minuscula
