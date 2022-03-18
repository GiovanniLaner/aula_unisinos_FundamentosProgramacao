salario = float(input('Diga um salário:'))

descontoPrevidencia = salario * 0.11
calculoPrevidencia = salario - descontoPrevidencia
descontoMaximo = salario - 318.20

if (descontoPrevidencia <= 318.20):
    print('Seu salário com desconto:', calculoPrevidencia)

else:
    print('Seu salário com desconto:', descontoMaximo)