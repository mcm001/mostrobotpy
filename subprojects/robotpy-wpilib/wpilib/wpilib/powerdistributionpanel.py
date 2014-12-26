#----------------------------------------------------------------------------
# Copyright (c) FIRST 2014. All Rights Reserved.
# Open Source Software - may be modified and shared by FRC teams. The code
# must be accompanied by the FIRST BSD license file in the root directory of
# the project.
#----------------------------------------------------------------------------

import hal

from .sensorbase import SensorBase

__all__ = ["PowerDistributionPanel"]

class PowerDistributionPanel(SensorBase):
    """Use to obtain voltage, current, and temperature from the CAN PDP"""

    def getVoltage(self):
        """
            :returns: The voltage of the PDP
            :rtype: float
        """
        return hal.getPDPVoltage()

    def getTemperature(self):
        """
            :returns: The temperature of the PDP in degrees Celsius
            :rtype: float
        """
        return hal.getPDPTemperature()

    def getCurrent(self, channel):
        """
            :returns: The current of one of the PDP channels (channels 0-15)
                      in Amperes
            :rtype: float
        """
        SensorBase.checkPDPChannel(channel)
        return hal.getPDPChannelCurrent(channel)
    
    def getTotalCurrent(self):
        """
            :returns: The total current drawn from the PDP channels in Amperes
            :rtype: float
        """
        return hal.getPDPTotalCurrent()
    
    def getTotalPower(self):
        """
            :returns: The total power drawn from the PDP channels in Joules
            :rtype: float
        """
        return hal.getPDPTotalPower()
    
    def getTotalEnergy(self):
        """
            :returns: The total energy drawn from the PDP channels in Watts
            :rtype: float
        """
        return hal.getPDPTotalEnergy()
    
    def resetTotalEnergy(self):
        """
            Reset the total energy drawn from the PDP
        """
        hal.resetPDPTotalEnergy()
    
    def clearStickyFaults(self):
        """
            Remove all of the fault flags on the PDP
        """
        hal.clearPDPStickyFaults()
    
    
