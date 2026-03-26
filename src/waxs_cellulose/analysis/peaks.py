import numpy as np
from lmfit.models import GaussianModel


def fit_gaussian(x: np.ndarray, y: np.ndarray):
    model = GaussianModel()
    params = model.guess(y, x=x)
    result = model.fit(y, params, x=x)
    return result