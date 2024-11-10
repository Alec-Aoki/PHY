import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def update(frame):
  line.set_data(t[:frame], x[:frame])
  return line,

def sistemaMassaMola(A, w, fase, quantPontos, tMax):
  """
  Calcula a trajetória de um sistema massa-mola sem viscosidade.
  Parâmetros:
    A: Amplitude do movimento
    w: Frequência de oscilação do sistema
    fase: Fase inicial do corpo no sistema
    quantPontos: Quantidade de pontos que serão plotados no gráfico
    tMax: Tempo máximo de simulação (em segundos)
  Retorna:
    x: Vetor da posição do corpo (o movimento ocorre ao longo de somente um eixo)
    t: Vetor de tempo para o movimento do corpo
  """

  t = np.linspace(0, tMax, num=quantPontos)

  x = A * np.cos(w*t + fase)

  return x, t


faseInicial = 0
amplitude = 10
freqInicial = 5
tempoMax = 5
quantPontos = 500

x, t = sistemaMassaMola(amplitude, freqInicial, faseInicial, quantPontos, tempoMax)

fig, ax = plt.subplots()
line, = ax.plot(t, x)

#plt.plot(t, x, lw=2, color='red')
plt.xlabel('t (s)')
plt.ylabel('x(t) (m)')
plt.title('Oscilador Harmônico (Sistema Massa-Mola) Sem Resistência do Ar')
#plt.grid(True)
#plt.show()

ax.set_xlim((0, 5))
ax.set_ylim((-10, 10))

ani = FuncAnimation(fig, update, frames = 1000, interval = 50)
plt.show()