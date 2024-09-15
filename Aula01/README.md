Fórmula para o cálculo do módulo de um vetor tridimensional:
$$\left|\left|\vec v\right|\right| = \sqrt{v_i^2 + v_j^2 + v_k^2}$$

No nosso caso (vetor bidimensional):
$\vec v\ = v_x.i + v_y.j = (v_x, v_y)$

$\left|\left|\vec v\right|\right| = \sqrt{v_x^2 + v_y^2}$

$v_x = 5$
$v_y = 2.4$

$\vec v\ = 5.i + 2.4.j = (5, 2.4)$
$\left|\left|\vec v\right|\right| = \sqrt{5^2 + 2.4^2} = \sqrt{25 + 5.76} = \sqrt{30.76}$
$\left|\left|\vec v\right|\right| = 5.54$


Como chegamos na fórmula do vetor bidimensional?
Pensando em um plano com eixos x e y perpendiculares, temos que $v_x$ é sua magnitude no eixo x e $v_y$ é sua magnitude no eixo y. Aplicando o teorema de pitágoras, temos $\left|\left|\vec v\right|\right|^2 = v_x^2 + v_y^2$, $\left|\left|\vec v\right|\right| = \sqrt{v_x^2 + v_y^2}$

Código em python para a resolução do exercício:

```python
   import numpy as np

   v = np.array([5, 2.4])

  print(np.linalg.norm(v))
```

