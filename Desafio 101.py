def voto(n):
    from datetime import date

    atual = date.today().year
    idade = atual - n
    if idade < 18:
        n = 'Voto negado!'
        return n
    elif idade <= 64:
        n = 'Voto obrigatório!'
        return n
    else:
        n = 'Voto opicional!'
        return n
    

print('-' * 30)
i = int(input('Em que ano você nasceu?\n'))
print(f'Com a idade {i} você tem {voto(i)}')