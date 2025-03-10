#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
# se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar 
# ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input("Digite o seu ano de nascimento: "))
idade = ano_atual - ano_nascimento
ano_de_alistamento = ano_nascimento + 18

print("Quem nasceu em {} tem {} anos em {}".format(ano_nascimento, idade, ano_atual ))

if idade < 18:
    anos_faltantes = 18 - idade
    print("Ainda faltam {} anos para o alistamento".format(anos_faltantes))
    print("Seu alistamento será em {}".format(ano_de_alistamento))
elif idade == 18:
    print("Você deve se alistar esse ano")
    print("Boa sorte!")
else:
    anos_passados = idade - 18
    print("Você tem mais de 18 anos!")
    print("Seu alistamento deveria acontecer em {}".format(ano_de_alistamento))
    print("Você está atrasado {} anos para o alistamento".format(anos_passados))
