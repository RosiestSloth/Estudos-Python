from time import sleep;

# Cadastrar Clientes < / Cadastrar Funcionários com role < / Realizar Pedidos / Cadastrar Pizzas / Editar os dados / Listar dados <

# \
def opcoes(tipo):
    global qtd_clientes
    global qtd_funcionarios

    if tipo == "menuInicio":
        print("-="*5, "MENU INICIAL", "-="*5)
        print("\n- 1: Cadastro de Clientes\n- 2: Cadastro de Funcionários\n- 3: Realização de Pedidos\n- 4: Cadastro de Pizzas\n- 5: Listagem de Clientes\n- 6: Listagem de Funcionários\n- 7: Editar Dados de Clientes\n- 8: Editar Dados de Funcionários\n- 0: Fechar o Programa")
        option = int(input("\nDigite o valor: "))
        return option
    
    elif tipo == "menuUsuario":
        print("-=" * 20)
        print(f"{'EDITAR USUÁRIO':^40}")
        print("-=" * 20)

        listarClientes()

        id_cliente = int(input("Digite o [id] do usuário: "))
        
        editarCliente(id_cliente)

    elif tipo == "menuFuncionario":
        print("-=" * 20)
        print(f"{'EDITAR FUNCIONÁRIO':^40}")
        print("-=" * 20)

        listarFuncionarios()

        id_funcionario = int(input("Digite o [id] do Funcionário: "))
        
        editarFuncionario(id_funcionario)
    elif tipo == "menuCliente":
        print("-=" * 20)
        print(f"{'EDITAR CLIENTE':^40}")
        print("-=" * 20)

        listarClientes()

        id_cliente = int(input("Digite o [id] do Funcionário: "))
        
        editarCliente(id_cliente)
    
    elif tipo == "menuCliente":
        print("-=" * 20)
        print(f"{'REALIZAR PEDIDO':^40}")
        print("-=" * 20)

        listarClientes()
        listarPizzas()
        
        realizarPedido()

# Seção de Clientes
def listarClientes():
    """ listagem de Clientes com um for simples, utilizando os valores dentro do dicionário """
    print("Lista de Clientes")

    print(f"{'[ID]':<6} {'Nome':<25} {'Contato':<15} {'Endereço'}")

    for c in range(qtd_clientes):
        print(f"[{c:^2}]   {clientes[c]['nome']:<25} {clientes[c]['contato']:<15} {clientes[c]['endereco']}")
        sleep(0.2)

    print("-=" * 20)
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
        CadastroClientes()

def editarCliente(id_cliente):
    try:
        print(f"Editando informações de {funcionarios[id_cliente]["nome"]}")
        
        clientes[id_cliente]["nome"] = str(input("Digite o nome do Funcionário: "))
        clientes[id_cliente]["contato"] = str(input("Digite o contato do Funcionário: "))
        clientes[id_cliente]["endereco"] = str(input("Digite o tipo de Funcionário: "))

    except Exception as e:
        print(f"Erro: valores inválidos: {e}")

def editarCliente(id_cliente):
    try:
        print(f"Editando informações de {clientes[id_cliente]["nome"]}")
        
        clientes[id_cliente]["nome"] = str(input("Digite o nome do cliente: "))
        clientes[id_cliente]["contato"] = str(input("Digite o contato do cliente: "))
        clientes[id_cliente]["endereco"] = str(input("Digite o endereço do cliente: "))

    except Exception as e:
        print(f"Erro: valores inválidos: {e}")

# Seção de Funcionários
def listarFuncionarios():
    """ listagem de funcionários com um for simples, utilizando os valores dentro do dicionário """
    print("Lista de Clientes")

    print(f"{'[ID]':<6} {'Nome':<25} {'Contato':<15} {'Endereço'}")

    for c in range(qtd_funcionarios):
        print(f"[{c:^2}]   {funcionarios[c]['nome']:<25} {funcionarios[c]['contato']:<15} {funcionarios[c]['role']}")
        sleep(0.2)

    print("-=" * 20)
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
        CadastroFuncionarios()

def editarFuncionario(id_funcionario):
    """ Editar dados de funcionários da empresa """
    try:
        print(f"Editando informações de {funcionarios[id_funcionario]["nome"]}")
        
        funcionarios[id_funcionario]["nome"] = str(input("Digite o nome do Funcionário: "))
        funcionarios[id_funcionario]["contato"] = str(input("Digite o contato do Funcionário: "))
        funcionarios[id_funcionario]["role"] = str(input("Digite o tipo de Funcionário: "))

    except Exception as e:
        print(f"Erro: valores inválidos: {e}")

# Seção de Pizzas

def cadastroPizzas():
    """Função para a realização do cadastro de Pizzas do sistema"""
    global qtd_pizzas
    try:
        pizza = {}
        pizza["nome"] = str(input("Digite o nome da Pizza: "))
        pizza["engredientes"] = str(input("Digite os engredientes: "))
        pizza["valor"] = float(input("Digite o valor: "))
        pizzas.append(pizza)

        print("Pizza cadastrada com Sucesso!")
        qtd_pizzas += 1
        sleep(1)

    except Exception as e:
        print("Erro ao cadastrar Pizza", e)
        sleep(0.5)
        cadastroPizzas()

def listarPizzas():
    print("Lista de Pizzas")

    print(f"{'[ID]':<6} {'Nome':<15} {'engredientes':<25} {'valor'}")

    for c in range(qtd_pizzas):
        print(f"[{c:^2}]   {pizzas[c]['nome']:<25} {pizzas[c]['engredientes']:<15} {pizzas[c]['valor']}")
        sleep(0.2)

    print("-=" * 20)
    sleep(1)

# Seção de Pedidos

def realizarPedido():
    id_cliente = int(input(("Digite o [id] do Cliente: ")))
    id_pizza = int(input("Digite o [id] da Pizza: "))


cliente = { "nome": "Matheus", "contato": "99 9999-9999", "endereco": "Rua 2 Lote 10 Casa Nº 950" }
funcionario = { "nome": "Adélio", "contato": "99 9999-9999", "role": "Administrador" }
pizza = { "nome": "4 Queijos", "engredientes": "Mussarela, parmesão, sheddar", "valor": 20.00 }
clientes = []
funcionarios = []
pizzas = []
option = ""
clientes.append(cliente)
funcionarios.append(funcionario)
pizzas.append(pizza)
qtd_clientes = 1
qtd_funcionarios = 1
qtd_pizzas = 1

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
            cadastroPizzas()
        
        case 5:
            # Listagem de Clientes
            print("Listagem de Clientes")
            listarClientes()

        case 6:
            # Listagem de Funcionários
            print("Listagem de Funcionários")
            listarFuncionarios()
        
        case 7:
            # Editar dados de Clientes
            print("Edição de Dados")
            opcoes("menuUsuario")

        case 8:
            # Editar dados de Funcionários
            print("Edição de Dados")
            opcoes("menuFuncionario")

        case 9:
            print("Edição de Dados")
            opcoes("menuCliente")
        case 0:
            # Sair do loop
            print("Saindo...")
            sleep(1)
            breakpoint

        case _:
            #Erro
            print("Erro: Digite um valor válido das opções")