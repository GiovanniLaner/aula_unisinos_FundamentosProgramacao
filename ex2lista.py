A = int(input('Diga um valor para A:'))
B = int(input('Diga um valor para B:'))
C = int(input('Diga um valor para C:'))

somaAB = A + B
somaAC = C + A

if (somaAB < somaAC):
    print('Soma de A + B é menor do que a soma de A + C')

else:
    print('Soma de A + C é maior do que a soma de A + B')