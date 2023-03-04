T = float(input("Quantos dias Alugados? "))
D = float(input("Quantos Km rodados? "))
A = ( 60 * T) + (0.15 * D)
print ("O total a pagar é de R${:.2f}!".format(A))
