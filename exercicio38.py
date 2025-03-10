# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais


# Recebendo os valores
print("Olá, vmaos comparar dois números?")
valor_a = int(input("Digite um valor: "))
valor_b = int(input("Digite outro valor: "))

# Comparando valores
if valor_a > valor_b:
    print("O PRIMEIRO valor é maior!")
elif valor_b > valor_a:
    print("O SEGUNDO valor é maior!")
else:
    print("Os valores são iguais!")