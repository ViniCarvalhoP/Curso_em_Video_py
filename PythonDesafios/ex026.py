f = str(input('Digite uma frase: ')).upper().strip()
print ('A letra "a" aparece {} vezes na frase.'.format(f.count('A')))
print ('A letra "a" apareceu na posição {}'.format(f.find('A')))
print ('A letra "a" apareceu na posição {}'.format(f.rfind('A')))
