import matplotlib.pyplot as plt
import math

quantEntradas = [100, 1000, 10000, 100000]
Bubble = [284, 17618, 1288670, 244596327]
Contagem = [236, 21007, 2012917, 195759227]
Heap = [127, 1623, 19236, 216151]
Insertion = [106, 8696, 414341, 37076095]
Merge = [42, 202, 1413, 13745]
Quick = [91, 1015, 12698, 114474]
Radix = [81, 715, 8243, 56570]
Selection = [140, 8179, 498981, 49296037]
Shell = [66, 989, 15074, 32719]

plt.title("Tempo de Execução (Vetor Aleatório)")
plt.xlabel("Quantidade de Elementos (n)")
plt.ylabel("Tempo (Milisegundos)")

# Plot each sorting algorithm
plt.plot(quantEntradas, Bubble, label='Bubble Sort', color='blue', marker='o')
plt.plot(quantEntradas, Contagem, label='Counting Sort', color='green', marker='s')
plt.plot(quantEntradas, Heap, label='Heap Sort', color='red', marker='^')
plt.plot(quantEntradas, Insertion, label='Insertion Sort', color='orange', marker='d')
plt.plot(quantEntradas, Merge, label='Merge Sort', color='purple', marker='x')
plt.plot(quantEntradas, Quick, label='Quick Sort', color='brown', marker='p')
plt.plot(quantEntradas, Radix, label='Radix Sort', color='pink', marker='H')
plt.plot(quantEntradas, Selection, label='Selection Sort', color='cyan', marker='*')
plt.plot(quantEntradas, Shell, label='Shell Sort', color='magenta', marker='v')

# Add a logarithmic scale for the y-axis to better view differences
plt.yscale('log')

# Display the legend in the upper left
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title="Algoritmos")
plt.tight_layout()

# Show the plot
plt.show()
