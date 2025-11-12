from time import sleep

inventario = [
    {"id": 1, "nome": "Notebook UltraFino", "categoria": "Computadores", "preco": 4500.00, "estoque": 7},
    {"id": 2, "nome": "Monitor 4K", "categoria": "Periféricos", "preco": 1800.00, "estoque": 10},
    {"id": 3, "nome": "Teclado Mecânico RGB", "categoria": "Periféricos", "preco": 350.00, "estoque": 25},
    {"id": 4, "nome": "Mouse Sem Fio", "categoria": "Periféricos", "preco": 120.00, "estoque": 30},
    {"id": 5, "nome": "Cadeira Gamer", "categoria": "Móveis", "preco": 1500.00, "estoque": 3},
    {"id": 6, "nome": "Placa de Vídeo", "categoria": "Hardware", "preco": 3800.00, "estoque": 5},
    {"id": 7, "nome": "SSD 1TB", "categoria": "Hardware", "preco": 450.00, "estoque": 0}
]

def BuscaCategoria(): 
    print(f'nome: {inventario[2]['nome']}')
    
    categorias = set(c["categoria"] for c in inventario)

    for cat in categorias:
        print(f'- {cat}')

    print("Digite uma categoria")
    escolha = input(": ")

    for c in inventario:
        if c["categoria"].lower() == escolha.lower():
            print(f'{c["nome"]} | Preço: R${c["preco"]:.2f} | Estoque: {c["estoque"]} ')
            validacao = False

    if validacao:
        print("Não foi encontrada nenhuma categoria")
    
    return True

def ListaEstoque():
    print(f'nome: {inventario[2]['nome']}')

    for c in inventario:
        if c["estoque"] == 0:
            print("- Produtos sem estoque: ")
            print(f'- {c["nome"]} | Preço: R${c["preco"]:.2f} | Estoque: {c["estoque"]} ')
            validacao = False

    if validacao:
        print("Não foi encontrada nenhuma categoria")

    return True

def ProdutoMaisCaro():
    for c in range(6):
        if inventario[c]["preco"] >= inventario[c-1]["preco"]:
            valorMenor = inventario[c]
        
    print(f"- {valorMenor["nome"]} | Preço: R${valorMenor["preco"]:.2f} | Estoque: {valorMenor["estoque"]} ")
    return True
        

def main():
    opcao = 0
    print("- 1 Buscar categoria\n- 2 Listar Estoque\n- 3 Visualizar Produto Mais Caro\n- 0 Sair[Padrão]")
    
    print(f"Digite uma opção[{opcao}]")
    opcao = int(input(": "))

    try:
        match opcao:
            case 1:
                BuscaCategoria()
            case 2:
                ListaEstoque()
            case 3:
                ProdutoMaisCaro()
            case 0:
                print("Obrigado por utilizar o programa!")
            case _:
                print("Digite um valor válido")

    except Exception:
        print("Digite um valor numérico válido")

valorMenor = []
perifericos = []
escolha = ""
validacao = True

print("-=-=-=-=-=-=-= SEJA BEM VINDO -=-=-=-=-=-=-=")
sleep(0.3)
main()