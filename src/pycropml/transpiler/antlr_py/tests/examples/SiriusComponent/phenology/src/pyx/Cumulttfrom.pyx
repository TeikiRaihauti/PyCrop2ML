import numpy 
from math import *
def model_cumulttfrom(stringlist calendarMoments_t1,
                      floatlist calendarCumuls_t1,
                      float cumulTT):
    """

    CumulTTFrom model
    Author: Pierre Martre
    Reference: ('',)
    Institution: INRA Montpellier
    ExtendedDescription: 
    ShortDescription: 

    """
    cdef float cumulTTFromZC_65
    cdef float cumulTTFromZC_39
    cdef float cumulTTFromZC_91
    cumulTTFromZC_65 = 0.0
    cumulTTFromZC_39 = 0.0
    cumulTTFromZC_91 = 0.0
    if "Anthesis" in calendarMoments_t1:
        cumulTTFromZC_65 = cumulTT - calendarCumuls_t1[calendarMoments_t1.index("Anthesis")]
    if "FlagLeafLiguleJustVisible" in calendarMoments_t1:
        cumulTTFromZC_39 = cumulTT - calendarCumuls_t1[calendarMoments_t1.index("FlagLeafLiguleJustVisible")]
    if "EndGrainFilling" in calendarMoments_t1:
        cumulTTFromZC_91 = cumulTT - calendarCumuls_t1[calendarMoments_t1.index("EndGrainFilling")]
    return  cumulTTFromZC_65, cumulTTFromZC_39, cumulTTFromZC_91
