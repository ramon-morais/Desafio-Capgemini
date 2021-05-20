def calcular_valor_investido():
    valor = float(input("Digite o valor, em reais, que deseja investir: \n"))
    total = (valor * 21.6) * 4 + (valor * 30)
    return total

total = calcular_valor_investido()
print("O total de visualizacoes é {:.2f} ".format(total))
