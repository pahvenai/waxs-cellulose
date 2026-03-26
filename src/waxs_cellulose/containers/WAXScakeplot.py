import numpy as np

class WAXScakeplot:
    """
    Preprocessed 2D scattering data presented as a function of 
    scattering vector length q and azimuthal angle (azim)
    Wherever possible, operations on intensities should not consider
    masked values
    """
    q: np.ndarray
    azim: np.ndarray
    I: np.ndarray
    mask: np.ndarray
    metadata: dict