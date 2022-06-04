import pycuda.driver as drv
drv.init()
print ("%d device(s) found." % drv.Device.count())