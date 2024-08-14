#open('caminho', 'r')

# r - Leitura
# a - Append
# e - escrita
# x - Criar Arquivo
# r+ - Leitura + escrita
# w - torna o arquivo em escrita mas limpa o conteúdo anterior/ cria um arquivo novo

# arquivo = open('Testes_de_aulas/Manipulacao_de_arquivos/teste3.txt', 'x')

#print(arquivo.readable()) - Verifica se o arquivo pode ser lido retornando True or False
#print(arquivo.read()) - Lê todo o arquivo.txt
#print(arquivo.readline()) - Lê apenas uma linha do arquivo.txt


#lista = arquivo.readlines() - Adiciona os textos dentro do arquivo dentro de uma lista

#print(lista)

#print(lista[3])

#arquivo.write('Python\n')

#arquivo.close()

import os

# if os.path.exists('Testes_de_aulas/Manipulacao_de_arquivos/teste3.txt'): # Verifica a existência de um arquivo e deleta o mesmo
#    os.remove('Testes_de_aulas/Manipulacao_de_arquivos/teste3.txt')
#    print('Deletado com sucesso')
#else:
#    print('Arquivo inexistente.')

os.rmdir('Testes_de_aulas/Manipulacao_de_arquivos/nova_pasta')