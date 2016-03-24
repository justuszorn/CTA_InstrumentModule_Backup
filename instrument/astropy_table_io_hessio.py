# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:46:51 2016

@author: zornju
astropy.io.hessio
"""

import pyhessio as h
from astropy.table import Table,join
import astropy.units as u
import numpy as np

def from_hessio_to_astropytable(filename):

    h.file_open(filename)
    next(h.move_to_next_event())
    tel_id = h.get_telescope_ids()
    
    tel_table = Table()
    
    tel_table['TelID']= tel_id
    
    tel_posX = [h.get_telescope_position(i)[0] for i in tel_id]*u.m
    tel_posY = [h.get_telescope_position(i)[1] for i in tel_id]*u.m
    tel_posZ = [h.get_telescope_position(i)[2] for i in tel_id]*u.m
    tel_table['TelX'] = tel_posX
    tel_table['TelX'].unit = u.m
    tel_table['TelY'] = tel_posY
    tel_table['TelY'].unit = u.m
    tel_table['TelZ'] = tel_posZ
    tel_table['TelZ'].unit = u.m
    
    for t in range(len(tel_id)):
        table = Table()
        pix_posX = h.get_pixel_position(tel_id[t])[0]*u.m
        pix_posY = h.get_pixel_position(tel_id[t])[1]*u.m       
        pix_id = np.arange(len(pix_posX))
        pix_area = h.get_pixel_area(tel_id[t])*u.m**2
         
        table['TelID'] = [tel_id[t] for i in range(len(pix_posX))]
        table['PixelID'] = pix_id
        table['PixX'] = pix_posX
        table['PixX'].unit = u.m
        table['PixY'] = pix_posY
        table['PixY'].unit = u.m
        table['PixArea'] = pix_area.value
        table['PixArea'].unit = pix_area.unit
        
        if t == 0:
            cam_table = table
        else:
            cam_table = join(cam_table,table,join_type='outer')
    
    return [tel_table,cam_table]
            

