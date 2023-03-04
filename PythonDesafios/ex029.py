km = int(input('Quantos km/h seu carro está?'))
#m = km = 80
if km <= 80:
    print('Você não será multado')
else:
    print('Você foi multado, no valor de {}'.format((km-80)*7))
