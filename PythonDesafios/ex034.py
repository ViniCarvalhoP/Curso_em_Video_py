salario = float(input('Digite seu salário: R$'))
if salario > 1250.00:
    aumento1 = salario + (salario*10/100)
    print('Seu salário pasará a ser R${:.2f}'.format(aumento1))
else:
    m = (salario+(salario*15/100))
    print ('Seu salário passará a ser R${:.2f}'.format(m))
