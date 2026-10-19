"""Demonstrate gamma heterogeneity, Lomax survival, and survivor selection.

Requires numpy and matplotlib. Run:
    python examples/02-gamma-lomax-simulation.py
"""
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(2026)
alpha = 2.0
beta = 100.0  # hours; gamma rate parameter, Lomax scale
n_devices = 100_000

# Draw a single, time-invariant event rate for each device.
rates = rng.gamma(shape=alpha, scale=1 / beta, size=n_devices)
first_events = rng.exponential(scale=1 / rates)

times = np.linspace(0, 300, 121)
empirical_survival = np.array([(first_events > t).mean() for t in times])
theoretical_survival = (beta / (beta + times)) ** alpha

# Among devices that have not yet experienced an event, calculate
# the average *fixed* latent rate; this is the population hazard.
survivor_mean_rates = np.array(
    [rates[first_events > t].mean() for t in times]
)
theoretical_hazard = alpha / (beta + times)

fig, ax = plt.subplots()
ax.plot(times, empirical_survival, label="Simulated event-free fraction")
ax.plot(times, theoretical_survival, "--", label="Lomax survival")
ax.set(xlabel="Time (hours)", ylabel="Probability of no first event")
ax.legend()
fig.tight_layout()

fig, ax = plt.subplots()
ax.plot(times, survivor_mean_rates, label="Mean fixed rate among survivors")
ax.plot(times, theoretical_hazard, "--", label="Lomax population hazard")
ax.set(xlabel="Time (hours)", ylabel="Events per hour")
ax.legend()
fig.tight_layout()
plt.show()
