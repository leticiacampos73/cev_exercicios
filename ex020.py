from random import shuffle
a1 = str(input('O nome do primeiro aluno:'))
a2 = str(input('O nome do segundo aluno:'))
a3 = str(input('O nome do terceiro aluno:'))
a4 = str(input('O nome do quarto aluno:'))
lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'a ordem será: \n {lista}')