# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valor_produto = float(input('Qual é o preço do produto? R$'))

result = valor_produto * (5 / 100)

print(
    f'O produto que custava R${valor_produto}, na promoção com desconto de 5% vai custar R${result:.4f}l')
