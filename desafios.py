# Resolvendo desafios que pedi ao DeepSeek

# Crie um programa que pede um número inteiro N ao usuário 
# e calcula a soma de todos os números de 1 até N.

print("Vamos somar os números!")
numero = int(input("Digite o número:"))
saida = 0
for i in range(1, numero+1): 
    saida += i
print(saida)


# Faça um programa que conta quantas vogais (a, e, i, o, u) 
# existem em uma palavra digitada pelo usuário.
palavra = str(input("Digite uma palavra: "))
saida2 = 0

for i in palavra: 
    if i == "a":
        saida2 += 1
    elif i == "e":
        saida2 += 1
    elif i == "i":
        saida2 += 1
    elif i == "o":
        saida2 += 1
    elif i == "u":
        saida2 += 1
print(saida2)

# Versão melhorada dessa resposta:

palavra = str(input("Digite uma palavra: "))
vogais = ["a", "e", "i", "o", "u"]
contador = 0 

for letra in palavra:
    if letra in vogais:
        contador += 1

print(contador)


# solução paralela para o caso i == "a" or i == "e" or ...
# a primeira tentativa estava dando errado pois eu tentei i == "a" or "e" or "i"...
# observe que entre OR/AND fica a condição T ou F, "'e' or 'i'" não está apto pra ser T ou F