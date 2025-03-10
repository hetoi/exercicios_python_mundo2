# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input("Qual o valor da casa que você deseja comprar? "))
salario = float(input("Qual o seu salário? "))
anos = int(input("Em quantos anos deseja quitar a casa? "))
print("________________________________")
prestacoes = valor_casa/(anos * 12)

if prestacoes <= (salario * 0.3):
    print("Parabéns, você conseguiu o empréstimo!")
    print("Cada prestação ficará no valor de R$ {:.2f}".format(prestacoes))
else: 
    print("Infelizmente o valor da prestação excede 30% do seu salário")
    print("Valor da prestação: R$ {:.2f}".format(prestacoes))
    print("Limite de 30% do seu salário: R$ {:.2f}".format(salario * 0.3))