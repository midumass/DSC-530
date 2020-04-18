"""
# DSC-530-T302 Assignment 2.2
# Exercise 2.4
# Zach Hill
# 13JUN2019
"""

from __future__ import print_function

import sys

import first
import thinkstats2


def Mode(hist):
    """Returns the value with the highest frequency.

    hist: Hist object

    returns: value from Hist
    """
    mode = max(hist, key=lambda key: hist[key])  
    return mode

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    live, firsts, others = first.MakeFrames()
    hist = thinkstats2.Hist(live.prglngth)

    # test Mode    
    mode = Mode(hist)
    print('Mode of preg length', mode)
    assert mode == 39, mode

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
