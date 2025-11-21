from time import sleep;

# Cadastrar Clientes < / Cadastrar Funcionários com role < / Realizar Pedidos / Cadastrar Pizzas / Editar os dados / Listar dados <

# \
def opcoes(tipo):

    if tipo == "menuInicio":
        print("-="*5, "MENU INICIAL", "-="*5)
        print("\n- 1: Cadastro de Clientes\n- 2: Cadastro de Funcionários\n- 3: Realização de Pedidos\n- 4: Cadastro de Pizzas\n- 5: Listagem de usuários\n- 6: Listagem de Funcionários\n- 0: Fechar o Programa")
        option = int(input("\nDigite o valor: "))
        return option
    
def listarClientes():
    """ listagem de Clientes com um for simples, utilizando os valores dentro do dicionário """
    print("-="*10)
    for c in clientes:
        print(c["nome"], " - ", c["contato"], " - ", c["endereco"])
    print("-="*10)
    sleep(1)

def CadastroClientes():
    """ Cadastrar Clientes da Pizzaria, que armazena os valores dentro de um dicionário e depois adiciona em uma lista, e soma a quantidade total com +1 cadastrado. """
    global qtd_clientes
    try:
        cliente = {}
        cliente["nome"] = str(input("Digite o Nome: "))
        cliente["contato"] = str(input("Digite o Contato: "))
        cliente["endereco"] = str(input("Digite o Endereço: "))
    
        clientes.append(cliente)
        print("Cliente Cadastrado com Sucesso!")
        qtd_clientes += 1
        sleep(1)
    
    except Exception as e:
        print("Erro ao Cadastrar Cliente: ", e)
        sleep(0.5)

# Seção de Funcionários
def listarFuncionarios():
    """ listagem de funcionários com um for simples, utilizando os valores dentro do dicionário """
    print("-="*10)
    for c in funcionarios:
        print(c["nome"], " - ", c["contato"], " - ", c["role"])
    print("-="*10)
    sleep(1)

def CadastroFuncionarios():
    """ Cadastrar Funcionários da Pizzaria, que armazena os valores dentro de um dicionário e depois adiciona em uma lista, e soma a quantidade total com +1 cadastrado. """
    global qtd_funcionarios
    try:
        funcionario = {}
        funcionario["nome"] = str(input("Digite o Nome: "))
        funcionario["contato"] = str(input("Digite o Contato: "))
        funcionario["role"] = str(input("Digite o Cargo: "))
    
        funcionarios.append(funcionario)
        print("Funcionário Cadastrado com Sucesso!")
        qtd_funcionarios += 1
        sleep(1)
    
    except Exception as e:
        print("Erro ao Cadastrar Funcionário: ", e)
        sleep(0.5)


cliente = {"nome": "Matheus", "contato": "99 9999-9999", "endereco": "Rua 2 Lote 10 Casa Nº 950"}
funcionario = {"nome": "Adélio", "contato": "99 9999-9999", "role": "Administrador"}
clientes = []
funcionarios = []
option = ""
clientes.append(cliente)
funcionarios.append(funcionario)
qtd_clientes = int(0)
qtd_funcionarios = 0




while option != 0:
    option = opcoes("menuInicio")

    match option:
        case 1:
            # Cadastrar Clientes
            print("Cadastro de Clientes")
            CadastroClientes()

        case 2:
            # Cadastrar Funcionários
            print("Cadastro de Funcionários")
            CadastroFuncionarios()

        case 3:
            # Realização de Pedidos
            print("Realização de Pedidos")

        case 4:
            # Cadastrar Pizzas
            print("Cadastro de Pizzas")

        case 0:
            # Sair do loop
            print("Saindo...")
            sleep(1)
            breakpoint
        case 5:
            print("Listagem de Usuários")
            listarClientes()
        case 6:
            print("Listagem de Funcionários")
            listarFuncionarios()
        case _:
            #Erro
            print("Erro: Digite um valor válido das opções")