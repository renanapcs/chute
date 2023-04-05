# Iniciar o programa gerar um numero de 1 a 10 aleatorio.
# usuario input um numero.
# numero do input < > ou = ao numero aleatorio gerado pelo sistema.
# if for = mensagem('voce acertou')
# if for < ou > mensagem('numero ${< menor} ou numero ${> maior} ')

import random

#Gera um numero aleatorio.
numero_aleatorio = random.randint(1, 10)

#Repetir até que o usario acerte o numero
while True:
    numero_usuario = int(input("digite um numero: "))#int para numeros inteiro. sen o int o numero é uma string.
    if numero_usuario == numero_aleatorio:
        print('Você acertou! parabens.')
        break #Encerra o programa se o usuario acertar o numero.
    else:
        if numero_usuario < numero_aleatorio:
            print('um pouco maior')
        elif numero_usuario > numero_aleatorio:
            print('um pouco menor')
