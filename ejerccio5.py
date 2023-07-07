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
        
pedir_numeros(8,5)
