"""
# DSC-530-T302 Assignment 8.2
# Zach Hill
# 27JUL2019
"""

'''
Exercise 13.1 In NSFG Cycles 6 and 7, the variable cmdivorcx contains
the date of divorce for the respondent's 
rst marriage, if applicable, encoded
in century-months.

Compute the duration of marriages that have ended in divorce, and the
duration, so far, of marriages that are ongoing. Estimate the hazard and
survival curve for the duration of marriage.

Use resampling to take into account sampling weights, and plot data from
several resamples to visualize sampling error.

Consider dividing the respondents into groups by decade of birth, and pos-
sibly by age at 
rst marriage.
'''

import numpy as np
import pandas as pd

import nsfg
import thinkstats2
import thinkplot

