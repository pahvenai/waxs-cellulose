class WAXSazimIntensities:
    """
    Container for handling 1D WAXS scattering intensities, specifically integrated over q-range
    from a specific q-range given by qRange
    Only intensity as a function of azimuthal angle is tolerated.
    All operations on intensity must leave out masked values.
    """
    azim: np.ndarray
    qRange: np.ndarray
    intensity: np.ndarray
    mask: np.ndarray
    metadata: dict