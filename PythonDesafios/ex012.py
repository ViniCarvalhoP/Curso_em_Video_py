preço = float(input("Qual é o preço do produto? R$"))
novo = preço - (preço*5/100)
print ("O produto que custava {:.2f}, na promção com desconto de 5% custará R${:.2f}!".format(preço,novo))
