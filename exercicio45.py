# Crie um programa que faça o computador jogar Jokenpô com você.

import random
from time import sleep

# Mensagem inicial
print("""
SUAS OPÇÕES: 
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
""")

# Opção que o jogador escolheu
escolha_jogador = int(input("Qual a sua jogada? "))

if escolha_jogador >= 1 and escolha_jogador <= 3:
    escolha_programa = random.randint(1,3)
    
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!!")
    
    # Todas as coombinações possíveis
    # Jogador tem três opções de escolha, em cada uma ele pode ganhar, perder, ou empatar

    # Caso empate
    if escolha_jogador == escolha_programa :
        mensagem = "O jogo EMPATOU!"

    # Caso ganhe
    elif (escolha_jogador == 1 and escolha_programa == 3) or \
         (escolha_jogador == 2 and escolha_programa == 1) or \
         (escolha_jogador == 3 and escolha_programa == 2):
        mensagem = "O jogador GANHOU"
    # Caso perca
    else: 
        mensagem = "O jogador PERDEU" 
    
    # Mensagem retornano resultado
    print("O JOGADOR JOGOU {}".format(escolha_jogador))
    print("COMPUTADOR JOGOU {}".format(escolha_programa))
    print(mensagem)

else:
    # Casos em que a não se escolhe entre 1 e 3
    print("OPÇÃO INVÁLIDA!")
 



