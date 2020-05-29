from pprint import pprint

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

from diffractio import degrees, mm, plt, sp, um, np
from diffractio.scalar_fields_XY import Scalar_field_XY
from my_utils_drawing import draw_several_fields
from diffractio.scalar_masks_XY import Scalar_mask_XY
from diffractio.scalar_sources_XY import Scalar_source_XY

from matplotlib import rcParams

rcParams['figure.figsize']=(12,10)
rcParams['figure.dpi']=400

num_pixels = 512#2048

length = 1000.0 * um
x0 = np.linspace(-length / 2, length / 2, num_pixels)
y0 = np.linspace(-length / 2, length / 2, num_pixels)
wavelength = 0.5 * um

u0 = Scalar_source_XY(x=x0, y=y0, wavelength=wavelength)

u1 = Scalar_source_XY(x=x0, y=y0, wavelength=wavelength)
#u1.plane_wave(A=1, theta=0 * degrees, phi=0 * degrees)

u = Scalar_field_XY(x=x0, y=y0, wavelength=wavelength)
intensity = Scalar_field_XY(x=x0, y=y0, wavelength=wavelength)
 
NA = 0.1
 
theta = NA* 0.5 * 180*degrees*0
phi = NA* 0.5 * 180*degrees*0

u0.plane_wave(A=1, theta=theta, phi=phi) 

u1.plane_wave(A=1, theta=-theta, phi=-phi) 
 
u = u0 #+ u1

intensity.u = np.abs(u1.u)**2 + np.abs(u0.u)**2    
#intensity.u = np.abs(u1.u+u0.u)**2    

u_p = u.RS(z=5000 * um, new_field=True, verbose=True)
 
u_f = u_p.RS(z=20000 * um, new_field=True, verbose=True)
 
draw_several_fields((u0,u1,u,intensity,u_p,u_f),
                    titulos=('0', '1', 'u','intensity', 'p','f'),
                    mode = 'real')