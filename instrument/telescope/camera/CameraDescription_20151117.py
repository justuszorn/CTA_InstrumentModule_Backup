from ctapipe.instrument import util_functions, instrument_lists as ld
import hessio as h
from astropy import units as u
import numpy as np
from ctapipe.io.camera import guess_camera_geometry

def initialize_hessio(filename,tel_id, file_closed):
    if file_closed:
        util_functions.load_hessio(filename)
        util_functions.nextevent_hessio()
    else:
        pass
    
    px = h.get_pixel_position(tel_id)[0]
    py = h.get_pixel_position(tel_id)[1]
    ld.pixel_posX.append(px)
    ld.pixel_posY.append(py)
    ld.camera_class.append(guess_camera_geometry(px*u.m,py*u.m).cam_id)
    
    #to use this, one has to go through every event of the run...
    n_channel = h.get_num_channel(tel_id)
    ld.channel_num = n_channel
    #for chan in range(n_channel):
    #    ld.adc_samples.append(h.get_adc_sample(tel_id,chan).tolist())
        
    if file_closed:
        util_functions.close_hessio()
        
def initialize_fits(filename,tel_id, file_closed):
    hdulist = file_closed
    if file_closed == 1:
        hdulist = util_functions.load_fits(filename)
        teles = hdulist[1].data
        ld.telescope = teles["TelID"].tolist()
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
        util_functions.close_fits(hdulist)
