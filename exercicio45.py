# Crie um programa que faça o computador jogar Jokenpô com você.

import random
from time import sleep

print("""
SUAS OPÇÕES: 
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
""")

escolha_jogador = int(input("Qual a sua jogada? "))
escolha_programa = random.randint(1,3)
if escolha_jogador <= 3:
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!!")
    
    if escolha_jogador == escolha_programa :
        mensagem = "O jogo EMPATOU!"
    elif escolha_jogador == 1 and escolha_programa == 2:
        mensagem = "O jogador PERDEU"
    elif escolha_jogador == 1 and escolha_programa == 3:
        mensagem = "O jogador GANHOU"
    elif escolha_jogador == 2 and escolha_programa == 3: 
        mensagem = "O jogador PERDEU" 
    
    # É preciso .format dos prints seguintes 
    # Quebrar a linha da mensagem 
    print("COMPUTADOR JOGOU {}".format(escolha_jogador))
    print("JOGADOR JOGOU {}".format(escolha_programa))
    print(str(mensagem))

else:
    print("OPÇÃO INVÁLIDA!")
 



