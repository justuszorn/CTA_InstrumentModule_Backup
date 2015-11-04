import numpy as np
import os
import sys
from astropy.io import fits
from astropy import units as u
import hessio as h
from ctapipe.io.hessio import hessio_event_source
from ctapipe.io.files import get_file_type
from ctapipe import io
import list_definition as ld


def load_hessio(filename):
    """Function to open and load hessio files"""
    event = h.file_open(filename)
    print("Hessio file %s has been opened" % filename)
    
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


def initialize(filename, format = 'hessio'):
    if format == 'hessio':
        load_hessio(filename)
        e=0
        while True:
            try:
                e+=1
                print("Event %i is read." % e)
                nextevent_hessio()
                ld.telescope_id.append(h.get_teldata_list())
            #ld.telescope_posX.append(?)
            #ld.telescope_posY.append(?)
            #ld.telescope_posZ.append(?)
            #ld.camera_fov.append(?)

                for i in range(0,len(ld.telescope_id[-1])):
                #ld.pixel_id.append(?)
                    px = h.get_pixel_position(ld.telescope_id[-1][i])[0]
                    ld.pixel_posX.append(px)
                    py = h.get_pixel_position(ld.telescope_id[-1][i])[1]
                    ld.pixel_posY.append(py)
                    ld.camera_class.append(io.guess_camera_geometry(px*u.m,py*u.m).cam_id)
                    ld.mirror_area.append(h.get_mirror_area(ld.telescope_id[-1][i]))
                    ld.mirror_number.append(h.get_mirror_number(ld.telescope_id[-1][i]))

            except:
                break
        
        print("In total %i events have been read." % e)
        ld.telescope_id = np.array([val for sublist in ld.telescope_id for val in sublist])
        ld.mirror_area = np.array(ld.mirror_area)

        close_hessio()

    elif format == 'fits':
        hdulist = load_fits(filename)
        j=0
        for i in range(0,len(hdulist[1].data)):
            ld.telescope_id.append(hdulist[1].data[i]["TelID"])
            ld.telescope_posX.append(hdulist[1].data[i]["TelX"])
            ld.telescope_posY.append(hdulist[1].data[i]["TelY"])
            ld.telescope_posZ.append(hdulist[1].data[i]["TelZ"])
            ld.camera_fov.append(hdulist[1].data[i]["FOV"])
            ld.mirror_area.append(hdulist[1].data[i]["MirrorArea"])
            
            pixel_id_cam = []
            while j<len(hdulist[2].data) and hdulist[2].data[j][1]==i:
                pixel_id_cam.append(hdulist[2].data[j]['PixelID'])
                j+=1
            ld.pixel_id.append(np.array(pixel_id_cam))

        close_fits(hdulist)

class Telescope:
    """`Telescope` is a class that provides and gets all the information about
    a specific telescope such as the camera's characteristics"""

    #Getter Functions:

    def getTelescopeID(self):
        print(ld.telescope_id)

    def getTelescopePosX(self):
        print(ld.telescope_posX)

    def getTelescopePosY(self):
        print(ld.telescope_posY)

    def getTelescopePosZ(self):
        print(ld.telescope_posZ)

    def getMirrorArea(self):
        print(ld.mirror_area)

    def getPixelX(self):
        print(ld.pixel_posX)

    #Plot Functions:

    #def plot(self, list_1, list_2=0):
    #    if list_2==0:
