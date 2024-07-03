#Aqui temos  o módulo de moedas

def moedas_aumentar(num=0, p=0):
    num += num*(p/100)
    return num

def moedas_diminuir(num=0, p=0):
    num -= num*(p/100)
    return num

def moedas_dobro(num=0):
    return num*2

def moedas_metade(num=0):
    return num/2

def moeda(num=0, moeda = 'R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')



#def moedas_aumentar(num=0, p=0):
#    return num

def moedas_diminuir(num=0, p=0):
    num -= num*(p/100)
    return num

def moedas_dobro(num=0):
    return num*2

def moedas_metade(num=0):
    return num/2

def moeda(num=0, moeda = 'R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')