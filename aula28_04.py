import random
'''Correção prova'''
#ex1
def ehPrimo(n):
   for i in range(2, n):
        if n % i == 0:
           primo = False
           print('não é primo')
           return False
   return True

n = int(input('Digite um numero:'))
print(ehPrimo(n))

#2
contPositivos = 0
contNegativos = 0
contDivisao2 = 0
contDivisao5 = 0
contPrimos = 0
contTotal = 0
n = -1
while (n != 0):
   n = int(input("Digite um numero inteiro:"))
   contTotal = contTotal + 1

   if n > 0:
      contPositivos = contPositivos + 1
   if n < 0:
      contNegativos = contNegativos + 1
   if n % 2 == 0:
      contDivisao2 = contDivisao2 + 1
   if n % 5 == 0:
      contDivisao5 = contDivisao5 + 1
   if (ehPrimo(n) == True):
      contPrimos = contPrimos + 1

print('total de numeros lidos:', contTotal)
print('Porcentagem de numeros positivos:', round(contPositivos / contTotal * 100, 2), '%')
print('Porcentagem de numeros negativos:', round(contPositivos / contTotal * 100, 2), '%')
print('Porcentagem de numeros divisiveis por 2:', round(contDivisao2 / contTotal * 100, 2), '%')
print('Porcentagem de numeros divisiveis por 5:', round(contDivisao5 / contTotal * 100, 2), '%')
print('Porcentagem de numeros primos:', round(contPrimos / contTotal * 100, 2), '%')

#4
sorteado = random.randint(1,10)

tentativas = 3
adivinhou = False

while (tentativas > 0 and adivinhou == False):
   numeroLido = int(input('Digite um numero de 1 a 10:'))
   tentativas = tentativas - 1
   if numeroLido == sorteado:
      print('Você acertou')
      adivinhou = True
   else:
      print('Voce errou')
      print('Vc ainda tem', tentativas, 'tentativas.')

if adivinhou == False:
   print('O numero sorteado era', sorteado)

   