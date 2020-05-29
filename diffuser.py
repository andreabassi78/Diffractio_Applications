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
rcParams['figure.dpi']=200



num_pixels = 512

length = 500 * um
x0 = np.linspace(-length / 2, length / 2, num_pixels)
y0 = np.linspace(-length / 2, length / 2, num_pixels)
wavelength = 0.6238 * um

u1 = Scalar_source_XY(x=x0, y=y0, wavelength=wavelength)
u1.plane_wave(A=1, theta=0 * degrees, phi=30 * degrees)



t1 = Scalar_mask_XY(x=x0, y=y0, wavelength=wavelength)
t1.roughness(t=(0.2 * um, 0.2 * um), s=1 * um)
###############################
u2 = u1 * t1
u2.draw(kind='phase')

u3 = u2.RS(z=1 * mm, new_field=True)

u4 = u2.RS(z=5 * mm, new_field=True)

u5 = u2.RS(z=10 * mm, new_field=True)

draw_several_fields((u3,u4, u5), titulos=( '1 mm', '5 mm', '10 mm'), logarithm=True);


