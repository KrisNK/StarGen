from collections import OrderedDict
import os
import numpy as np
from photutils.datasets import make_random_gaussians_table
from astropy.io import fits

n_sources = 50 #nb etoiles
param_ranges = [('amplitude', [500, 3500]), #flux en conventionel max~13,000adu en EM max ~4,000adu
                 ('x_mean', [0, 1024]), #detecteur fait 1024X1024 pixels
                 ('y_mean', [0,1024]), #detecteur fait 1024X1024 pixels
                 ('x_stddev', [3,3.1]), # seeing a OMM ~1.5-7" et 1 pixel=0.44"/pixel (HWHM)
                 ('y_stddev', [3,3.1]), # seeing a OMM ~1.5-7" et 1 pixel=0.44"/pixel (HWHM)
                 ('theta', [0,np.pi])] #pas utils pcq pas de galaxies
                 
                 
                 
                 
                 
param_ranges = OrderedDict(param_ranges)
sources = make_random_gaussians_table(n_sources, param_ranges,
                                       random_state=12345)
for col in sources.colnames:
    sources[col].info.format = '%.8g'  # for consistent table output
print(sources)
from matplotlib import pyplot as plt
from photutils.datasets import make_gaussian_sources_image
shape = (1024,1024)
im = make_gaussian_sources_image(shape,sources)
im = np.asarray(im,dtype=np.ushort)

hdu = fits.PrimaryHDU(im)

try:
    os.remove('./dataEM.fits')
except:
    pass

hdu.writeto('./dataEM.fits')

plt.figure()

plt.imshow(im)

plt.figure()
x = np.ushort(sources[0]['x_mean'])
y = np.ushort(sources[0]['y_mean'])
plt.plot(im[y-20:y+20,x])

plt.show()
