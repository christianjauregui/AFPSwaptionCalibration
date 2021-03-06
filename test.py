#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 12:54:51 2019

@author: paragonhao
"""
from blackModel76 import BlackModel76
import unittest

class UniteTestMethods(unittest.TestCase):
     
   
    
    def test_blackModelPrice(self):
        blackModel76 = BlackModel76(tenor = 4, fRate = 0.07, xRate= 0.075, rfRate=0.06, T = 2, sigma=0.02, m = 2)
        print(blackModel76.getPayerSwaptionPrice())
       
if __name__ == '__main__':
    unittest.main()
    
    
# example on how to construct the curve

from utils import Utils


file_Path_swaption_ts = 'data/swaption_termStructure.xlsx'
calibrationDate = '2019-07-05'
termStructure = Utils.getTermStructure(calibrationDate, file_Path_swaption_ts)
Utils.getForwardCurve(termStructure)
