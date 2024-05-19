from time import sleep

def notas(*num, sit=False):
    """
    Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais noras dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionario com várias informações sobre a situação da turma.
    """
    notas = []
    soma = 0

    for q in num:
        notas.append(q)
        soma += q

    print(notas)
    dados = {}
    notas.sort()
    dados['Quantidade de notas'] = len(notas)
    dados['Maior nota'] = notas[len(notas) - 1]
    dados['Menor nota'] = notas[0]
    dados['Media'] = soma/len(notas)

    if sit:
        if dados['Media'] > 7:
            dados['situação'] = 'boa'

        elif dados['Media'] <= 7:
            dados['situação'] = 'ruim'

    return dados


dados = notas(8, 9, 5, 6  , 8, sit=True)

for k, i in dados.items():
    print(f'A {k} é {i}')
