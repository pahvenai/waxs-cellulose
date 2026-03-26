import numpy as np

class WAXSintensities:
    """
    Container for handling 1D WAXS scattering intensities.
    Only intensity as a function of scattering vector length q is tolerated.
    All operations on intensity must leave out masked values.
    """
    q: np.ndarray
    I: np.ndarray
    mask: np.ndarray
    metadata: dict