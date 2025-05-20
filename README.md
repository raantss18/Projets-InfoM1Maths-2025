## Projet 10 "Série de Fourier"

- La série de Fourier permet d'approximer une fonction périodique $f(x)=x$ par une somme infinie de $cosinus$ et $sinus$.
  $$S_N(x)=\frac{a_0}{2}+\sum_{n=1}^{N}\left(a_n\cos(nx)+b_n\sin(nx)\right)$$

- Les coefficients de Fourier sont donnés par :
$$a_n=\fract{1}{\pi}\int_{-\pi}^{\pi}f(x)\cos(nx)\dx$$
$$b_n=\fract{1}{\pi}\int_{-\pi}^{\pi}f(x)\sin(nx)\dx$$

## Phénomène de Gibbs

- Lorsque $f(x)$ présente une **discontinuité** , la série de Fourier **Oscille** près de cette discontinuité et depasse la vraie valeur.
- Ce phénomène est appelé " phénomène de Gibbs" .

## Observation

- Les oscillations ne disparaissent jamais , même en augmente $N$ .
- L'erreur est environ 10% d'erreur de la discontinuité.
- Visible dans l' approximation de la fonction en **signaux carrés** et **en marche d" escalier** .


## Conclusion 
Pour tracer cette courbe , on va utiliser les bibliothèques python ( numpy et matplotlib,...)



