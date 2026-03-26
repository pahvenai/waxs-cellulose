import numpy as np

class WAXSpattern:
    """
    Experimental 2D scattering pattern
    Subject to preprocessing before turning into analyzable data as a WAXScakeplot
    """
    I: np.ndarray
    mask: np.ndarray
    metadata: dict
    protected: bool
    
    def __init__(self, intensities, protected = False):
        self.I = intensities
        self.mask = np.ones(self.I.shape)
        self.protected = protected