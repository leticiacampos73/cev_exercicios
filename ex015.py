d = int(input('Quantos dias vc usou o carro?'))
km = float(input('quantos qulometros vc pecorreu:'))
t = (60 * d) + (0.15 * km)
print('o total a ser pago é R${:.2f}'.format(t))
#print(f'o total sera de R$: {t}')