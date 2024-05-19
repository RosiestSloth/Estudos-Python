n = s = 0
contagem = 0
while True:
    
    n = int(input('Digite um número ou digite 999 para sair'))
    contagem += 1
    s +=n

    if n == 999:
        
        break

n = -999
print(f'A quantidade de números digitados é {contagem} e a soma entre eles é {s}')