aluno = dict()
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input('Média do aluno: '))
if aluno['media'] < 6:
    aluno['situacao'] = 'reprovado'
else:
    aluno['situacao'] = 'aprovado'
print(f'Média de {aluno["nome"]} é {aluno["media"]}\nO {aluno["nome"]} está {aluno["situacao"]}')