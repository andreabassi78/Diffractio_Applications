from pprint import pprint

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

from diffractio import degrees, mm, plt, sp, um, np
from diffractio.scalar_fields_XY import Scalar_field_XY
from diffractio.utils_drawing import draw_several_fields
from diffractio.scalar_masks_XY import Scalar_mask_XY
from diffractio.scalar_sources_XY import Scalar_source_XY

from matplotlib import rcParams

rcParams['figure.figsize']=(12,10)
rcParams['figure.dpi']=400


num_pixels = 1024#2048

length = 1000.0 * um
x0 = np.linspace(-length / 2, length / 2, num_pixels)
y0 = np.linspace(-length / 2, length / 2, num_pixels)
wavelength = 0.5 * um


u1 = Scalar_source_XY(x=x0, y=y0, wavelength=wavelength)
u1.plane_wave(A=1, theta=0 * degrees, phi=0 * degrees)


source_length = length/2
N_sources = 3
xs0 = np.linspace(-source_length / 2, source_length / 2, N_sources)
ys0 = np.linspace(-source_length / 2, source_length / 2, N_sources)


t1 = Scalar_mask_XY(x=x0, y=y0, wavelength=wavelength)
t1.image(filename="pi.tif", invert=False)

t2 = Scalar_mask_XY(x=x0, y=y0, wavelength=wavelength)
t2.image(filename="ph.png", invert=False)
r = 20 * um 
#t2.circle(r0=(0 * um, 0 * um), radius=(r, r), angle=0 * degrees)

#initu5 = False
u5 = Scalar_field_XY(x=x0, y=y0, wavelength=wavelength)
intensity = Scalar_field_XY(x=x0, y=y0, wavelength=wavelength)


for index_x in range(num_pixels):
    for  index_y in range(num_pixels):
        #print('indexes:',index_x,index_y)
        
        x= x0[index_x]
        y= y0[index_y]
        
        r0 = (x,y)        
        
        #print('r0 = ', r0)                  
        # u1.spherical_wave(A=1.0,
        #                   r0=r0,
        #                   z0=0,
        #                   radius=1000 * um,
        #                   mask=False, normalize=False)
    
        u_t = t1.u  
        
        if u_t[index_y,index_x] > 0:
            
            w0 = (0.1*um,0.1*um)
            u1.gauss_beam(r0 = r0,
                          w0 = w0,
                          z0=0 * um,
                          A=1,
                          theta=0,
                          phi=0)
            # NA = 0.1
        
            # theta = NA* xs0[index_x]/source_length * 180*degrees 
            # phi = NA* ys0[index_y]/source_length * 180*degrees
            # u1.plane_wave(A=1, theta=theta, phi=phi) 
            
            # print(theta,phi)
            #plt.figure()
            #plt.imshow(np.abs(u_t))
            #plt.pause(0.01)
            
            u2 = u1 * t1
            
            u3 = u2.RS(z=40000 * um, new_field=True)
            
            #t2 = Scalar_mask_XY(x=x0, y=y0, wavelength=wavelength)
            
            u4 = u3 * t2
            
            #draw_several_fields((u1,u2,u3,u4),titulos=('1', '2', '3', '4'))
            u = u4.RS(z=20000 * um, new_field=True)
            
            
            u5 += u
            intensity.u += np.abs(u.u)**2    
                
            draw_several_fields((u1,u2,u4,u,u5, intensity),titulos=('1', '2', '3', 'u','5','intensity'))
            plt.pause(0.001)
          

#u5.normalize()
#draw_several_fields((u2,u3,u4,u5),titulos=('in', 'ph-', 'ph+', 'out'))

#u5.draw(kind='intensity')


