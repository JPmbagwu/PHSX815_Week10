#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 21:47:23 2023

@author: johnpaulmbagwu
"""

import numpy as np
import matplotlib.pyplot as plt

# Define a probability distribution that is not a Gaussian
def my_dist(x):
    return 1 / (1 + np.exp(-(x-5)))

# Set the number of experiments and the sample size
M = 20000
N = 70

# Perform M experiments, each with N samples
sample_means = []
for i in range(M):
    samples = my_dist(np.random.uniform(0, 10, N))
    sample_mean = np.mean(samples)
    sample_means.append(sample_mean)

# Plot the distribution of sample means
plt.hist(sample_means, bins=50, density=True)
plt.title(f"Distribution of {M} sample means from {N} samples each")
plt.xlabel("Sample mean")
plt.ylabel("Frequency")
plt.show()
