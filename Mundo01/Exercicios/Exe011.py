# Faça um programa que leia a largura e a altura de uma parede em metros.
# Calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

lga = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))

result = lga * alt
result_litro = result / 2

print(
    f'Sua parede tem a dimensão de {lga} X {alt} e sua área é de {result}m2.')
print(f'Para pintar essa parede, você precisará de {result_litro}l de tinta.')
