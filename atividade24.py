# Exercício Python 24: Refaça a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.

num = int(input('digite o numero:'))

for numero in range(0, 11):
    print('{} X {} = {}'.format(num ,numero,(num * numero)))
