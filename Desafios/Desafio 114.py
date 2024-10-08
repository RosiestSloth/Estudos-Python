import requests

def Verificar_Site(url):
    try:
        resposta = requests.get(url)
    except:
        print('O site do Pudim não está acessível.')
    else:
        print("O Site do Pudim está acessível.")

Verificar_Site('https://www.pudim.com.br/')

