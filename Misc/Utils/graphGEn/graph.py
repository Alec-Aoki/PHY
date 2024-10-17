import matplotlib.pyplot
import math

quantEntradas = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
tempo1 = [0.000032, 0.000051, 0.000087, 0.000259, 0.001541, 0.010502, 0.082572, 0.730486, 6.631656, 77.403269]
#tempo = [math.factorial(3), math.factorial(4), math.factorial(5), math.factorial(6), math.factorial(7), math.factorial(8), math.factorial(9), math.factorial(10), math.factorial(11), math.factorial(12)]
tempo2 = [0.000001, 0.000001, 0.000004, 0.000013, 0.000063, 0.000440, 0.003713, 0.035417, 0.391957, 4.284960]


matplotlib.pyplot.xlabel("n")
matplotlib.pyplot.ylabel("Segundos")
matplotlib.pyplot.plot(quantEntradas, tempo1, label='Força Bruta', color='blue')
matplotlib.pyplot.plot(quantEntradas, tempo2, label='Otimizado', color='red')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()