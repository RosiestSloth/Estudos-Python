tabuada = 0
numero = 0
mult = 0
print('Digite um número positivo para relizar a multiplicação \n e um negativo para encerrar o programa.')
while True:
    print('Digite um número: ')
    numero = int(input())
    if numero > 0:
        while tabuada != 11:
            mult = numero * tabuada
            print(numero, ' x ', tabuada, ' = ', mult) 
            tabuada += 1
    tabuada -= 10
    if numero < 0:
        break
print('Fim.')