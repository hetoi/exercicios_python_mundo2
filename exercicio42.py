# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

r1= float(input("Pimeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

# If dentro de if
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos PODEM FORMAR um triângulo ", end="")
    if r1 == r2 == r3:
        print("EQUILÁTERO!")
        
    # importante colocar condição de diferença entre r1 e r3
    elif r1 != r2 != r3 != r1:
        print("ESCALENO!")
    else:
        print("ISÓCELES!")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo.")