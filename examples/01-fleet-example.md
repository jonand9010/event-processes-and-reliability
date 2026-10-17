# One fleet, three different questions

[Contents](../README.md)

Consider independent devices. Each has a rate drawn once from $\operatorname{Gamma}(2,100)$, using shape–rate parameters and hours as exposure. Given its rate, each device follows a homogeneous Poisson process. All devices are observed from a common age zero; exposure windows below are fixed in advance.

## 1. How many events in the next 50 hours for a new device?

Before observing its history, the predictive count is negative binomial:

$$
E[N(50)]=1,\qquad \operatorname{Var}(N(50))=1.5.
$$

The probability of at least one event is

$$
1-\left(\frac{100}{150}\right)^2=\frac59\approx0.5556.
$$

Using a Poisson distribution at the mean rate 0.02 would instead give $1-e^{-1}\approx0.6321$. Averaging rates before calculating probabilities does not generally preserve the probabilities.

## 2. How likely is a first event in the next 50 hours after 100 event-free hours?

The device has provided information: its rate distribution, conditional on that event-free history, is $\operatorname{Gamma}(2,200)$.

The conditional probability is

$$
1-\frac{S(150)}{S(100)}
=1-\left(\frac{200}{250}\right)^2
=0.36.
$$

This is lower than for a new device. The observation changed our information about its rate.

## 3. What if it had four events in those 100 hours?

Its posterior rate distribution is $\operatorname{Gamma}(6,200)$, with mean 0.03 events per hour. Assuming events do not alter its underlying rate, the expected count in the next 50 hours is

$$
50\frac6{200}=1.5.
$$

The probability of at least one additional event is

$$
1-\left(\frac{200}{250}\right)^6
\approx0.7379.
$$

This is a recurrent-event question, not the probability of its first event: its first event already occurred.

## What to carry forward

| Available history | Rate distribution used for prediction | Probability of an event in next 50 h |
| --- | --- | --- |
| New device | Gamma(2, 100) | 0.5556 |
| No events in first 100 h | Gamma(2, 200) | 0.3600 |
| Four events in first 100 h | Gamma(6, 200) | 0.7379 |

All three calculations use the same generative model. They differ in the observed history and the question being asked.
