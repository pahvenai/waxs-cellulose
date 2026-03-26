import numpy as np


def load_txt(filepath: str) -> np.ndarray:
    """Load simple two-column WAXS data (q, intensity)."""
    return np.loadtxt(filepath)