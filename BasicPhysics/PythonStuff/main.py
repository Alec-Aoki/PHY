import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100) #100 valores entre 0 e 10
y = np.sin(x)

#plotando o gráfico:
plt.figure(figsize=(8,4))
plt.plot(x, y, label = 'Função sen(x)', color = 'C1', linewidth = 2)
plt.title('Função sen(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()