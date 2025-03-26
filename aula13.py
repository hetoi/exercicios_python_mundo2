# print("Testando os comandos de FOR:")
# for c in range(0, 100, 20):
#     print(c)
# print("FIM")


print("Vamos contar até o número que você deseja. Contando apenas os números páres")
n = int(input("Digite um número: "))
for c in range(1, n+1, 2):
    print(c)
print("Fim!")

# Iterando (percorrendo) cada letra de uma string
palavra = "Joana"
for i in palavra: 
    print(i)

# Iterando um intervalo numérico
for i in range(1,10):
    print(i)

# Loop aninhado (for dentro de for)
for i in range(3):
    for j in range(2):
        print("i = {}, j = {}".format(i, j))

# Controlando fluxo com Break e Continue
# nesse caso a ordem dos fatores altera o resultado
# Se a condição if vier primeiro ele chega no 5 mas não imprime
for i in range(10):
    print(i)
    if i == 5:
        break # para o loop
    
# for precisa de uma sequência para iterar
# - Lista 
# - String
# - Range
# Em casos onde você quer iterar uma variável com um número int, pode usar range(1, variável+1)

#range(inicio,fim)
# onde fim é exclusivo, ou seja range lê fim como (fim - 1) 