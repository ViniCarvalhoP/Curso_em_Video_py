Real = float(input("Quanto dinheiro você tem na carteira? R$"))
Dólar = Real / 5.29
Euro = Real / 5.63
Libras = Real / 6.37
print ("Você, com R$ {:.2f}, pode comprar em US$ {:.2f}, em EUR {:.2f} e em GBP {:.2f}!".format(Real,Dólar,Euro,Libras))
