lista = ('pão', 1.00,
          'azeitona', 15.99,
            'pringless', 12.00,
              'toddy', 12.50,
                'salsicha', 9.90,
                'farinha', 4.90)
print()
print(30*'-','\n      LISTAGEM DE PREÇOS')
print(30*'-')
print(f'{lista[0]}', 16*'.', f'R${lista[1]}'
      f'\n{lista[2]}', 11*'.', f'R${lista[3]}'
      f'\n{lista[4]}', 10*'.', f'R${lista[5]}'
      f'\n{lista[6]}', 14*'.', f'R${lista[7]}'
      f'\n{lista[8]}', 11*'.', f'R${lista[9]}'
      f'\n{lista[10]}', 12*'.', f'R${lista[11]}')
print(30*'-') 
print()