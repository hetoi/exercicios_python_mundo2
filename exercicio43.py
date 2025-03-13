# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
# calcule seu Índice de Massa Corporal (IMC) 
# e mostre seu status, de acordo com a tabela abaixo:

# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

peso = float(input("Qual o seu peso? (kg) "))
altura = float(input("Qual a sua altura? (m) "))
imc = peso/(altura**2)
print("O IMC dessa pessoa é {:.2f}".format(imc))

if imc < 18.5:
    print("Você está Abaixo do Peso")
elif 18.5 <= imc < 25:
    print("Parabéns, você está no Peso Ideal")
elif 25 <= imc < 30:
    print("Ops, parece que você está com sobrepeso")
elif 30 <= imc <= 40:
    print("Eita, você está com obesidade!")
else:
    print("Você está com Obesidade Mórbida! ")