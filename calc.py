import math

def f(x):

    return round (((x**2) + (3**x) - 10), 3)


precisao = 0.001
y = True

while y:
    a = float(input(f'Digite a primeira estimativa (a): '))
    b = float(input(f'Digite a segunda estimativa (b): '))

    if f(a) * f(b) < 0:

        x = a

        while x <= b:

            raiz = f(x)

            # print (f'{raiz:.3f}: raiz. {x:.3f}: x')

            if abs(raiz) <= precisao:

                print(f"{raiz:.3f} : raiz aproximada da função, com x = {x:.3f}")

                y = False

            x = x + precisao

    else:
        print(f'Não é possivel seguir com: a = {a} e b = {b}. Estimativa inicial precisa ser menos que a estimativa final!')
