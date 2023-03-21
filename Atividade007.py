# Desenvolva um prpframa que leia o nome de uma pessoa, peso, altura, calcule o IMC
# e mostre seu status, de acordo com a tabela abaixo:
# - IMC < 18,5: Abaixo do peso
# - IMC >= 18,5 e < 25: Peso ideal
# - IMC >= 25 e < 30: Sobrepeso
# - IMC >= 30 e < 40: Obesidade
# - IMC >= 40: Obesidade Mórbida

# IMC = peso / (altura * altura)

pessoa = input("Qual é o seu nome? ")
peso = float(input("Qual é o seu peso em Kilogramas? "))
altura = float(input("Qual é a sua altura em Metros? "))

IMC = peso / (altura*altura)

print("O IMC de {} é {:.2f}".format(pessoa, IMC))

if IMC < 18.5:
    print("Então {} está ABAIXO DO PESO!".format(pessoa))

elif IMC >= 18.5 and IMC < 25:
    print("Então {} está com PESO IDEAL!".format(pessoa))

elif IMC >= 25 and IMC < 30:
    print("Então {} está com SOBREPESO!".format(pessoa))

elif IMC >= 30 and IMC < 40:
    print("Então {} está com OBESIDADE MÓRBIDA!".format(pessoa))
