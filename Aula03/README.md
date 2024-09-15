 Considere uma trajetória representada pela curva espacial descrita parametricamente pelo vetor posição $$ \vec{r} = x(t) \hat{i} + y(t) \hat{j} + z(t) \hat{k} $$ com as seguintes equações horárias:$ \begin{equation} x(t) = R \cos(\theta (t))\end{equation} \begin{equation} y(t) = R \sin(\theta (t))\end{equation} \begin{equation} z(t) = ct \end{equation} \begin{equation} \theta (t) = \omega t \end{equation}$ Onde $ R $, $ c $ e $ \omega $ são constantes e $ \displaystyle t \in \left[ 0, \frac{2 \pi}{\omega} \right] $.

Questão 1. Calcule o vetor velocidade $ \vec {v} $ e seu módulo.
Sendo a velocidade a taxa de variação do vetor posição (que define a trajetória) no parâmatro tempo, operação definida pela derivada, temos que suas componentes $v_x$, $v_y$ e $v_z$ são as derivadas das componentes $x$, $y$ e $z$ do vetor $\vec{r}$ (definidas a partir da função implícita $\theta = \omega t$). Assim, temos: $ \begin{align} \vec{v} = \frac{d}{dt} \vec{r} (t), \end{align} \begin{align} \vec{v} = v_x (t) \hat{i} + v_y (t) \hat{j} + v_z (t) \hat{k} = \frac{d}{dt} x(t) \hat{i} + \frac{d}{dt} y(t) \hat{j} + \frac{d}{dt} z(t) \hat{k}. \end{align} $
$ \begin{align} v_x (t) = \frac{d}{dt} x(t) = - R \omega \sin(\omega t), \end{align} \begin{align} v_y (t) = \frac{d}{dt} y(t) = R \omega \cos(\omega t), \end{align} \begin{align} v_z (t) = \frac{d}{dt} z(t) = c. \end{align}
\begin{align} \vec{v} = - R \omega \sin(\omega t) \hat{i} + R \omega \cos(\omega t) \hat{j} + c \hat{k}. \end{align}$

Por definição: $$\left\| \vec{A} \right\| = \sqrt{\vec{A} \cdot \vec{A}}.$$ Logo, assumindo uma base ortonormal: $\begin{align} \left\| \vec{v} \right\| = \sqrt{\vec{v} \cdot \vec{v}} = \sqrt{ v_x(t) v_x(t) + v_y(t) v_y(t) + v_z(t) v_z(t) } = \sqrt{ (-R \omega \sin(\omega t))^2 + (R \omega \cos(\omega t))^2 + c^2 } = \sqrt{ R^2 \omega^2 (\sin(\omega t))^2 + R^2 \omega^2 (\cos(\omega t))^2 + c^2 } = \sqrt{ R^2 \omega^2 (\sin^2(\omega t) + \cos^2(\omega t)) + c^2 }. \end{align} \begin{align} \left\| \vec{v} \right\| = \sqrt{ R^2 \omega^2 + c^2 }. \end{align} \begin{align} \displaystyle \left[ v \right] = \left[ \sqrt{ L^2 (\frac{1}{T})^2 } \right] = \left[ \frac{L}{T} \right]. \end{align}$ Nota-se que o módulo da velocidade não depende do tempo, isto é, ele é constante durante toda a trajetória. Isso nos indica que não há uma aceleração sobre a partícula que muda o módulo de sua velocidade.

