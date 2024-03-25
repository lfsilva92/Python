# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
num = int(input('Digite um número: '))
ant = (num - 1)
pos = (num + 1)
print(
    f'Analisando o número {num}, seu antecessor é {ant} e o sucessor é {pos}')
