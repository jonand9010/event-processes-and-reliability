# 4. Survival, hazard, and what observation hides

[Previous](03-gamma-poisson-mixture.md) · [Contents](../README.md) · [Worked example](../examples/01-fleet-example.md)

## The question

How do we describe time to failure, including devices that have not failed when observation ends?

Let $T\geq0$ be time to the event of interest. For a continuous event-time distribution, define:

$$
S(t)=P(T>t),\qquad F(t)=1-S(t),\qquad f(t)=F'(t).
$$

Here $S$ is the survival function, $F$ is the cumulative distribution function, and $f$ is the probability density.

The hazard is the instantaneous event rate conditional on survival:

$$
h(t)=\lim_{\Delta t\downarrow0}
\frac{P(t<T\leq t+\Delta t\mid T>t)}{\Delta t}
=\frac{f(t)}{S(t)}.
$$

Its units are inverse time. It is not a probability and can exceed 1 per unit time. Over a sufficiently short interval, the conditional event probability is approximately $h(t)\Delta t$.

The cumulative hazard is

$$
H(t)=\int_0^t h(u)\,du,
\qquad S(t)=e^{-H(t)},
$$

assuming an absolutely continuous distribution with $S(0)=1$ on the time range considered.

## The Poisson connection

For the first event of a homogeneous Poisson process,

$$
S(t)=e^{-\lambda t},\qquad H(t)=\lambda t,\qquad h(t)=\lambda.
$$

More generally, a nonhomogeneous Poisson process with deterministic intensity $\lambda(u)$ has first-event survival

$$
S(t)=\exp\left(-\int_0^t\lambda(u)\,du\right).
$$

The first-event hazard equals that intensity. An arbitrary recurrent-event process need not have this property: its event intensity can depend on the complete event history.

## Gamma heterogeneity creates decreasing population hazard

Under the previous chapter's model, draw a rate once per device and let $T$ denote its first-event time. Then

$$
S(t)=E[e^{-\Lambda t}]
=\left(\frac{\beta}{\beta+t}\right)^\alpha,
$$

which is Lomax survival, also called Pareto type II, with shape $\alpha$ and scale $\beta$. Therefore

$$
H(t)=\alpha\log\left(1+\frac{t}{\beta}\right),
\qquad h(t)=\frac{\alpha}{\beta+t}.
$$

Every device has a constant conditional hazard. Yet the population hazard decreases: high-rate devices tend to experience their first event earlier, leaving a lower-rate group among those still event-free.

Equivalently, the rate distribution among survivors is $\mathrm{Gamma}(\alpha,\beta+t)$, whose mean is $\alpha/(\beta+t)$.

**A decreasing population hazard does not establish that individual devices improve with age.**

## Right censoring

Let $C$ be the time observation ends. We observe

$$
X=\min(T,C),\qquad \delta=\mathbf{1}\{T\leq C\}.
$$

The indicator $\delta$ equals 1 for an observed event and 0 for right censoring. A censored record says the device survived through $X$; it does not say that it will never fail.

Under independent censoring, or suitable conditional independent censoring given included covariates, the contribution to the event-time likelihood is

$$
f(X)^\delta S(X)^{1-\delta}.
$$

This omits factors involving only the censoring mechanism. If disappearance from monitoring is associated with unobserved failure risk, this simplification may not be justified.

For example, a device observed event-free for 50 hours contributes $S(50)$. Deleting that record discards evidence and can distort the estimated lifetime distribution.

## Check your understanding

Under $\alpha=2$ and $\beta=100$ hours, compare the population first-event hazard at ages 0 and 100 hours. Has any device's own rate changed?

**Answer:** The hazards are 0.02 and 0.01 per hour. Individual rates have not changed in this model. The distribution of rates among devices still event-free has changed.
