# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual é o salário do Funcionário R$'))

result = salario * (15 / 100)
salario_aumento = salario + result

print(
    f'Um funcionário que ganhava R${salario}, com 15% de aumento, passa a receber R${salario_aumento:.2f}')
