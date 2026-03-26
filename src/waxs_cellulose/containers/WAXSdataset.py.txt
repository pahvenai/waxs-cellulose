class WAXSdataset:
     """
     A collection of data from one experiment.
     May contain raw data, 1D scattering intensities or 2D scattering intensities.
     """
     WAXScakeplots: list
     WAXSpatterns: list
     WAXSintensities: list
     WAXSazimIntensities: list
     metadata: dict