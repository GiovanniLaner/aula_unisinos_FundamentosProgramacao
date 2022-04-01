valor = float(input('DIGITE O VALOR A RETIRAR:'))

notas100 = int(valor / 100)
valor = valor - notas100 * 100
valor = valor % 100

print(notas100)
print(valor)

valor = float(input('DIGITE O VALOR A RETIRAR:'))
notas50 = int(valor / 50)
valor = valor % 50

print(notas50)
print(valor)

valor = float(input('DIGITE O VALOR A RETIRAR:'))
notas20 = int(valor /20)
valor = valor % 20

print(notas20)
print(valor)