# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
n = int(input('Digite um número para ver sua tabuada: '))
print('----------')
for i in range(11):
    r = (n * i)
    print(f'{n} x {i} = {r}')
print('----------')
