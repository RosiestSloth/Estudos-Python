valor = float(input('Qual o  valor da casa?\n'))
salario = float(input('Qual o seu valor salárial?\n'))
anos = int(input('em quantos anos você vai pagar?\n'))
mes = anos * 12
prest = valor / mes
if prest > salario*0.3:
    print('Emprestimo negado')
else:
    print(f'o valor da prestação será de {prest}')