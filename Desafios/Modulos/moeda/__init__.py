#Aqui temos  o módulo de moedas

def moedas_aumentar(num=0, p=0, format=False):
    """
        num: Variável que recebe os valores
        p: Porcentagem que vai aumentar o valor
        format: Define se vai ser formatado para valor BRT ou não False or True
    """
    num += num*(p/100)
    return num if format is False else moeda(num) #Se a variável format for False, ele irá retornar o valor sem ser formatado se não retorna o valor formatado.

def moedas_diminuir(num=0, p=0, format=False):
    """
        num: Variável que recebe os valores
        p: porcentagem que vai ser diminuida
        format: Define se vai ser formatado para valor BRT ou não False or True
    """
    num -= num*(p/100)
    return num if format is False else moeda(num)#Se a variável format for False, ele irá retornar o valor sem ser formatado se não retorna o valor formatado.

def moedas_dobro(num=0, format=False):
    """
        num: Variável que recebe os valores
        format: Define se vai ser formatado para valor BRT ou não False or True
    """
    return num*2 if format is False else moeda(num*2)#Se a variável format for False, ele irá retornar o valor sem ser formatado se não retorna o valor formatado.

def moedas_metade(num=0, format=False):
    """
        num: Variável que recebe os valores
        format: Define se vai ser formatado para valor BRT ou não False or True
    """
    return num/2 if format is False else moeda(num/2)#Se a variável format for False, ele irá retornar o valor sem ser formatado se não retorna o valor formatado.

def moeda(num=0, moeda = 'R$'):
    """
        Formata o valor da moeda para BRT
        num: Recebe o número a ser formatado
        moeda: Recebe o parametro de País vai ser a moeda(Por padrão é do Brasil.)
    """
    return f'{moeda}{num:.2f}'.replace('.', ',')

def resumo(preco=0, taxa=10, taxar=5):
    print('-'*30)
    print('Resumo do valor'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{moedas_dobro(preco, True)}')
    print(f'Metade do preço: \t{moedas_metade(preco, True)}')
    print('-'*30)
