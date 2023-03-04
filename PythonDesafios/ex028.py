from random import randint
numero = randint(0,5)
chute = int(input('Em que número eu pensei?'))
if chute == numero:
    print('Parabéns, voce acertou!')
else:
    print('Você errou!')
if chute > numero:
    print ('Parabéns, você é um IDIOTA!')