Questão 2. Calcule o vetor aceleração $ \vec{a} $ e seu módulo.
Sendo aceleração a taxa de variação da velocidade no tempo (derivada de $ \vec{v} $ em $ t $), temos: $\begin{align} \vec{a} (t) = \frac{d}{dt} \vec{v} (t) = a_x (t) \hat{i} + a_y (t) \hat{j} + a_z (t) \hat{k} = \frac{d}{dt} v_x(t) \hat{i} + \frac{d}{dt} v_y(t) \hat{j} + \frac{d}{dt} v_z(t) \hat{k}. \end{align}$
$\begin{align} a_x (t) = \frac{d}{dt} v_x(t) = - R \omega^2 \cos(\omega t), \end{align} \begin{align} a_y (t) = \frac{d}{dt} v_y(t) = - R \omega^2 \sin(\omega t), \end{align} \begin{align} a_z (t) = \frac{d}{dt} v_z(t) = 0. \end{align}
\begin{align} \vec{a}(t) = - R \omega^2 \cos(\omega t) \hat{i} - R \omega^2 \sin(\omega t) \hat{j} + 0 \hat{k}. \end{align} Assumindo uma base ortonormal: \begin{align} \left\| \vec{a} \right\| = \sqrt{\vec{a} \cdot \vec{a}} = \sqrt{ a_x(t) a_x(t) + a_y(t) a_y(t) + a_z(t) a_z(t) } = \sqrt{ (-R \omega^2 \cos(\omega t))^2 + (-R \omega^2 \sin(\omega t))^2 + 0^2 } = \sqrt{ R^2 \omega^4 (\cos(\omega t))^2 + R^2 \omega^4 (\cos(\omega t))^2 + 0 } = \sqrt{ R^2 \omega^4 (\sin^2(\omega t) + \cos^2(\omega t)) } = \sqrt{ R^2 \omega^4 }. \end{align}
\begin{align} \left\| \vec{a} \right\| = R \omega^2. \end{align} \begin{align} \left[ a \right] = \left[ \frac{L}{T^2} \right]. \end{align}$ Nota-se que o módulo da aceleração não depende do tempo; isso significa que a partícula tem uma aceleração constante durante toda sua trajetória. No entanto, afirmamos no item anterior que a partícula não possui nenhuma aceleração alterando o módulo de sua velocidade. Isso se dá pois a aceleração presente é centrípeta, ou seja, aponta para o centro da trajetória (circular) e altera somente a direção da velocidade, e não o seu módulo.

Questão 3. i) Calcule o produto escalar entre os vetores aceleração e velocidade. Sendo o produto escalar, geometricamente, a projeção de um vetor sobre outro, temos que (assumindo uma base ortonormal): $\begin{align} \vec{A} \cdot \vec{B}  = (A_x, A_y, A_z) \cdot (B_x, B_y, B_z) = A_x B_x C_x + A_y B_y C_y + A_z B_z C_z. \end{align} Logo, temos: \begin{align} \vec{v}(t) \cdot \vec{a}t = v_x(t) a_x(t) + v_y(t) a_y(t) + v_z(t) a_z(t) = (- R \omega \sin(\omega t)) (- R \omega^2 \cos(\omega t)) + (R \omega \cos(\omega t)) (-R \omega^2 \sin(\omega t)) + c 0 = R^2 \omega^2 \sin(\omega t) \cos(\omega t) - R^2 \omega^2 \sin(\omega t) \cos(\omega t) = 0. \end{align} $ Logo, $ \vec{v} \cdot \vec{a} = 0 $. Temos, também por definição, $\displaystyle \vec{A} \cdot \vec{B} = \left\| \vec{A} \right\| \left\| \vec{B} \right\| \cos(\theta)$, $\theta = ang(\vec{A}, \vec{B}).$ Como temos $\left\| \vec{a} \right\| \neq 0$, $\left\| \vec{v} \right\| \neq 0$ e $ \vec{v} \cdot \vec{a} = 0 $, só nos resta $\cos(\theta) = 0$, o que nos dá $\displaystyle \theta = \frac{\pi}{2}$ ou $\displaystyle \theta = \frac{3 \pi}{2}$. Isso signifca que o vetor aceleração e velocidade são perpendiculares entre si o tempo inteiro ($ \vec{v} \cdot \vec{a} = 0 $, não variando com o tempo). Isso faz sentido, principalmente considerando que temos uma trajetória helicoidal em que a aceleração é centrípeta e seu vetor aponta sempre para o centro da trajetória, enquanto o vetor velocidade é sempre tangente à trajetória, sendo portanto perpendicular ao vetor aceleração.

ii) Sendo velocidade a taxa de variação do vetor posição (que define a trajetória) no tempo, operação dada pela derivada, temos que o comprimento da trajetória pode ser dada pela operação inversa (a integral) aplicada à velocidade. Logo: $ \begin{align} \Delta s = \int_{t_i}^{t_f} \left\| \vec{v} (t) \right\| dt = \int_{0}^{\frac{2 \pi}{\omega}} \sqrt{ R^2 \omega^2 + c^2 } dt = \sqrt{ R^2 \omega^2 + c^2 } \int_{0}^{\frac{2 \pi}{\omega}} dt = \sqrt{ R^2 \omega^2 + c^2 } \left[ t \right]_{0}^{\frac{2 \pi}{\omega}} = \sqrt{ R^2 \omega^2 + c^2 } \frac{2 \pi}{\omega}. \end{align}$
$\begin{align} \Delta s = \frac{2 \pi}{\omega}  \sqrt{ R^2 \omega^2 + c^2 }. \end{align} \begin{align} \left[ \Delta s \right] = \left[ T \frac{L}{T} \right] = \left[ L \right]. \end{align}$

