from calendar import isleap
ano = int(input('Diga um ano e descubra se ele é bissexto ou não: '))
if isleap(ano):
    print('Sim, seu ano é um ano bissexto!')
else:
    print('Não, seu ano não é bissexto!')


# ano = int(input('Digite um ano e descubra se ele é bissexto ou não: '))
# if (ano%4==0 and ano%100!=0) or (ano%400==0):
#     print('É bissexto!') 
# else:
#     print('Não é bissexto!')