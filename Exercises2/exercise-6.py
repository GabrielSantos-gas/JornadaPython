palavra = input('Digite uma palavra palíndromo') 

if palavra == palavra[::-1]:
    print('Está é uma palabra palíndromo')
else:
    print('Está nao é uma palavra palíndromo')