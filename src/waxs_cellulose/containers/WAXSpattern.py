class WAXSpattern:
    """
    Experimental 2D scattering pattern
    Subject to preprocessing before turning into analyzable data as a WAXScakeplot
    """
    intensities: np.ndarray
    mask: np.ndarray
    metadata: dict