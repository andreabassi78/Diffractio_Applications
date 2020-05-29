# -*- coding: utf-8 -*-
"""
Created on Thu May  7 10:59:46 2020

@author: Andrea Bassi
"""

import time

from diffractio import degrees, mm, np, num_max_processors, plt, um
from diffractio.scalar_fields_X import (Scalar_field_X,
                                        extended_polychromatic_source,
                                        extended_source_multiprocessing,
                                        polychromatic_multiprocessing)
from diffractio.scalar_masks_X import Scalar_mask_X
from diffractio.scalar_sources_X import Scalar_source_X
from diffractio.utils_multiprocessing import (_pickle_method, _unpickle_method,
                                              execute_multiprocessing)
from multiprocessing import Pool
from diffractio.utils_optics import (gauss_spectrum, lorentz_spectrum,
                                     uniform_spectrum)

from diffractio.scalar_fields_XZ import Scalar_field_XZ

from matplotlib import rcParams

rcParams['figure.figsize']=(6,4)
rcParams['figure.dpi']=75

# print(num_max_processors)


# x = np.linspace(-300 * um, 300 * um, 1024)
# wavelength = 0.850 * um
# num_fuentes = 100

# S = 1 * um
# z0 = 0 * um

# distance = 5 * mm

# red = Scalar_mask_X(x, wavelength)

# red.slit(x0=0, size=25 * um)

# #red.ronchi_grating(x0=0 * um, period=period, fill_factor=0.5)

# #lens = Scalar_mask_X(x, wavelength)
# #lens.lens(focal=focal, radius=30 * mm)

# u1 = Scalar_source_X(x, wavelength)

# # posiciones de la fuente
# x0s = np.linspace(-S / 2, S / 2, num_fuentes)
# intensities = Scalar_field_X(x, wavelength)

# time1 = time.time()
# for x0 in x0s:
#     u1.spherical_wave(
#         A=1,
#         x0=x0,
#         z0=z0,
#         radius=100000 * um,
#         mask=False,
#         normalize=True)
#     u2 = u1 * red
#     u2.RS(z=distance, new_field=False, verbose=False)
#     intensities.u = intensities.u + abs(u2.u)**2
#     #intensities.u = intensities.u + u2.u

# #intensities.u = abs(intensities.u)**2
# intensities.u = intensities.u / intensities.u.max()
# time_proc = time.time() - time1
# print("num_proc: {}, time={}".format(1, time_proc))
# intensities.draw(kind='amplitude')


def __experiment_extended_source__(x0):

    x = np.linspace(-100 * um, 100 * um, 128)
    wavelength = 0.850 * um
    z0 = -500 * mm
    period = 50 * um
    focal = 5 * mm

    red = Scalar_mask_X(x, wavelength)
    red.ronchi_grating(x0=0 * um, period=period, fill_factor=0.5)

    lens = Scalar_mask_X(x, wavelength)
    lens.lens(focal=focal, radius=30 * mm)

    u1 = Scalar_source_X(x, wavelength)

    # posiciones de la fuente

    u1.spherical_wave(
        A=1., x0=x0, z0=z0, radius=100000 * um, mask=False, normalize=True)
    u2 = u1 * red * lens
    u2.RS(z=focal, new_field=False, verbose=False)

    return u2

x0s = np.linspace(-150 * um, 150 * um, 2)
x0_central = 0 * um

# intensity0, u_s0, time_proc0 = extended_source_multiprocessing(
#     __experiment_extended_source__,
#     x0_central,
#     num_processors=1,
#     verbose=True)

intensity, u_s, time_proc = extended_source_multiprocessing(
    __experiment_extended_source__,
    x0s,
    num_processors=num_max_processors,
    verbose=True)

plt.figure()
#plt.plot(u_s0.x, intensity0, 'k', lw=2, label='punctual source')
plt.plot(u_s[0].x, intensity, 'r', lw=2, label='extended source')
plt.legend()
plt.ylim(bottom=0);
