numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if  num >=0 and num <=20:
            break
        print('Tente novamente. ')
    print(f'O número é {numero[num]}')
    print('Você quer continuar?S/N')
    c = str.lower(input(''))
    if c == 'n':
        break
    elif c == 's':
        print('iniciando novamente...')
print('FIM.')