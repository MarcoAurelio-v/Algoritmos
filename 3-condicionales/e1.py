import typing

candidate:float = float(input("Por favor ingresa un número: "))

is_even: bool = True

if candidate % 2 == 0:
    is_even = True
else:
    is_even:bool = False

is_positive:bool = True

if candidate >= 0:
    is_positive = True
else:
    is_positive = False
msg:str = f"El número {candidate} es "

if is_even == True:
    msg += "par y es"
else:
    msg += "impar y es"
if is_positive == True:
    msg += "positivo"
else:
    msg += "negativo"
print(f"{msg}")