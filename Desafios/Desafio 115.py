pessoas = list()
while True:
    print('-'*30)
    print(f'{"MENU PRINCIPAL":>22}')
    print('-'*30)

    print("\t1 - Ver pessoas cadastradas")
    print("\t2 - Cadastrar nova pessoa")
    print("\t3 - Sair")

    opcao = int(input("Opção: "))

    if opcao == 1:
        nome = str(input("Digite o nome"))
        pessoas.append(nome)
    else:
        break

print(pessoas)
