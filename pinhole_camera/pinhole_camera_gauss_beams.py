from pprint import pprint

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

from diffractio import degrees, mm, plt, sp, um, np
from diffractio.scalar_fields_XY import Scalar_field_XY
from diffractio.scalar_masks_XY import Scalar_mask_XY
from diffractio.scalar_sources_XY import Scalar_source_XY
from matplotlib import rcParams

from pinholes_utils_drawing import draw_several_fields

from pinholes import random_points_mask

#rcParams['figure.figsize']=(12,10)
#rcParams['figure.dpi']=400

num_pixels = 1024#2048

length = 4000.0 * um
x0 = np.linspace(-length / 2, length / 2, num_pixels)
y0 = np.linspace(-length / 2, length / 2, num_pixels)
wavelength = 0.5 * um

u1 = Scalar_source_XY(x=x0, y=y0, wavelength=wavelength)
#u1.plane_wave(A=1, theta=0 * degrees, phi=0 * degrees)

step = 40 *um

xs0 = np.linspace(-length/2, length/2, int(length/step))
ys0 = np.linspace(-length/2, length/2, int(length/step))

ratio = int(num_pixels/(length/step))

# N_thetas = 21
# N_phis = 7

# NA = 0.02
# thetas = np.linspace(0, 2* np.pi, N_thetas) 
# phis = np.linspace (0, NA, N_phis) 


t2 = Scalar_mask_XY(x=x0, y=y0, wavelength=wavelength)
#t2.image(filename="ph.png", invert=False)
r = 15 * um 
r_big = 300 * um
#t2.circle(r0=(0 * um, 0 * um), radius=(r, r), angle=0 * degrees)
t2.u = random_points_mask(dimension = np.array([num_pixels, num_pixels]),
                          radiuspinhole = int(r*num_pixels/length),
                          n = 50,
                          radiusmask = int(r_big*num_pixels/length))
    


t1 = Scalar_mask_XY(x=x0, y=y0, wavelength=wavelength)
t1.image(filename="pi_small.tif", invert=False)
u_t = t1.u 

u5 = Scalar_field_XY(x=x0, y=y0, wavelength=wavelength)
intensity = Scalar_field_XY(x=x0, y=y0, wavelength=wavelength)

u_start = Scalar_field_XY(x=x0, y=y0, wavelength=wavelength)

#jj=0
for  index_y, ys in enumerate(ys0):

    for  index_x, xs in enumerate(xs0):
         
        if u_t[int(index_y*ratio),int(index_x*ratio)] == 0: 
            continue
        # else:
        #     jj += 1
        #     print('xs,ys: ',xs,ys)
        #     print('indexes:', index_x,index_y)
        #     continue
        r0 = (xs,ys)
        
        w0 = (10*um,10*um)
        u1.gauss_beam(r0 = r0,
                      w0 = w0,
                      z0=0 * um,
                      A=1)
        
        # u1.spherical_wave(A=1.0,
        #                    r0=r0,
        #                    z0=0,
        #                    radius=1000 * um)
        
        u2 = u1 * t1
        u_start += u2 
        
        u3 = u2.RS(z=80000 * um, new_field=True, verbose=False)
        
        u4 = u3 * t2
        

        #draw_several_fields((u1,u2,u3,u4),titulos=('1', '2', '3', '4'))
        u = u4.RS(z=40000 * um, new_field=True, verbose=False)
        
        u5 += u
        intensity.u += np.abs(u.u)**2    
        
        #title = 'theta:'+str(theta) + ' phi:' + str(phi)        
        title = 'gauss beams. r: '+ str(r)
        
        draw_several_fields((u_start,u3,u4,u,u5,intensity),
                            titulos=('start', 'ph-', 'ph', 'detector','real','intensity'),
                            title = title,
                            mode = 'real',
                            logarithm = True,
                            normalize = False)
        
        plt.pause(0.001)