from .io.loaders import load_txt
from .preprocessing.normalize import normalize_intensity
from .analysis.peaks import fit_gaussian


def run_pipeline(filepath: str):
    data = load_txt(filepath)
    x, y = data[:, 0], data[:, 1]

    y_norm = normalize_intensity(y)
    fit = fit_gaussian(x, y_norm)

    return fit

"""
Change to:

pipeline = Pipeline([
    Normalize(),
    BackgroundSubtract(),
    PeakFit()
])
"""