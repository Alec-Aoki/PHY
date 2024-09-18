import random

numeroGerado: int = random.randint(0, 100) #inclusivo
print(numeroGerado)
tentativas = []

while(True):
    n = int(input())
    tentativas.append(n)

    if(n > numeroGerado):
        print("Seu numero foi maior")
        continue
    if(n < numeroGerado):
        print("Seu numero foi menor")
        continue

    print("Numero acertado!")
    print(f"Suas tentativas ({len(tentativas)}): {tentativas}")
    break