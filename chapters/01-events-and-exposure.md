# 1. Events, exposure, and the questions we ask

[Contents](../README.md) · [Next: Poisson process](02-poisson-process.md)

## The question

A fleet records 20 faults this week. Is that a lot?

The count alone cannot answer this. Twenty faults during 100 operating hours tells a different story from twenty faults during 100,000 operating hours.

Before selecting a distribution, define what can produce an event, what counts as an event, and how much opportunity there was to observe it.

## Define the observation

For device $i$, write:

- $Y_i$: the observed number of faults.
- $e_i$: observed exposure, such as operating hours.
- $\lambda_i$: its expected event rate per unit exposure under the model.

A basic model is

$$
Y_i\mid\lambda_i,e_i\sim\operatorname{Poisson}(\lambda_i e_i).
$$

The product $\lambda_i e_i$ is dimensionless and is the expected count. A rate of 0.02 faults per hour over 100 hours gives an expected count of 2.

Exposure need not be calendar time. It could be kilometres, requests, or operating cycles. The exposure scale is a modelling choice: using kilometres assumes that a kilometre is the relevant unit of opportunity, perhaps after accounting for operating conditions.

## Three different questions

| Question | Observation | Starting point |
| --- | --- | --- |
| How many faults occur during operation? | Count and exposure | Count model |
| How long until the first failure? | Event or censoring time | Survival model |
| How do faults recur after repair? | Ordered event times and repair history | Recurrent-event or renewal model |

One device can contribute many fault events but only one first failure. A terminal failure ends its ability to contribute future operating exposure. A logged warning might do neither.

## A common trap: averaging rates

Device A has 1 fault in 10 hours. Device B has 9 faults in 900 hours.

Their individual observed rates are 0.1 and 0.01 faults per hour. Their unweighted average is 0.055.

The pooled rate is instead

$$
\widehat\lambda_{\mathrm{pooled}}=\frac{1+9}{10+900}
=\frac{10}{910}\approx0.01099.
$$

These describe different summaries. The first gives each device equal weight. The second gives each observed operating hour equal weight and is the maximum-likelihood estimate under an independent common-rate Poisson model with fixed exposures.

Neither summary, by itself, establishes a causal difference or identifies a device's underlying rate.

## What could break a simple model?

- One physical incident emits many duplicate log entries.
- Offline devices cannot report faults.
- Faults cause downtime, changing later exposure.
- The rate changes with temperature, software version, or age.
- Devices enter observation only after surviving an earlier period.

Defining exposure handles opportunity; it does not automatically solve dependence, missing observation, or selection.

## Check your understanding

A device produces 6 faults over 300 operating hours. What is its observed rate, and what does that estimate not tell you?

**Answer:** $6/300=0.02$ faults per operating hour. This does not establish that its rate is constant, quantify estimation uncertainty, or specify the probability of a terminal failure.
