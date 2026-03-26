# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 23:56:25 2026

"""

conversionFactors = {
    "1/AA": 1e-10,
    "1/nm": 1e-9,
    "1/um": 1e-6,
    "1/mm": 1e3,
    "1/cm": 1e2,
    "AA": 1e10,
    "nm": 1e9,
    "um": 1e-6,
    "mm": 1e-3,
    "cm": 1e-2}

prettyPrints = {
    "1/AA": r"$\AA^{-1}$",
    "1/nm": "nm^{-1}",
    "1/um": r"$\mu m^{-1}$",
    "1/mm": "mm^{-1}",
    "1/cm": "cm^{-1}",
    "AA": "nm",
    "nm": "nm",
    "um": "um",
    "mm": "mm",
    "cm": "cm"}

class PhysicalUnit:
    """
    Most numbers need to be associated with a unit.
    The class allows the units to be visualized, converted
    to SI units and included with the data.
    """
    shorthand: str
    conversionFactor: float 
    prettyPrint: str
    
    def __init__(self, shorthand, conversionFactor = None, prettyPrint = None):
        if (not conversionFactor) and (shorthand in conversionFactors):
            conversionFactor = conversionFactors[shorthand] 
        if (not prettyPrint) and (shorthand in prettyPrints):
            prettyPrint = prettyPrints[shorthand]
        self.shorthand = shorthand
        self.conversionFactor = conversionFactor
        self.prettyPrint = prettyPrint
        
    def __repr__(self):
        return "PhysicalUnit(): " + self.shorthand
    
    def __str__(self):
        return self.prettyPrint
    
    def toSI(self):
        return self.conversionFactor
    