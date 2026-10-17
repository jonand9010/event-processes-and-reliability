# Event Processes and Reliability

*A practical guide to counts, rates, lifetimes, and failures.*

How do events occur over time, how do their rates vary, and what can we infer about the systems producing them?

This is a growing collection of short, connected chapters. The aim is mathematical clarity with practical interpretation: enough derivation to understand why a model works, without the scope of a full textbook.

Faults provide the running example. The same mathematics can describe other repeatable events, provided the assumptions fit.

## Start here

Read the chapters in order:

1. [Events, exposure, and the questions we ask](chapters/01-events-and-exposure.md)
2. [The Poisson process: counts and waiting times](chapters/02-poisson-process.md)
3. [Gamma-distributed rates and negative binomial counts](chapters/03-gamma-poisson-mixture.md)
4. [Survival, hazard, and what observation hides](chapters/04-survival-and-hazard.md)

Then work through [one fleet, three different questions](examples/01-fleet-example.md).

Use the [notation guide](meta/notation.md) when a symbol is unfamiliar. See the [roadmap](meta/roadmap.md) for planned topics and the [chapter template](meta/chapter-template.md) when adding material.

## The central connection

Let $N(t)$ count events up to time $t$, and let $T_1$ be the time of the first event. Then

$$
P(T_1>t)=P(N(t)=0).
$$

This identity requires no Poisson assumption: no event yet means the first event is still ahead. Specific process assumptions turn it into specific count and lifetime distributions.

For a homogeneous Poisson process, counts are Poisson and interarrival times are exponential. With gamma-distributed device rates, marginal counts are negative binomial and first-event survival is Lomax. These connections anchor the first chapters.

## Style and scope

- State the observational unit and the question before choosing a distribution.
- Define symbols and units when they first appear.
- Separate a generative model, an inference procedure, and a decision rule.
- State assumptions and explain what would break them.
- Use small numerical examples and short exercises with answers.
- Treat fault events, first failures, and terminal failures as different data structures.

The initial chapters are drafts with worked mathematics. Planned chapters are listed separately; they are not implied to be complete.

## Reading the Markdown

Open `README.md` on GitHub and follow the relative links. Equations use GitHub-supported `$...$` and `$$...$$` math syntax. No build step or Python installation is required. Other Markdown viewers may need math support enabled.

## Next contribution

The next planned chapter is **Estimating rates and expressing uncertainty**, covering exposure-based likelihoods, interval estimates, and gamma–Poisson updating. See the roadmap for the sequence after that.
