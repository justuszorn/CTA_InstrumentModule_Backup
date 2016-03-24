import numpy as np
import os
import sys
from astropy.io import fits
from astropy import units as u
from astropy.table import Table
import hessio as h
from ctapipe.io.hessio import hessio_event_source
from ctapipe.io.files import get_file_type
from ctapipe import io
from ctapipe.instrument import instrument_lists as ld
from ctapipe.instrument.telescope import TelescopeDescription as TD
from ctapipe.instrument.telescope.camera import CameraDescription as CD
from ctapipe.instrument.telescope.optics import OpticsDescription as OD
from ctapipe.instrument import util_functions
import warnings
from ctapipe.visualization import ArrayDisplay
import matplotlib.pyplot as plt

#TO DO:
# - rise warnings or put values to -1 or sth. else if desired information is not stored in the file. Currently in such a case returned array is empty. Maybe it's ok like that??
# - rise warning if one trys to get a camera or optics information of a telescope of ID x which is not given in the file

def initialize_telescope(filename, file_closed = True):
    ld.clear_lists_telescope()
    ld.clear_lists_camera()
    ld.clear_lists_optics()

    if 'simtel.gz' in filename:
        file_closed = TD.initialize_hessio(filename,file_closed)
        for tel in ld.telescope_id:
            CD.initialize_hessio(filename,tel,file_closed)
            OD.initialize_hessio(filename,tel,file_closed)
        util_functions.close_hessio()

    elif 'fits' in filename:
        file_closed = TD.initialize_fits(filename,file_closed)
        for tel in ld.telescope_id:
            CD.initialize_fits(filename,tel,file_closed)
            OD.initialize_fits(filename,tel,file_closed)
        util_functions.close_fits(file_closed)


def initialize_camera(filename,tel_id,file_closed = True):
    if file_closed:
        ld.clear_lists_camera()
        ld.clear_lists_telescope()
    else:
        pass

    if 'simtel.gz' in filename:
        CD.initialize_hessio(filename,tel_id,file_closed)
    elif 'fits' in filename:
        CD.initialize_fits(filename,tel_id,file_closed)
    
       
def initialize_optics(filename, tel_id,file_closed = True):
    if file_closed:
        ld.clear_lists_optics()
        ld.clear_lists_telescope()
    else:
        pass

    if 'simtel.gz' in filename:
        OD.initialize_hessio(filename,tel_id,file_closed)
    elif 'fits' in filename:
        OD.initialize_fits(filename,tel_id,file_closed)


class Subarray:
    #What should be in here?

    def __init__(self):
        self.telescope = Telescope()
    
    def plotSubArray(self):
        ad = ArrayDisplay(ld.telescope_posX, ld.telescope_posY, ld.mirror_area)
        for i in range(len(ld.telescope_id)):
            name = "CT%i" % ld.telescope_id[i]
            plt.text(ld.telescope_posX[i],ld.telescope_posY[i],name,fontsize=8)
        ad.axes.set_xlim(-1000, 1000)
        ad.axes.set_ylim(-1000, 1000)
        plt.show()

    

class Telescope:
    """`Telescope` is a class that provides and gets all the information about
    a specific telescope such as the camera's characteristics"""

    def __init__(self):
        self.optics = Optics()
        self.camera = Camera()

    #Getter Functions:

    def getTelescopeNumber(self):
        return ld.telescope_num

    def getTelescopeID(self):
        return(ld.telescope_id)

    def getTelescopePosX(self):
        if len(ld.telescope_posX) == 0:
            warnings.warn("File contains no info about TelescopePosX.")
        return(ld.telescope_posX)

    def getTelescopePosY(self):
        return(ld.telescope_posY)

    def getTelescopePosZ(self):
        return(ld.telescope_posZ)


    #Write Functions:

    #Plot Functions:

    #def plot(self, list_1, list_2=0):
    #    if list_2==0:

class Optics:
    """`Optics` is a class that provides and gets all the information about
    the optics of a specific telescope."""

    def getMirrorArea(self):
        return(ld.mirror_area)

    def getMirrorNumber(self):
        return(ld.mirror_number)

    def getOptFocLen(self):
        return ld.focal_length

class Camera:
    """`Camera` is a class that provides and gets all the information about
    the camera of a specific telescope."""

    def getCameraClass(self):
        return(ld.camera_class)

    def getCameraFOV(self):
        return(ld.camera_fov)

    def getPixelID(self):
        return(ld.pixel_id)

    def getPixelX(self):
        return(ld.pixel_posX)

    def getPixelY(self):
        return(ld.pixel_posY)

    def getPixelZ(self):
        return(ld.pixel_posZ)

    #maybe not needed...
    def getNumberChannels(self):
        return ld.channel_num

    def getADCsamples(self):
        return ld.adc_samples
    #---------------------------


class Pixel:
     """`Pixel` is a class that provides and gets all the information about
    a specific pixel of a specific camera."""

     
    
