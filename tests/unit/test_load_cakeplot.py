# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 20:57:03 2026

"""

import numpy as np
from waxs_cellulose.io.loaders import load_cakeplot

# Test data is in tests/data
from pathlib import Path
DATA_DIR = Path(__file__).parents[1] / "data"

def test_load_cakeplot0():
    arr = load_cakeplot(DATA_DIR / "guadua_bamboo_split_5_linescan_30s_0122.csv",
                        q = [0.5, 3.0], azim = [0, 90])
    meanValue = np.nanmean(arr.I)
    assert np.isclose(meanValue,  14.558, atol=0.01)
    
def test_load_cakeplot1():
    arr = load_cakeplot(DATA_DIR / "guadua_bamboo_split_5_linescan_30s_0122.csv",
                        q = [0.5, 3.0], azim = [0, 90])
    assert (len(arr.azim) == arr.I.shape[0])
    assert (len(arr.q) == arr.I.shape[1])
    assert (len(arr.q) == 800)
    assert (len(arr.azim) == 180)