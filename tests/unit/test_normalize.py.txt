import numpy as np
from waxs_cellulose.preprocessing.normalize import normalize_intensity


def test_normalize():
    arr = np.array([0, 1, 2])
    norm = normalize_intensity(arr)
    assert np.isclose(norm.max(), 1.0)