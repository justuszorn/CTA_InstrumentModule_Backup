import InstrumentDescription as ID

#example of hessio file:
format = "hessio"
filename = '/lustre/fs19/group/cta/users/zornju/anaconda3/ctapipe/ctapipe-extra/datasets/gamma_test.simtel.gz'
ID.initialize(filename,format)

#get some telescope characteristics stored in the file:

tel1 = ID.Telescope()
print(tel1.getTelescopeID())
print(tel1.camera.getPixelX())
print(tel1.optics.getMirrorArea())
print(tel1.getTelescopePosX())

#example of fits file:
format = "fits"
filename = "/afs/ifh.de/user/z/zornju/luster/PROD2_telconfig.fits"
ID.initialize(filename,format)

#get some telescope characteristics stored in the file:

tel2 = ID.Telescope()
print(tel2.getTelescopeID())
print(tel2.getTelescopePosX())
print(tel2.optics.getMirrorArea())


