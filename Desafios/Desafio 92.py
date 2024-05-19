from time import sleep
trabalhador = {}
trabalhador['nome'] = str(input('Digite seu nome: '))
trabalhador['ano'] = int(input('Digite o seu ano de nascimento: '))
trabalhador['ctps'] = int(input('Digite a sua carteira de trabalho(se você não tem, digite 0)'))
if trabalhador['ctps'] != 0:
    trabalhador['contratacao'] = int(input('que ano você foi contratado?\n'))
    trabalhador['salario'] = float(input('Qual seu salário?\n'))
else:
    print('Processando...')
    sleep(2)
trabalhador['idade'] = 2024 - trabalhador['ano']
trabalhador['aposentado em'] = (65 - trabalhador['idade']) + 2024
print(f'Você tem {trabalhador["idade"]} anos, sua carteira de trabalho é {trabalhador["ctps"]}, você vai aposentar em {trabalhador["aposentado em"]}')