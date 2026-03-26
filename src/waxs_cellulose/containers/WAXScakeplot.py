import numpy as np
from waxs_cellulose.helpers.units import PhysicalUnit

class WAXScakeplot:
    """
    Preprocessed 2D scattering data presented as a function of 
    scattering vector length q and azimuthal angle (azim)
    Wherever possible, operations on intensities should not consider
    masked values.
    """
    q: np.ndarray
    qUnit: PhysicalUnit
    azim: np.ndarray
    I: np.ndarray
    mask: np.ndarray
    metadata: dict
    
    def __init__(self, intensities, azim, q, qUnit = "1/AA", protected = False):
        self.I = intensities
        shape = self.I.shape
        
        if len(azim) == 2:
            self.azim = np.linspace(azim[0], azim[1], shape[0])
        elif len(azim) == shape[0]:
            self.azim = azim
        else:
            raise ValueError("len(azim) was " + str(len(azim)) + 
                             ", allowed values 2 and " + str(shape[0]))   
            
        if len(q) == 2:
            self.q = np.linspace(q[0], q[1], shape[1])
        elif len(q) == shape[1]:
            self.q = q
        else:
            raise ValueError("len(q) was " + str(len(q)) + 
                             ", allowed values 2 and " + str(shape[1]))
         
        self.mask = np.ones(shape)
        self.qUnit = PhysicalUnit(qUnit)
        self.protected = protected