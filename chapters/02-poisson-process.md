# 2. The Poisson process: counts and waiting times

[Previous](01-events-and-exposure.md) · [Contents](../README.md) · [Next](03-gamma-poisson-mixture.md)

## The question

What model connects a constant fault rate to both the number of faults and the time between faults?

## A process, not just a distribution

Let $N(t)$ count faults in $(0,t]$, with $N(0)=0$. A homogeneous Poisson process with rate $\lambda>0$ has:

1. Independent counts in disjoint time intervals.
2. Interval-count distributions that depend only on interval length.
3. For a short interval of length $\Delta t$, probability $\lambda\Delta t+o(\Delta t)$ of one event and $o(\Delta t)$ of two or more events.

Here $o(\Delta t)$ denotes a term whose ratio to $\Delta t$ approaches zero as $\Delta t$ approaches zero.

These assumptions imply

$$
N(t)\sim\mathrm{Poisson}(\lambda t),
\qquad
P(N(t)=k)=e^{-\lambda t}\frac{(\lambda t)^k}{k!},
$$

for $k=0,1,2,\ldots$, with

$$
E[N(t)]=\mathrm{Var}(N(t))=\lambda t.
$$

The distribution describes a count in one window. The process additionally describes how counts relate across windows.

## Deriving the first-event distribution

Let $T_1$ be the time until the first event. The first event occurs after $t$ exactly when there are no events by $t$:

$$
P(T_1>t)=P(N(t)=0)=e^{-\lambda t}.
$$

Thus $T_1$ has an exponential distribution with rate $\lambda$, mean $1/\lambda$, and constant hazard $\lambda$.

Every successive interarrival time has the same exponential distribution, and the interarrival times are independent. This statement concerns successive events in this process; a model where each failure permanently removes the device needs a different description after the first failure.

## Numerical example

If $\lambda=0.02$ faults per hour and $t=50$ hours, then $\lambda t=1$:

- Expected count: 1.
- Probability of zero faults: $e^{-1}\approx0.3679$.
- Probability of at least one fault: $1-e^{-1}\approx0.6321$.
- Mean waiting time: 50 hours.

An expected count of one does not mean an event is certain.

## Memorylessness

For $s,t\geq0$,

$$
P(T_1>s+t\mid T_1>s)=e^{-\lambda t}.
$$

Surviving without a fault for $s$ hours does not change the remaining waiting-time distribution **when the constant rate is known and the model holds**.

If devices have different unknown rates, surviving without a fault can change what we infer about the device's rate. The next chapter shows why the population then behaves differently.

## When the model is too simple

Equal mean and variance is a prediction for repeated counts at the same exposure under the same rate. Raw counts from unequal exposures need not have equal empirical mean and variance.

Counts may vary more than a common-rate Poisson model predicts, even when exposure is the same. Possible explanations include different rates across devices, events occurring in clusters, changing operating conditions, or observation errors. Excess variation alone does not identify which explanation is responsible.

The next chapter develops one of these possibilities: each device follows a Poisson process, but its rate can differ from those of other devices. We will derive the resulting count distribution from that assumption.
