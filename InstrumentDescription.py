import numpy as np
import os
import sys
from astropy.io import fits
from astropy import units as u
import hessio as h
from ctapipe.io.hessio import hessio_event_source
from ctapipe.io.files import get_file_type
from ctapipe import io
import instrument_lists as ld
import warnings


def load_hessio(filename):
    """Function to open and load hessio files"""
    event = h.file_open(filename)
    print("Hessio file %s has been opened" % filename)
    return event
    
def nextevent_hessio():
    next(h.move_to_next_event())

def load_fits(filename):
    hdulist = fits.open(filename)
    print("Fits file %s has been opened" % filename)
    return hdulist

def load_ascii(filename):
    """Function to open and load an ASCII file"""
    print("ASCI file %s has been opened" % filename)

def close_hessio():
    h.close_file()
    print("Hessio file has been closed.")

def close_fits(hdulist):
    print("Fits file has been closed.")
    hdulist.close()

def close_ascii():
    print("ASCII file has been closed")



def initialize_camera(tel_id, filename, file_closed = 1):
    if 'simtel.gz' in filename:
        if file_closed:
            ld.clear_lists_camera()
            load_hessio(filename)
            nextevent_hessio()
        else:
            pass
    
        px = h.get_pixel_position(tel_id)[0]
        py = h.get_pixel_position(tel_id)[1]
        ld.pixel_posX.append(px)
        ld.pixel_posY.append(py)
        ld.camera_class.append(io.guess_camera_geometry(px*u.m,py*u.m).cam_id)

        if file_closed:
            close_hessio()
        
    elif 'fits' in filename:
        hdulist = file_closed
        if file_closed == 1:
            ld.clear_lists_camera()
            ld.clear_lists_telescope()
            hdulist = load_fits(filename)
            for i in range(0,len(hdulist[1].data)):
                ld.telescope_id.append(hdulist[1].data[i]["TelID"])
        else:
            pass
        
        index = ld.telescope_id.index(tel_id)
        ld.camera_fov.append(hdulist[1].data[index]["FOV"])
        
        pixel_id_cam = []
        index2 = np.where(hdulist[2].data['L0ID'] == index)[0]
        for i in index2:
            pixel_id_cam.append(hdulist[2].data[i]['PixelID'])
        ld.pixel_id.append(pixel_id_cam)
        
        if file_closed == 1:
            close_fits(hdulist)
    
        
def initialize_optics(tel_id, filename, file_closed = 1):
    if 'simtel.gz' in filename:
        if file_closed:
            ld.clear_lists_optics()
            load_hessio(filename)
            nextevent_hessio()
        else:
            pass
    
        ld.mirror_area.append(h.get_mirror_area(tel_id))
        ld.mirror_number.append(h.get_mirror_number(tel_id))

        if file_closed:
            close_hessio()        

    elif 'fits' in filename:
        hdulist = file_closed
        if file_closed == 1:
            ld.clear_lists_optics()
            ld.clear_lists_telescope()
            hdulist = load_fits(filename)
            for i in range(0,len(hdulist[1].data)):
                ld.telescope_id.append(hdulist[1].data[i]["TelID"])
        else:
            pass
        index = ld.telescope_id.index(tel_id)
        ld.mirror_area.append(hdulist[1].data[index]["MirrorArea"])

        if file_closed == 1:
            close_fits(hdulist)

def initialize_telescope(filename, file_closed = True):
    ld.clear_lists_telescope()
    ld.clear_lists_camera()

    if 'simtel.gz' in filename:
        if file_closed:
            file_closed = load_hessio(filename)
            nextevent_hessio()
        else:
            pass

        ld.telescope_id = h.get_telescope_ids().tolist()
        #ld.telescope_id.append(h.get_teldata_list())
        ld.telescope_num = h.get_num_telescope()

    elif 'fits' in filename:
        if file_closed:
            hdulist = load_fits(filename)
            file_closed = hdulist
        else:
            pass
        
        for i in range(0,len(hdulist[1].data)):
            ld.telescope_id.append(hdulist[1].data[i]["TelID"])
            ld.telescope_posX.append(hdulist[1].data[i]["TelX"])
            ld.telescope_posY.append(hdulist[1].data[i]["TelY"])
            ld.telescope_posZ.append(hdulist[1].data[i]["TelZ"])
        

    for tel in ld.telescope_id:
        initialize_camera(tel,filename,file_closed)
        initialize_optics(tel,filename,file_closed)

    if 'simtel.gz' in filename:   
        close_hessio()
    elif 'fits' in filename:
        close_fits(hdulist)

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
    the optics of a specific telescope."""

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

    
