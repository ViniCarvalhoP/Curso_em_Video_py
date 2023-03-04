n1 = int(input('Insira um número:'))
n2 = int(input('Insira outro número:'))
n3 = int(input('Insira outro número: '))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n2 and n3<n1:
    menor = n3
#Verificando quem é maior
    maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n2 and n3>n1:
    maior = n3
print('O menor número é: {}'.format(menor))
print('O maior número é: {}'.format(maior))
