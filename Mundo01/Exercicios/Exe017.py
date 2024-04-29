# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

from math import hypot as h

cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))

print(f'A hipotenusa vai medir {h(cateto_oposto, cateto_adjacente):.2f}')
