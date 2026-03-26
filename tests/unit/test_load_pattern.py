# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 13:59:59 2026
"""

import numpy as np
from waxs_cellulose.io.loaders import load_pattern

# Test data is in tests/data
from pathlib import Path
DATA_DIR = Path(__file__).parents[1] / "data"

def test_load_pattern():
    arr = load_pattern(DATA_DIR / "guadua_bamboo_split_5_linescan_30s_0122.csv")
    meanValue = np.nanmean(arr.I)
    assert np.isclose(meanValue,  14.558, atol=0.01)