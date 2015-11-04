import InstrumentDescription as ID
import list_definition as ld

#example of hessio file:
format = "hessio"
filename = '/lustre/fs19/group/cta/users/zornju/anaconda3/ctapipe/ctapipe-extra/datasets/gamma_test.simtel.gz'
ID.initialize(filename,format)

#get some telescope characteristics stored in the file:

tel = ID.Telescope()
tel.getTelescopeID()
tel.getPixelX()
tel.getMirrorArea()

ld.telescope_id = []
ld.telescope_posX = []
ld.mirror_area = []

#example of fits file:
format = "fits"
filename = "/afs/ifh.de/user/z/zornju/luster/PROD2_telconfig.fits"
ID.initialize(filename,format)

#get some telescope characteristics stored in the file:

tel = ID.Telescope()
tel.getTelescopeID()
tel.getTelescopePosX()
tel.getMirrorArea()
