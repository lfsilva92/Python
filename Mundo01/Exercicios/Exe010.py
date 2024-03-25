# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
real = float(input('Quanto dinheiro você tem na carteira? R$'))
# Dolar em 19/03/2024 - 5.02
dolar = float(real / 5.02)
print(f'Com R${real} você pode comprar US${dolar:.2f}')
