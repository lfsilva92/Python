# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import acos as c1, asin as s1, atan as t1, radians as r

angulo = float(input('Digite o angulo que você deseja: '))
seno = s1(r(angulo))
cosseno = c1(r(angulo))
tangente = t1(r(angulo))

print(f'O angulo de {angulo} tem o SENO de {seno:.2f}')
print(f'O angulo de {angulo} tem o COSSENO de {cosseno:.2f}')
print(f'O angulo de {angulo} tem a TANGENTE de {tangente:.2f}')
