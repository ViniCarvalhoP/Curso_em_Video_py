n = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(n)}')
print(f'Só tem espaços? {n.isspace()}')
print(f'É um número? {n.isnumeric()}')
print(f'É alfabético? {n.isalpha()}')
print(f'É alfanumérico? {n.isalnum()}')
print(f'Está em letra maiúscula? {n.isupper()}')
print(f'Está em letra minúsucla? {n.islower()}')
print(f'Está capitalizada? {n.istitle()}')
