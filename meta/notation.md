# Notation and parameter conventions

[Contents](../README.md)

| Symbol | Meaning | Typical units |
| --- | --- | --- |
| $t$ | Elapsed time or exposure coordinate | Hours |
| $e_i$ | Observed exposure of device $i$ | Hours |
| $N(t)$ | Number of events in $(0,t]$ | Count |
| $Y_i$ | Observed count for device $i$ | Count |
| $\lambda$ | A specified event rate | Per hour |
| $\Lambda$ | Random device rate or uncertain rate | Per hour |
| $\alpha$ | Gamma shape | Dimensionless |
| $\beta$ | Gamma rate parameter | Hours, when modelling a per-hour rate |
| $\mu$ | Expected count in a specified window | Dimensionless |
| $T$, $T_1$ | Event time, first-event time | Hours |
| $S(t)$ | Survival probability | Dimensionless |
| $F(t)$ | Cumulative event probability | Dimensionless |
| $f(t)$ | Event-time density | Per hour |
| $h(t)$ | Hazard conditional on survival | Per hour |
| $H(t)$ | Cumulative hazard | Dimensionless |
| $C$ | Censoring time | Hours |
| $X$ | Observed minimum of event and censoring times | Hours |
| $\delta$ | Indicator of an observed event | 0 or 1 |
| $\Gamma(\cdot)$ | Gamma function | Depends on argument |

## Gamma convention

$\operatorname{Gamma}(\alpha,\beta)$ always uses shape and **rate**. Its mean is $\alpha/\beta$. Libraries using a scale parameter need scale $1/\beta$.

The gamma distribution's rate parameter $\beta$ is distinct from the physical fault rate $\lambda$.

## Negative binomial convention

For shape $r>0$ and $0<p<1$, use

```math
P(Y=k)=\frac{\Gamma(k+r)}{\Gamma(r)k!}p^r(1-p)^k.
```

Its mean is $r(1-p)/p$. In the gamma–Poisson mixture, $r=\alpha$ and $p=\beta/(\beta+t)$ for $t>0$. At $t=0$, the count is zero with probability one.

## Conditioning

$P(A\mid B)$ means the probability of $A$ given information $B$. Conditional and marginal statements must not be interchanged: independent counts given a device rate may become dependent after averaging over that rate.
