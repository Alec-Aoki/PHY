<p dir="ltr" style="text-align:left;"><span style="color: rgb(239, 69, 64); --darkreader-inline-color: #9c3330;" data-darkreader-inline-color="">EM VERMELHO: Comentários do monitor Gustavo.</span>
</p>
<p dir="ltr" style="text-align:left;">Fórmula para o cálculo do módulo de um vetor tridimensional:
  <br>$$\left|\left|\vec v\right|\right| = \sqrt{v_i^2 + v_j^2 + v_k^2}$$
  <br>
  <br>No nosso caso (vetor bidimensional):
  <br>$\vec v\ = v_x.i + v_y.j = (v_x, v_y)$
  <br>
  <br><span style="color: rgb(239, 69, 64); --darkreader-inline-color: #9c3330;" data-darkreader-inline-color="">Quando você decompõe o vetor em vetores unitários, precisa indicar o i, j e k com chapéu ou em negrito: $v_{x}\hat{i} + v_{y}\hat{j}$</span>
  <br>
  <br>$\left|\left|\vec v\right|\right| = \sqrt{v_x^2 + v_y^2}$</p>
<p dir="ltr" style="text-align:left;"><span style="color: rgb(239, 69, 64); --darkreader-inline-color: #9c3330;" data-darkreader-inline-color="">Você pode abreviar o comando de módulo para \left\|, assim: $\left\| \vec v \right\|$</span>
</p>
<p dir="ltr" style="text-align:left;">$v_x = 5$
  <br>$v_y = 2.4$
  <br>
  <br>$\vec v\ = 5.i + 2.4.j = (5, 2.4)$
  <br>$\left|\left|\vec v\right|\right| = \sqrt{5^2 + 2.4^2} = \sqrt{25 + 5.76} = \sqrt{30.76}$
  <br>$\left|\left|\vec v\right|\right| = 5.54$
  <br>
  <br>
  <br>Como chegamos na fórmula do vetor bidimensional?
  <br>Pensando em um plano com eixos x e y perpendiculares, temos que $v_x$ é sua magnitude no eixo x e $v_y$ é sua magnitude no eixo y. Aplicando o teorema de pitágoras, temos $\left|\left|\vec v\right|\right|^2 = v_x^2 + v_y^2$, $\left|\left|\vec v\right|\right|
  = \sqrt{v_x^2 + v_y^2}$
  <br>
</p>
<p dir="ltr" style="text-align:left;">Código em python para a resolução do exercício:</p>
<p dir="ltr" style="text-align:left;">&nbsp;&nbsp; import numpy as np</p>
<p dir="ltr" style="text-align:left;">&nbsp;&nbsp; v = np.array([5, 2.4])</p>
<p dir="ltr" style="text-align:left;">&nbsp; print(np.linalg.norm(v))</p><span style="color: rgb(239, 69, 64); --darkreader-inline-color: #9c3330;" data-darkreader-inline-color="">Compilou certinho! :)</span>
<br>
<p></p>