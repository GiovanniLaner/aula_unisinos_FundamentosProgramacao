valorProduto = float(input('Diga o valor do produto:'))

if (valorProduto < 20 and valorProduto > 0):
    valorFinal = valorProduto + (valorProduto * 0.45)
    print('Valor final com o lucro:', valorFinal)

elif (valorProduto >= 20 and valorProduto <= 50):
      valorFinal = valorProduto + (valorProduto * 0.35)
      print('Valor final com o lucro:', valorFinal)
else:
    valorFinal: valorProduto + (valorProduto * 0.25)
    print('Valor final com o lucro:', valorFinal)