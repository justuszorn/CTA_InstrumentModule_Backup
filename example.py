import InstrumentDescription as ID

tel = ID.Telescope()
cam = ID.Camera()
opt = ID.Optics()

#example of hessio file:
filename = '/lustre/fs19/group/cta/users/zornju/anaconda3/ctapipe/ctapipe-extra/datasets/gamma_test.simtel.gz'

#load only the stored optics info of a specific telescope with ID = 2 out of the file
ID.initialize_optics(2,filename)
print('------------------------------------')
print(opt.getMirrorArea())
print(opt.getMirrorNumber())
print('------------------------------------')

#load only the stored camera info of a specific telescope with ID = 2 out of the file
ID.initialize_camera(2,filename)
print('------------------------------------')
print(cam.getPixelX())
print(cam.getCameraClass())
print('------------------------------------')

#load all the information connected to the telescopes out of the file,
#i.e. all the info which is stored in the file about all the telescopes
ID.initialize_telescope(filename)
print('------------------------------------')
print(tel.getTelescopePosX())
print(tel.getTelescopeNumber())
print(tel.getTelescopeID())
print(opt.getMirrorArea())
print(opt.getMirrorNumber())
print(cam.getPixelX())
print(cam.getCameraClass())
print('------------------------------------')
print('------------------------------------')




#example of fits file:
filename = "/afs/ifh.de/user/z/zornju/luster/PROD2_telconfig.fits"

#load only the stored optics info of a specific telescope with ID = 2 out of the file
ID.initialize_optics(2,filename)
print('------------------------------------')
print(opt.getMirrorArea())
print('------------------------------------')

#load only the stored camera info of a specific telescope with ID = 2 out of the file
ID.initialize_camera(2,filename)
print('------------------------------------')
print(cam.getPixelID())
print(cam.getCameraFOV())
print('------------------------------------')

#load all the information connected to the telescopes out of the file,
#i.e. all the info which is stored in the file about all the telescopes
ID.initialize_telescope(filename)
print('------------------------------------')
print(tel.getTelescopePosX())
print(tel.getTelescopeNumber())
print(tel.getTelescopeID())
print(opt.getMirrorArea())
print(cam.getCameraFOV())
