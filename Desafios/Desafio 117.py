import time

def arqExiste(nome):
    try:
        a = open(nome, 'rt')
    except FileNotFoundError:
        return False
    else:
        return True

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        print('-'*30, '\nPESSOAS CADASTRADAS\n', '-'*30)
        for linha in a:
            dado = linha.split(';')
            dado[1].replace('\n', '')
            print(f'{dado[0]:30<}{dado[1]:>3} anos')
    finally:
        a.close()

def CriarArq(nome):
    try:
        a = open(nome, 'wt+')
        a.close
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def leiaInt(msg):
    try:
        idade = int(input(msg))
    except (TypeError, ValueError):
        print('ERRO: Digite um número')
        time.sleep(1)
    except():
        print('\033[31mERRO: Digite um valor válido\033[m')
        time.sleep(1)
    else:
        return idade
    
def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO no registro dos dados')
        else:
            print(f'Foram registrados, {nome} e {idade}')
        finally:
            a.close()




arq = 'cursoemvideo.txt'
pessoas = []
cont = 0

if arqExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado!')
    CriarArq(arq)

while True:
    try:
        print('-'*30)
        print(f'{"MENU PRINCIPAL":>22}')
        print('-'*30)

        print("\t\033[33m1\033[m - \033[34mVer pessoas cadastradas\033[m")
        print("\t\033[33m2\033[m - \033[34mCadastrar nova pessoa")
        print("\t\033[33m3\033[m - \033[34mSair")

        opcao = int(input("Opção: \033[m"))
        
    except (TypeError, ValueError):
        print('\033[31mERRO: Digite uma opção válida da tabela.\033[m')
    except KeyboardInterrupt:
        print('\033[31mERRO: Encerrado pelo usuário.\033[m')
    else:
        if opcao == 1:
            print('-'*30)
            print('          LISTANDO')
            print('-'*30)
            lerArquivo(arq)
        elif opcao == 2:
            print('-'*30)
            print('          NOVO CADASTRO')
            print('-'*30)
            nome = str(input("Nome: "))
            idade = leiaInt('Idade: ')
            cadastrar(arq, nome, idade)
        
        elif opcao == 3:
            print('-'*30)
            print('            SAINDO')
            print('-'*30)
            print('Obrigado por utilizar o programa!')
            print('-'*30)
            break
        else:
            print('\033[31mERRO: Digite uma opção válida da tabela\033[m')
            time.sleep(1)

#Nota 10 Gustavo Guanabara, excelente curso!!!!
