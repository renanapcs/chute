import random

class ChuteCerto:
    def __init__(self):
        self.numero_aleatorio = random.randint(1, 100)

    def chuteNumero(self):
        while True:
            numero_input = int(input('Chute um numero: '))
            if self.numero_aleatorio == numero_input:
                print("parabens Você acertou!")
                break
            elif numero_input > self.numero_aleatorio:
                print("Um pouco menor")
            else:
                print("Um pouco maior")

chute = ChuteCerto()

chute.chuteNumero()