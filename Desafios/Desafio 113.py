def Leia_Int():
    while True:
        try:
            n = int(input("Digite um número inteiro: "))
        except:
            print("ERRO: Digite um valor válido.")
        else:
            return n
        
def Leia_Float():
    while True:
        try:
            n = float(input("Digite um número Real: "))
        except:
            print("ERRO. Digite um valor válido")
        else:
            return n


inteiro = Leia_Int()
real = Leia_Float()

print(f"O valor inteiro digitado foi {inteiro}\nO valor Real digitado foi {real}")