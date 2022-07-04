import numpy as np
import matplotlib.pyplot as plt

mu = 0.0
sigma = 1.0

samples = np.random.default_rng().normal(mu, sigma, 1000)
mean = abs(mu - np.mean(samples))
variance = abs(sigma - np.std(samples, ddof=1))

print(f"Mu: {mu}\nSigma: {sigma}\nMean: {mean}\nVariance: {variance}")

count, bins, ignored = plt.hist(samples, 50, density=True)
plt.plot(
    bins,
    1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-((bins - mu) ** 2) / (2 * sigma**2)),
    linewidth=2,
    color="r",
)
plt.show()
