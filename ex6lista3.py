import random


numero = int(input('É hora do duelo do par ou impar, escolha um número de 0 a 5:'))
numeroRandom = random.randint(0, 5)

resultado = numero + numeroRandom

print('Seu número', numero
      , 'número da máquina', numeroRandom)

if (resultado % 2 == 0):
    print('Deu par!')

else:
    print('Deu impar!')    