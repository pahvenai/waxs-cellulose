import numpy as np


def normalize_intensity(intensity: np.ndarray) -> np.ndarray:
    """
    Normalize intensity to maximum value of 1.

    Parameters
    ----------
    intensity : np.ndarray
        Raw scattering intensity.

    Returns
    -------
    np.ndarray
        Normalized intensity.
    """
    return intensity / np.nanmax(intensity)