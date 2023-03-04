atual = float(input("Qual é o salário do Funcionário? R$"))
novo =  atual + (atual*15/100)
print ("Um Funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receebr R${:.2f}".format(atual,novo))
