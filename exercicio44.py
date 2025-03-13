# Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

preco = float(input("Qual o valor da compra? R$"))
print("FORMAS DE PAGAMENTO")
print("[1] à vista dinheiro/cheque")
print("[2] à vista no cartão")
print("[3] 2x no cartão")
print("[4] 3x ou mais no cartão")
pagamento = int(input("Qual a opção? "))

if pagamento == 1:
    preco = preco*0.9
    print("O valor da compra será de RS{}".format(preco))
elif pagamento == 2:
    preco = preco * 0.95
    print("O valor da compra será de R${}".format(preco))
elif pagamento == 3:
    parcela = (preco/2)
    print("Cada parcela ficará no valor de R${}".format(parcela))
elif pagamento == 4:
    qtd_parcelas = int(input("Em quantas parcelas? "))
    parcela = (preco*1.2)/qtd_parcelas
    print("Em {} parcelas, cada uma ficará no valor de R${}.".format(qtd_parcelas, parcela))
