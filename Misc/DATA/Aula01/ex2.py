while(True):
    tamPiramide = int(input())
    if(tamPiramide > 0):
        break

for i in range(tamPiramide):
    for _ in range(tamPiramide - (i+1)): #_ pois essa variável não será usada dentro do loop
        print(" ", end = "")

    for _ in range(i+1):
        print("#", end = "")

    print("")

#ou:
#for i in range(tamPiramide):
#    print(" " * (tamPiramide - (i + 1) + "#" * (i + 1)))