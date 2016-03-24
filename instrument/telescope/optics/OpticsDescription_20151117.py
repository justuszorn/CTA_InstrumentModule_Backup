from ctapipe.instrument import util_functions, instrument_lists as ld
import hessio as h

def initialize_hessio(filename,tel_id, file_closed):
    if file_closed:
        util_functions.load_hessio(filename)
        util_functions.nextevent_hessio()
    else:
        pass
    
    ld.mirror_area.append(h.get_mirror_area(tel_id))
    ld.mirror_number.append(h.get_mirror_number(tel_id))

    if file_closed:
        util_functions.close_hessio()
        
def initialize_fits(filename,tel_id, file_closed):  
    hdulist = file_closed
    if file_closed == 1:
        hdulist = load_fits(filename)
        teles = hdulist[1].data
        ld.telescope = teles["TelID"].tolist()  
    else:
        pass
    index = ld.telescope_id.index(tel_id)
    ld.mirror_area.append(hdulist[1].data[index]["MirrorArea"])
    
    if file_closed == 1:
        util_functions.close_fits(hdulist)
