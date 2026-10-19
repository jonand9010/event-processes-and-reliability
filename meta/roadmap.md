# Development roadmap

[Contents](../README.md)

## Written starter chapters

1. Events and exposure.
2. Homogeneous Poisson process and exponential waiting times.
3. Gamma rate heterogeneity and negative binomial counts.
4. Survival, hazard, population selection, and right censoring.
5. Gamma mixtures, Lomax first-event survival, and survivor selection.

## Next: inference from observations

6. **Estimating rates and expressing uncertainty.** Poisson likelihood, pooled exposure, frequentist intervals, gamma–Poisson updating, and posterior predictive counts. Distinguish confidence, credible, and prediction intervals.
7. **Checking the model.** Exposure-aware diagnostics, zero counts, overdispersion, temporal dependence, and competing explanations for negative binomial counts.
8. **Survival with incomplete observation.** Kaplan–Meier estimation, risk sets, independent censoring, delayed entry, and the difference between first-event data and recurrent-event histories.

## Then: explaining variation

9. **Regression for event counts.** Poisson and negative binomial regression, exposure offsets, rate ratios, and covariate interpretation.
10. **Regression for event times.** Proportional hazards, Cox regression, accelerated failure time models, and checking assumptions.
11. **Frailty and hierarchical models.** Shared device effects, population versus individual predictions, and partial pooling.

## Then: recurrence and system behaviour

12. **Renewal and repair.** Exponential versus non-exponential gaps, age since repair, and what “as good as new” means.
13. **Recurrent events and competing risks.** Event histories, dependence, terminal events, and cause-specific questions.
14. **Monitoring changes in fault rates.** Baselines, exposure-adjusted comparisons, practical effect sizes, and sequential decisions.
15. **From component events to system reliability.** System boundaries, reliability functions, dependencies, and limits of aggregation.

## Working method

Add one chapter at a time. Each should answer a concrete question and connect back to the preceding model. Keep optional technical derivations separate from the main explanation when they interrupt the flow.

Add simulation code when it resolves a specific conceptual question. The Markdown should remain readable without running it. Choose a licence before public reuse; none is assigned by this starter.
