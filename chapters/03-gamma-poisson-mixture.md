# 3. Gamma-distributed rates and negative binomial counts

[Previous](02-poisson-process.md) · [Contents](../README.md) · [Next](04-survival-and-hazard.md)

## The question

What if every device follows a constant-rate Poisson process, but different devices have different rates?

Draw a device rate $\Lambda$ once, then keep that rate fixed for that device. Conditional on the rate and a fixed exposure $t$,

$$
N(t)\mid\Lambda=\lambda\sim\operatorname{Poisson}(\lambda t).
$$

Across devices, suppose

$$
\Lambda\sim\operatorname{Gamma}(\alpha,\beta),
$$

using **shape** $\alpha>0$ and **rate** $\beta>0$, not scale:

$$
g(\lambda)=\frac{\beta^\alpha}{\Gamma(\alpha)}
\lambda^{\alpha-1}e^{-\beta\lambda},\qquad \lambda>0.
$$

Here $\Gamma$ is the gamma function. The rate distribution has

$$
E[\Lambda]=\frac{\alpha}{\beta},\qquad
\operatorname{Var}(\Lambda)=\frac{\alpha}{\beta^2}.
$$

If $\Lambda$ is measured per hour, $\beta$ has units of hours and $\alpha$ is dimensionless.

## Integrate over rates

To obtain a count distribution for a randomly selected device, average the conditional Poisson probability over the gamma distribution:

$$
\begin{aligned}
P(N(t)=k)
&=\int_0^\infty
\frac{e^{-\lambda t}(\lambda t)^k}{k!}
\frac{\beta^\alpha}{\Gamma(\alpha)}
\lambda^{\alpha-1}e^{-\beta\lambda}\,d\lambda\\
&=\frac{\beta^\alpha t^k}{k!\Gamma(\alpha)}
\frac{\Gamma(k+\alpha)}{(\beta+t)^{k+\alpha}}\\
&=\frac{\Gamma(k+\alpha)}{\Gamma(\alpha)k!}
\left(\frac{\beta}{\beta+t}\right)^\alpha
\left(\frac{t}{\beta+t}\right)^k.
\end{aligned}
$$

This is a negative binomial distribution. Its shape need not be an integer. Because negative binomial conventions vary, the probability formula above defines the convention used here.

Writing $\mu=\alpha t/\beta$ gives

$$
E[N(t)]=\mu,\qquad
\operatorname{Var}(N(t))=\mu+\frac{\mu^2}{\alpha}.
$$

At fixed $\mu$, smaller $\alpha$ means more heterogeneity and more overdispersion. As $\alpha$ grows with $\mu$ fixed, the distribution approaches Poisson.

## Where does the extra variance come from?

The law of total variance gives

$$
\operatorname{Var}(N(t))
=E[\operatorname{Var}(N(t)\mid\Lambda)]
+\operatorname{Var}(E[N(t)\mid\Lambda])
=tE[\Lambda]+t^2\operatorname{Var}(\Lambda).
$$

The first term is Poisson variation within a given rate. The second is variation between rates.

## Counts across windows become dependent

For two disjoint windows of lengths $t_1$ and $t_2$ on the same device, let their counts be $Y_1$ and $Y_2$. Conditional on its rate, they are independent. Marginally,

$$
\operatorname{Cov}(Y_1,Y_2)
=t_1t_2\operatorname{Var}(\Lambda)>0.
$$

A high-rate device tends to have high counts in both windows. Drawing a new independent rate in every window would be a different process, even if each individual window had the same negative binomial marginal distribution.

## Heterogeneity and uncertainty are different interpretations

A gamma distribution can represent physical variation across device rates. It can also represent uncertainty about one unknown rate in Bayesian inference.

Both lead to a gamma–Poisson mixture, but the predictive question differs: are we selecting a new device from a population, or predicting more observations from the same device after learning from its history?

With a gamma prior and an observed count $k$ over exposure $t$, the posterior is $\operatorname{Gamma}(\alpha+k,\beta+t)$ under the fixed-exposure Poisson likelihood. When analysing a particular device under a population model, its history similarly updates its individual rate distribution.

## Check your understanding

Take $\alpha=2$, $\beta=100$ hours and $t=50$ hours. Find the mean count, variance, and probability of no faults.

**Answer:** The mean is 1; the variance is 1.5; the zero probability is $(100/150)^2=4/9\approx0.4444$. A common-rate Poisson model with the same mean has zero probability $e^{-1}\approx0.3679$. The mixture produces more zeros as well as a heavier upper tail.
