"""
# DSC-530-T302 Assignment 2.2
# Exercise 1.2
# Zach Hill
# 13JUN2019
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2


'''Write a function that reads the respondent file, 2002FemResp.dat.gz.'''
def ReadRespFile():
    dict_file = './2002FemResp.dct'
    data_file = './2002FemResp.dat.gz'
    
    dict_input = thinkstats2.ReadStataDct(dict_file)
    df = dict_input.ReadFixedWidth(data_file, compression='gzip', nrows=None)
        
    return df

'''Print the value counts for the pregnum variable and compare them to the published results in the NSFG codebook.'''
def CountValues(df):
    print(df['pregnum'].value_counts().sort_index())
    
'''Cross-validate the respondent and pregnancy files by comparing pregnum for each respondent with the number of records in the pregnancy file.'''
def CompareValues(df):
    preg = nsfg.ReadFemPreg()
    map_preg = nsfg.MakePregMap(preg)
    
    for index, pregnum in df['pregnum'].items():
        if len(map_preg[df.caseid[index]]) != pregnum:
            return False
    return True

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    resp = ReadRespFile()
    resp.head()
    
    CountValues(resp)
        
    assert(len(resp)==7643)
    assert((resp['pregnum'].value_counts()[1])==1267)
    assert(CompareValues(resp))
    
    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
