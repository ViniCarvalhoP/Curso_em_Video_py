distancia = float(input('Qual a distância da sua viagem? '))
passagem = distancia * 0.50
if distancia <= 200:
    print('Sua passagem custará: R${:.2f}'.format(passagem))
else:
    print ('Sua passagem custará: R${:.2f}!.'.format(distancia*0.45))

