import InstrumentDescription as ID
import list_definition as ld

#example of hessio file:
format = "hessio"
filename = '/lustre/fs19/group/cta/users/zornju/anaconda3/ctapipe/ctapipe-extra/datasets/gamma_test.simtel.gz'
ID.initialize(filename,format)

#get some telescope characteristics stored in the file:

tel = ID.Telescope()
print(tel.getTelescopeID())
print(tel.getPixelX())
print(tel.getMirrorArea())

#example of fits file:
format = "fits"
filename = "/afs/ifh.de/user/z/zornju/luster/PROD2_telconfig.fits"
ID.initialize(filename,format)

#get some telescope characteristics stored in the file:

tel = ID.Telescope()
print(tel.getTelescopeID())
print(tel.getTelescopePosX())
print(tel.getMirrorArea())
