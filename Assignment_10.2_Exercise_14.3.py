"""
# DSC-530-T302 Assignment 10.2
# Exercise 14-3
# Zach Hill
# 10AUG2019
"""
import numpy as np
import random

import normal
import thinkstats2
import thinkplot

# =============================================================================
# Exercise 14.3 In a recent paper, Stein et al. investigate the effects of an
# intervention intended to mitigate gender-stereotypical task allocation within
# student engineering teams.
# Before and after the intervention, students responded to a survey that asked
# them to rate their contribution to each aspect of class projects on a 7-point
# scale.
# Before the intervention, male students reported higher scores for the pro-
# gramming aspect of the project than female students; on average men re-
# ported a score of 3.57 with standard error 0.28. Women reported 1.91, on
# average, with standard error 0.32.
# Compute the sampling distribution of the gender gap (the difference in
# means), and test whether it is statistically signifcant. Because you are given
# standard errors for the estimated means, you don't need to know the sample
# size to figure out the sampling distributions.
# After the intervention, the gender gap was smaller: the average score for men
# was 3.44 (SE 0.16); the average score for women was 3.18 (SE 0.16). Again,
# compute the sampling distribution of the gender gap and test it.
# Finally, estimate the change in gender gap; what is
# =============================================================================

male_score_before = 3.57
male_stderr_before = .28
male_score_after = 3.44
male_stderr_after = .16

female_score_before = 1.91
female_stderr_before = .32
female_score_after = 3.18
female_stderr_after = .16

# normal.Normal requires the mean and the variance, which is the stderr sqrd
male_before = normal.Normal(3.57, 0.28**2)
male_after = normal.Normal(3.44, 0.16**2)

female_before = normal.Normal(1.91, 0.32**2)
female_after = normal.Normal(3.18, 0.16**2)

diff_before = female_before - male_before
print('Mean =', diff_before.mu, 'P-value =', 1-diff_before.Prob(0))
print('CI', diff_before.Percentile(5), diff_before.Percentile(95))
print('Standard Error =', diff_before.sigma)

diff_after = female_after - male_after
print('Mean =', diff_after.mu, 'P-value =', 1-diff_after.Prob(0))
print('CI =', diff_after.Percentile(5), diff_after.Percentile(95))
print('Standard Error =', diff_after.sigma)

diff = diff_after - diff_before
print('Mean =', diff.mu, 'P-value =', diff.Prob(0))
print('CI =', diff.Percentile(5), diff.Percentile(95))
print('Standard Error =', diff.sigma)