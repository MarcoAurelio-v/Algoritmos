import typing

nombre:str = input("Ingrese su nombre: ")
edad:int = int(input("Ingrese su edad: )")
# Si su edad es menor o igual a 4 años el precio de su entrada es gratis.
# Si su edad es menor o igual a 18 años el precio de su entrada es de $1.50
# Si su edad es mayor o igual a los 60 años su entrada tendrá un valor de $1
# La entrada para un adulto promedio es de $2.00
precio_entrada:float = 0.0
if edad <= 4:
    precio_entrada = 0.0
elif edad <= 18:
    precio_entrada = 1.50
elif edad >= 60:
    precio_entrada = 1.00
else: 
    precio_entrada = 2.00

print (f'El cliente: {nombre} tiene: {edad} años y su entrada de cine cuesta: ${precio_entrada}')