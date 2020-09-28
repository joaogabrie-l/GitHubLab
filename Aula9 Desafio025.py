nome = str(input('Digite seu nome completo: '))

nome = nome.upper()

nome = nome.find('SILVA')

if nome == -1:
    print('Seu nome não possuí Silva')
else:
    print('Seu nome possuí Silva')
    