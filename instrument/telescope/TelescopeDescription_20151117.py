from ctapipe.instrument import util_functions, instrument_lists as ld
import hessio as h

def initialize_hessio(filename,file_closed):
    if file_closed:
        file_closed = util_functions.load_hessio(filename)
        print(file_closed)
        util_functions.nextevent_hessio()
    else:
        pass
    
    #ld.telescope_id = h.get_telescope_ids().tolist() #--> this function only can be used if the according python wrapper hase been added to pyhessio.c and hessio.py
    
    ld.telescope_id = h.get_teldata_list().tolist()
    ld.telescope_num = h.get_num_telescope()

    return file_closed

def initialize_fits(filename,file_closed):
    if file_closed:
        hdulist = util_functions.load_fits(filename)
        file_closed = hdulist
    else:
        pass
    teles = hdulist[1].data
    ld.telescope_id = teles["TelID"].tolist()
    ld.telescope_posX = teles["TelX"].tolist()
    ld.telescope_posY = teles["TelY"].tolist()
    ld.telescope_posZ = teles["TelZ"].tolist()
    ld.telescope_num = len(ld.telescope_id)

    return file_closed
