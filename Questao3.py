from random import randint
Q = []
for numero in range(20):
    Q.append(randint(a=1, b=100))

# Variável de Controle
maior = -1
menor = 101

for item_da_lista in Q:
    if maior < item_da_lista:
        maior = item_da_lista
    if menor > item_da_lista:
        menor = item_da_lista

print('Lista de Números')
print(Q)
print(f'O maior valor é: {maior}')
print(f'O menor valor é: {menor}')

# Funções de máximo e mínimo
print(max(Q))
print(min(Q))