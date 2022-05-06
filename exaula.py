from re import X


A = [10, 2, 64, 53, 123]

somatorio = A[0] + A[1] + A[2] + A[3] + A[4] 

soma = 0
for X in A:
    soma += X 
print('Somatório =', soma)    
print(somatorio)
produto = 1
for X in A:
    produto *= X
print('Produto de tudo é:', produto)