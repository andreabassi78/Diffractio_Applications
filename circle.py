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


# ## circle

num_pixels = 1024

length = 600 * um
x0 = np.linspace(-length / 2, length / 2, num_pixels)
y0 = np.linspace(-length / 2, length / 2, num_pixels)
wavelength = 0.6238 * um

u1 = Scalar_source_XY(x=x0, y=y0, wavelength=wavelength)
u1.plane_wave(A=1, theta=0 * degrees, phi=0 * degrees)

t1 = Scalar_mask_XY(x=x0, y=y0, wavelength=wavelength)
t1.circle(
    r0=(0 * um, 0 * um), radius=(30 * um, 30 * um), angle=0 * degrees)

t1.circle(
    r0=(30 * um, 30 * um), radius=(30 * um, 30 * um), angle=0 * degrees)


u2 = u1 * t1

u3 = u2.RS(z=100 * um, new_field=True)

u4 = u2.RS(z=1000 * um, new_field=True)

draw_several_fields((u2,u3,u4), titulos=('mask', '100 um', '500 um'), logarithm=True)