iii) A distância entre as posições final $\vec{r} (t=T)$ e inicial $\vec{r} (t=0)$ é calculada como o módulo do vetor $\vec{r_L}$ que liga esses dois pontos:  $\begin{align} \vec{r} (T) = \vec{r} \left( \frac{2 \pi}{\omega} \right) = \left( R \cos \left(\omega \frac{2 \pi}{\omega} \right), R \sin \left( \omega \frac{2 \pi}{\omega} \right), c \frac{2 \pi}{\omega} \right) = \left( R \cos(2 \pi), R \sin(2 \pi), c \frac{2 \pi}{\omega} \right) = \left( R , 0, c \frac{2 \pi}{\omega} \right), \end{align} \begin{align} \vec{r} (0) = (R \cos(\omega 0), R \sin(\omega 0), c 0) = (R \cos(0), R \sin(0), 0) = (R, 0, 0). \end{align}$
$\begin{align} \vec{r_L} = \vec{r} \left( \frac{2 \pi}{\omega} \right) - \vec{r} (0) = \left( R , 0, c \frac{2 \pi}{\omega} \right) - (R, 0, 0) = \left( 0, 0, \frac{2 \pi c}{\omega} \right). \end{align} $

 Logo, a magnitude deste vetor é: $\begin{align} L = \left\| \vec{r_L} \right\| = \sqrt{ \vec{r_L} \cdot \vec{r_L} } = \sqrt{ 0^2 + 0^2 + \left( \frac{2 \pi c}{\omega} \right)^2 } = \sqrt{ \left( \frac{2 \pi c}{\omega} \right)^2 }, \end{align} \begin{align} L = \frac{2 \pi c}{\omega}. \end{align}$

iv) Há uma clara diferença entre o comprimento da trajetória e a distância entre a posição inicial e final da partícula. O comprimento da trajetória leva em conta a soma de todos os pontos da trajetória: se uma partícula, após se deslocar, retornar ao ponto de início do deslocamento, o comprimento dessa trajetória NÃO será nulo. Já a distância entre o ponto inicial e final da trajetória nada mais é que o menor segmento de reta possível que liga esses dois pontos, não levando em conta curvas ou "retornos" na trajetória. Se uma particula retorna ao ponto de início de seu deslocamento, a distância entre o ponto inicial e final será zero. Portanto, é possível dizer que o comprimento da trajetória é uma representação constantemente mais fiel do espaço percorrido pela partícula durante seu deslocamento que a mera distância entre seu ponto de início e término.

Questão 4. Curvatura é o quanto uma curva se diferencia de uma reta. Por definição temos que a curvatura é obtida a partir da componente perpendicular da derivada segunda do vetor posição ($\frac{d^2\vec{r}}{d^2t} = \frac{d\left\| \vec{v} \right\|}{dt} \hat{v} + (\left\| \vec{v} \right\|)^2 \kappa \hat{n}$), e portanto: $ \displaystyle \kappa (t) =  \frac{ \left\| \vec{v} \times \vec{a} \right\| }{ (\left\| \vec{v} \right\|)^3 } $ 

Produto vetorial é a operação que fornece um vetor simultaneamente perpendicular aos seus dois operandos. Por definição, $ \left\| \vec{v} \times \vec{a} \right\| = \left\| \vec{v} \right\| . \left\| \vec{a} \right\| . \sin(\theta), \theta = ang(\vec{v}, \vec{a}) $. Conforme notamos na questão 3, temos $ \theta = \frac{\pi}{2}.$ Disto temos: $\begin{align} \left\| \vec{v} \right\| = \sqrt{ R^2 \omega^2 + c^2 }, \end{align} \begin{align} \left\| \vec{a} \right\| = R \omega^2, \end{align} \begin{align} \theta = \frac{\pi}{2}. \end{align}$
$\begin{align} \kappa (t) = \frac{ \left\| \vec{v} \right\| \left\| \vec{a} \right\| \sin(\theta) }{ (\left\| \vec{v} \right\|)^3 } = \frac{ \left\| \vec{a} \right\| \sin(\theta) }{ (\left\| \vec{v} \right\|)^2 } = \frac{ R \omega^2 \sin( \frac{\pi}{2} ) }{ ( \sqrt{ R^2 \omega^2 + c^2 } )^2 } = \frac{ R \omega^2 }{ (R^2 \omega^2 + c^2 ) } = \frac{ R \omega^2 }{ R^2 \omega^2 + c^2 }. \end{align} \begin{align} \left[ \kappa (t) \right] = \left[ \frac{\frac{L}{T^2}}{\frac{L^2}{T^2}} \right] = \left[ \frac{1}{L} \right]. \end{align} $