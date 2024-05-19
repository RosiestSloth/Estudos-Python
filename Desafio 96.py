from time import sleep

def area(l, c):
    Area_Terreno = (l * c)
    print(f'A área do terreno com os valores dados é de {Area_Terreno}m²')


l = int(input('Digite a largura do terreno: '))
c = int(input('Digite o comprimento do terreno: '))
print('Recebendo os valores...')
sleep(1)
print(f'Largura = {l}\ncomprimento = {c}')
sleep(0.5)
area(l, c)
 