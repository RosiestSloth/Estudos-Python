import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://pudim.com.br')
except urllib.error.URLError:
    print("O site Pudim não está acessível no momento.")
else:
    print("Conseegui acesar o site Pudim com sucesso!")
    print(site.read())
