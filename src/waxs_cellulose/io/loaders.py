import numpy as np
import os
import pandas as pd
from waxs_cellulose.containers.WAXSpattern import WAXSpattern
from waxs_cellulose.containers.WAXScakeplot import WAXScakeplot

def load_intensities(filepath: str) -> np.ndarray:
    """Load simple two-column WAXS data (q, intensity)."""
    return np.loadtxt(filepath)

def load_pattern(filepath: str, fileformat: str = "None", protected: bool = False):
    """
    Tries to open a 2D scattering pattern

    Parameters
    ----------
    filepath : str
        Path where the 2D scattering pattern is.
    fileformat : str
        Format of the 2D scattering pattern file.
        Supported formats: csv, image formats
    protected : bool
        Can be used to keep data unaltered

    Returns
    -------
    WAXSpattern if reading is succesful or None if unsuccesful.

    """
    
    # If file format is not given try to guess it from file extension
    if fileformat == "None":
        filename, fileformat = os.path.splitext(filepath)
    
    if fileformat in ["csv", ".csv"]:
        pattern = pd.read_csv(filepath, header=None).to_numpy()        
        return WAXSpattern(intensities=pattern, protected=protected)
    
    return None
    
def load_cakeplot(filepath: str, azim: np.ndarray, q: np.ndarray, 
                  fileformat: str = "None", protected: bool = False):
    """
    Tries to open a 2D cake plot

    Parameters
    ----------
    filepath : str
        Path where the cakeplot (intensity as a funcion of q and azim) is.
    azim : np.ndarray
        Gives the azim-values for the cakeplot
        length of array must be 2 or must match first dimension of cakeplot
    q : np.ndarray
        Gives the q-values for the cakeplot
        length of array must be 2 or must match second dimension of cakeplot
    fileformat : str
        Format of the 2D scattering pattern file.
        Supported formats: csv, image formats
    protected : bool
        Can be used to keep data unaltered

    Returns
    -------
    WAXScakeplot if reading is succesful or None if unsuccesful.

    """
    
    # If file format is not given try to guess it from file extension
    if fileformat == "None":
        filename, fileformat = os.path.splitext(filepath)
    
    if fileformat in ["csv", ".csv"]:
        pattern = pd.read_csv(filepath, header=None).to_numpy()        
        return WAXScakeplot(intensities=pattern, q=q, azim=azim, 
                           protected=protected)
    
    return None