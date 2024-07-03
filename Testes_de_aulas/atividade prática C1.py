nome = input('qual seu nome? \n ')
print(f'Boas vindas {nome}')
idade = int(input(f'qual sua idade : '))
if idade >= 16:
    print('Você é elegível para votar na eleição estudantil!')
else:
    print('Desculpe, você ainda não tem idade suficiente para votar na eleição estudantil.')