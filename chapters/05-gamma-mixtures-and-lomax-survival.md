# 5. Gamma mixtures: counts, first events, and survivor selection

[Previous](04-survival-and-hazard.md) · [Contents](../README.md) · [Simulation](../examples/02-gamma-lomax-simulation.py)

## One model, two observable quantities

Suppose each device draws a fixed, unobserved event rate at the beginning of observation:

$$
\Lambda\sim\mathrm{Gamma}(\alpha,\beta),
$$

where $\alpha>0$ is the dimensionless shape and $\beta>0$ is the **rate parameter** (with units of time when $\Lambda$ has units of inverse time). Conditional on $\Lambda=\lambda$, events follow a homogeneous Poisson process with rate $\lambda$.

We can ask two different questions about this same model:

1. How many events occur by time $t$?
2. How long until the first event?

These lead to different marginal distributions, but are mathematically linked.

## Counts: the negative binomial

For $k=0,1,2,\ldots$,

$$
P(N(t)=k\mid\Lambda=\lambda)
=\frac{e^{-\lambda t}(\lambda t)^k}{k!}.
$$

Integrating over the gamma distribution gives

$$
P(N(t)=k)=
\frac{\Gamma(k+\alpha)}{\Gamma(\alpha)k!}
\left(\frac{\beta}{\beta+t}\right)^\alpha
\left(\frac{t}{\beta+t}\right)^k.
$$

This is the negative binomial distribution, as derived in [Chapter 3](03-gamma-poisson-mixture.md).

## Time to first event: the Lomax distribution

Write $T_1$ for the first event time. Conditional on a fixed device rate,

$$
P(T_1>t\mid\Lambda=\lambda)=e^{-\lambda t}.
$$

Marginal survival is the average over rates:

$$
\begin{aligned}
S(t)
&=\int_0^\infty e^{-\lambda t}
\frac{\beta^\alpha}{\Gamma(\alpha)}
\lambda^{\alpha-1}e^{-\beta\lambda}\,d\lambda\\
&=\frac{\beta^\alpha}{\Gamma(\alpha)}
\frac{\Gamma(\alpha)}{(\beta+t)^\alpha}\\
&=\left(\frac{\beta}{\beta+t}\right)^\alpha.
\end{aligned}
$$

This is **Lomax (Pareto type II) survival** with shape $\alpha$ and scale $\beta$. The gamma distribution uses $\beta$ as a rate parameter, whereas the resulting Lomax distribution uses the same numerical $\beta$ as a time scale.

The density, cumulative hazard, and hazard are

$$
f(t)=\frac{\alpha\beta^\alpha}{(\beta+t)^{\alpha+1}},
$$

$$
H(t)=\alpha\log\left(1+\frac{t}{\beta}\right),
\qquad
h(t)=\frac{\alpha}{\beta+t}.
$$

Consequently,

$$
h'(t)=-\frac{\alpha}{(\beta+t)^2}<0.
$$

A heavy tail is another distinguishing feature: for large $t$, survival decreases approximately as $t^{-\alpha}$, rather than exponentially. The mean first-event time is finite only if $\alpha>1$.

## The exact connection: zero events

The first event has not happened by $t$ exactly when the event count is zero:

$$
\boxed{P(T_1>t)=P(N(t)=0).}
$$

Putting $k=0$ in the negative binomial formula reproduces the Lomax survival function. The identity itself holds for any ordinary counting process that starts with zero events, not just for Poisson or gamma mixtures.

**Important distinction:** $T_1$ is the *first event*, not necessarily terminal component failure. For a recurrent fault process, the device may continue operating after its first event. The probability of no faults is not automatically the probability of remaining operational.

## Why does the population hazard decrease?

Each device has constant individual hazard $\lambda$ for its first event. But the devices still event-free at time $t$ are not a random sample of the original population.

By Bayes' rule,

$$
g(\lambda\mid T_1>t)\propto
e^{-\lambda t}g(\lambda).
$$

For the gamma model, this yields

$$
\Lambda\mid T_1>t\sim\mathrm{Gamma}(\alpha,\beta+t).
$$

The average rate among event-free survivors is therefore

$$
E[\Lambda\mid T_1>t]=\frac{\alpha}{\beta+t}=h(t).
$$

High-rate devices tend to experience their first event early. Over time, the event-free population is increasingly dominated by low-rate devices. This is **survivor selection**, sometimes called *frailty selection*.

A decreasing population hazard therefore does **not** imply that any individual device is improving with age.

## A numerical example

Let $\alpha=2$ and $\beta=100$ hours. The initial mean device rate is $0.02$ events per hour.

| Elapsed time (hours) | Event-free fraction $S(t)$ | Population first-event hazard (per hour) |
| --- | --- | --- |
| 0 | 1.000 | 0.0200 |
| 50 | 0.444 | 0.0133 |
| 100 | 0.250 | 0.0100 |
| 200 | 0.111 | 0.0067 |

These numbers describe a changing *composition of survivors*, not aging-related improvement of a particular device.

## Simulate the mechanism

Run [the Python example](../examples/02-gamma-lomax-simulation.py) to draw one constant rate per device, sample its first-event time, and compare empirical survival with the theoretical Lomax curve. The example also compares the empirical survivor-average latent rate with the theoretical population hazard.

## What the model does not establish

Observing a decreasing hazard is not sufficient evidence for gamma heterogeneity. Genuine age-dependent hazards, unobserved covariates, selection effects, and observation mechanisms can produce similar patterns. Nor does a negative binomial fit to counts uniquely identify a gamma–Poisson mechanism.

The derivation describes a **generative explanation**, not a unique inference from observed data.
