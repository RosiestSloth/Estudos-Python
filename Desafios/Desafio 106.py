print('\033[31m', '~'*30)
print('   Sistema de ajuda PyHelp')
print('~'*30)
resp = ''

while resp != 'N':
    h = str(input('\033[0mFunção ou biblioteca > '))
    
    print(f'\033[7;30m {help(h)} \033[m')
    resp = str(input('Você quer continuar S/N?\n').upper())

print('Obrigado por utilizar o programa.')