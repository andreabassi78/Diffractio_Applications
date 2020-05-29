from pprint import pprint


# In[23]:


import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

from diffractio import degrees, mm, plt, sp, um, np
from diffractio.scalar_fields_XY import Scalar_field_XY
from diffractio.utils_drawing import draw_several_fields
from diffractio.scalar_masks_XY import Scalar_mask_XY
from diffractio.scalar_sources_XY import Scalar_source_XY


# In[24]:


from matplotlib import rcParams

rcParams['figure.figsize']=(12,10)
rcParams['figure.dpi']=200


# ## Slit

# In[25]:


num_pixels = 512

length = 100 * um
x0 = np.linspace(-length / 2, length / 2, num_pixels)
y0 = np.linspace(-length / 2, length / 2, num_pixels)
wavelength = 0.6238 * um

u1 = Scalar_source_XY(x=x0, y=y0, wavelength=wavelength)
u1.plane_wave(A=1, theta=0 * degrees, phi=0 * degrees)
# u1.laguerre_beam(p=2, l=1, r0=(0 * um, 0 * um), w0=7 * um, z=0.01 * um)

t1 = Scalar_mask_XY(x=x0, y=y0, wavelength=wavelength)
t1.slit(x0=0, size=10 * um, angle=0 * degrees)

u2 = u1 * t1

u3 = u2.RS(z=25 * um, new_field=True)

u4 = u2.RS(z=100 * um, new_field=True)

draw_several_fields((u2, u3, u4), titulos=('mask', '25 um', '100 um'))


# ## double slit

# In[54]:


num_pixels = 512

length = 100 * um
x0 = np.linspace(-length / 2, length / 2, num_pixels)
y0 = np.linspace(-length / 2, length / 2, num_pixels)
wavelength = 0.6238 * um

u1 = Scalar_source_XY(x=x0, y=y0, wavelength=wavelength)
u1.plane_wave(A=1, theta=0 * degrees, phi=0 * degrees)
# u1.laguerre_beam(p=2, l=1, r0=(0 * um, 0 * um), w0=7 * um, z=0.01 * um)

t1 = Scalar_mask_XY(x=x0, y=y0, wavelength=wavelength)
t1.double_slit(x0=0, size=2 * um, separation=10 * um, angle=0 * degrees)

u2 = u1 * t1
u3 = u2.RS(z=100 * um, new_field=True)

u4 = u2.RS(z=200 * um, new_field=True)

draw_several_fields((u2,u3,u4), titulos=('mask', '100 um', '200 um'))


# ## square

# In[49]:


num_pixels = 512

length = 100 * um
x0 = np.linspace(-length / 2, length / 2, num_pixels)
y0 = np.linspace(-length / 2, length / 2, num_pixels)
wavelength = 0.6238 * um

u1 = Scalar_source_XY(x=x0, y=y0, wavelength=wavelength)
u1.plane_wave(A=1, theta=0 * degrees, phi=0 * degrees)
#u1.laguerre_beam(p=2, l=1, r0=(0 * um, 0 * um), w0=7 * um, z=0.01 * um)

t1 = Scalar_mask_XY(x=x0, y=y0, wavelength=wavelength)
t1.square(r0=(0 * um, 0 * um), size=(50 * um, 50 * um), angle=0 * degrees)

u2 = u1 * t1

u3 = u2.RS(z=100 * um, new_field=True)

u4 = u2.RS(z=5500 * um, new_field=True)

draw_several_fields((u2,u3,u4), titulos=('mask', '100 um', '200 um'), logarithm=True)


# ## circle

# In[28]:


num_pixels = 512

length = 100 * um
x0 = np.linspace(-length / 2, length / 2, num_pixels)
y0 = np.linspace(-length / 2, length / 2, num_pixels)
wavelength = 0.6238 * um

u1 = Scalar_source_XY(x=x0, y=y0, wavelength=wavelength)
u1.plane_wave(A=1, theta=0 * degrees, phi=0 * degrees)

t1 = Scalar_mask_XY(x=x0, y=y0, wavelength=wavelength)
t1.circle(
    r0=(0 * um, 0 * um), radius=(25 * um, 25 * um), angle=0 * degrees)

u2 = u1 * t1

u3 = u2.RS(z=100 * um, new_field=True)

u4 = u2.RS(z=500 * um, new_field=True)

draw_several_fields((u2,u3,u4), titulos=('mask', '100 um', '500 um'), logarithm=True)


# ## ring

# In[29]:


num_pixels = 1024

length = 500 * um
x0 = np.linspace(-length / 2, length / 2, num_pixels)
y0 = np.linspace(-length / 2, length / 2, num_pixels)
wavelength = 0.6238 * um

u1 = Scalar_source_XY(x=x0, y=y0, wavelength=wavelength)
u1.plane_wave(A=1, theta=0 * degrees, phi=0 * degrees)

t1 = Scalar_mask_XY(x=x0, y=y0, wavelength=wavelength)
t1.ring(
    r0=(0 * um, 0 * um),
    radius1=(25 * um, 50 * um),
    radius2=(100 * um, 150 * um),
    angle=45)

u2 = u1 * t1

u3 = u2.RS(z=2.5*mm, new_field=True)

u4 = u2.RS(z=10*mm, new_field=True)

u5 = u2.RS(z=100*mm, new_field=True)

draw_several_fields((u2,u3,u4,u5), titulos=('mask','25 um', '100 um', '500 um'), logarithm=True)
   


# ## cross

# In[30]:


num_pixels = 512

length = 200 * um
x0 = np.linspace(-length / 2, length / 2, num_pixels)
y0 = np.linspace(-length / 2, length / 2, num_pixels)
wavelength = 0.6238 * um

u1 = Scalar_source_XY(x=x0, y=y0, wavelength=wavelength)
u1.plane_wave(A=1, theta=0 * degrees, phi=0 * degrees)

t1 = Scalar_mask_XY(x=x0, y=y0, wavelength=wavelength)
t1.cross(r0=(0 * um, 0 * um), size=(150 * um, 50 * um), angle=45 * degrees)

u2 = u1 * t1

u3 = u2.RS(z=150 * um, new_field=True)

u4 = u2.RS(z=5000 * um, new_field=True)

draw_several_fields((u2,u3,u4), titulos=('mask', '150 um', '5000 um'), logarithm=True)


# ## edge

# In[31]:


num_pixels = 1024

length = 200 * um
x0 = np.linspace(-length / 2, length / 2, num_pixels)
y0 = np.linspace(-length / 2, length / 2, num_pixels)
wavelength = 0.6238 * um

u1 = Scalar_source_XY(x=x0, y=y0, wavelength=wavelength)
u1.plane_wave(A=1, theta=0 * degrees, phi=0 * degrees)

t1 = Scalar_mask_XY(x=x0, y=y0, wavelength=wavelength)
t1.two_levels(level1=0, level2=.5, xcorte=0, angle=0)

u2 = u1 * t1

u3 = u2.RS(z=100 * um, new_field=True)

u4 = u2.RS(z=1000 * um, new_field=True)
 
draw_several_fields((u2,u3,u4), titulos=('mask', '100 um', '1000 um'), logarithm=True)


# In[32]:


u3.draw_profile(point1=(-50, 0), point2=(50, 0), kind='intensity', order=2)
h, profile, p1, p2 = t1.profile(
    point1=(-50, 0), point2=(50, 0), kind='intensity', order=1)
plt.plot(h, profile, 'r', lw=2);
plt.xlim(50,225)


# ## image

# In[33]:


num_pixels = 512

length = 100 * um
x0 = np.linspace(-length / 2, length / 2, num_pixels)
y0 = np.linspace(-length / 2, length / 2, num_pixels)
wavelength = 0.6238 * um

u1 = Scalar_source_XY(x=x0, y=y0, wavelength=wavelength)
u1.plane_wave(A=1, theta=0 * degrees, phi=0 * degrees)

t1 = Scalar_mask_XY(x=x0, y=y0, wavelength=wavelength)

t1.image(filename="lenaColor.png", invert=False)
u2 = u1 * t1

u3 = u2.RS(z=50 * um, new_field=True)

u4 = u2.RS(z=250 * um, new_field=True)

draw_several_fields((u2,u3,u4), titulos=('mask', '100 um', '1000 um'), logarithm=True)


# ## mask_from_function

# In[34]:


num_pixels = 512

length = 200 * um
x0 = np.linspace(-length / 2, length / 2, num_pixels)
y0 = np.linspace(-length / 2, length / 2, num_pixels)
wavelength = 0.6238 * um

u1 = Scalar_source_XY(x=x0, y=y0, wavelength=wavelength)
u1.plane_wave(A=1, theta=0 * degrees, phi=0 * degrees)


f1 = "R1-h1+np.sqrt(R1**4-(self.X-x0)**4-(self.Y-y0)**4)"
f2 = "R2-h2+np.sqrt(R2**2-(self.X)**2-(self.Y)**2)"
v_globals = {
    'R1': 6 * mm,
    'R2': 2 * mm,
    'x0': 0 * um,
    'y0': 25 * um,
    'h1': 4 * mm,
    'h2': -1 * mm,
    'np': np,
}
index = 1.5
print(v_globals)

t1 = Scalar_mask_XY(x=x0, y=y0, wavelength=wavelength)
t1.mask_from_function(
    r0=(0 * um, 0 * um),
    index=index,
    f1=f1,
    f2=f2,
    v_globals=v_globals,
    radius=(100 * um, 100 * um),
    mask=True)

u2 = u1 * t1
u2.draw('phase', has_colorbar='vertical')

u3 = u2.RS(z=2000 * um, new_field=True)

u4 = u2.RS(z=5000 * um, new_field=True)

draw_several_fields((u2,u3,u4), titulos=('mask', '100 um', '1000 um'), logarithm=True);


# ## astigmatism

# In[35]:


num_pixels = 512

length = 500 * um
x0 = np.linspace(-length / 2, length / 2, num_pixels)
y0 = np.linspace(-length / 2, length / 2, num_pixels)
wavelength = 0.6238 * um

u1 = Scalar_source_XY(x=x0, y=y0, wavelength=wavelength)
u1.plane_wave(A=1, theta=0 * degrees, phi=0 * degrees)

t1 = Scalar_mask_XY(x=x0, y=y0, wavelength=wavelength)
t1.lens(
    r0=(0 * um, 0 * um),
    radius=(250 * um, 250 * um),
    focal=(5 * mm, 10 * mm),
    angle=0 * degrees)

u2 = u1 * t1

u3 = u2.RS(z=5 * mm, new_field=True)

u4 = u2.RS(z=6.5 * mm, new_field=True)

u5 = u2.RS(z=10 * mm, new_field=True)

draw_several_fields((u2,u3,u4,u5), titulos=('mask','5 mm', '7 mm', '10 mm'), logarithm=True)


# ## Fresnel lens

# In[36]:


num_pixels = 512

length = 250 * um
x0 = np.linspace(-length / 2, length / 2, num_pixels)
y0 = np.linspace(-length / 2, length / 2, num_pixels)
wavelength = 0.6238 * um

u1 = Scalar_source_XY(x=x0, y=y0, wavelength=wavelength)
u1.plane_wave(A=1, theta=0 * degrees, phi=0 * degrees)

t1 = Scalar_mask_XY(x=x0, y=y0, wavelength=wavelength)
t1.fresnel_lens(
    r0=(0 * um, 0 * um),
    radius=(125 * um, 125 * um),
    focal=(1 * mm, 1 * mm),
    angle=45 * degrees,
    kind='amplitude',
    phase=np.pi,
    mask=True)
u2 = u1 * t1
u2.draw(kind='amplitude')
u3 = u2.RS(z=1 * mm, new_field=True)
u3.draw()
plt.xlim(-10,10)
plt.ylim(-10,10)

t1.fresnel_lens(
    r0=(0 * um, 0 * um),
    radius=(125 * um, 125 * um),
    focal=(1 * mm, 1 * mm),
    angle=0 * degrees,
    kind='phase',
    phase=np.pi,
    mask=True)
u2 = u1 * t1
u2.draw(kind='phase')
u3 = u2.RS(z=1 * mm, new_field=True)
u3.draw();
plt.xlim(-10,10)
plt.ylim(-10,10);


# ## biprism

# In[37]:


num_pixels = 512

length = 250 * um
x0 = np.linspace(-length / 2, length / 2, num_pixels)
y0 = np.linspace(-length / 2, length / 2, num_pixels)
wavelength = 0.6238 * um

u1 = Scalar_source_XY(x=x0, y=y0, wavelength=wavelength)
u1.plane_wave(A=1, theta=0 * degrees, phi=0 * degrees)

t1 = Scalar_mask_XY(x=x0, y=y0, wavelength=wavelength)

t1.biprism_fresnel(
    r0=(0 * um, 0 * um), width=125 * um, height=5 * um, n=1.5)
u2 = u1 * t1
u2.draw(kind='phase')

u3 = u2.RS(z=1.25 * mm, new_field=True)

u4 = u2.RS(z=2.5 * mm, new_field=True)

draw_several_fields((u3,u4), titulos=('1.25 mm', '2.5 mm'), logarithm=True)


# ## axicon

# In[38]:


num_pixels = 512

length = 250 * um
x0 = np.linspace(-length / 2, length / 2, num_pixels)
y0 = np.linspace(-length / 2, length / 2, num_pixels)
wavelength = 0.6238 * um

u1 = Scalar_source_XY(x=x0, y=y0, wavelength=wavelength)
u1.plane_wave(A=1, theta=0 * degrees, phi=0 * degrees)

t1 = Scalar_mask_XY(x=x0, y=y0, wavelength=wavelength)
t1.axicon(r0=(0 * um, 0 * um), radius=125 * um, height=2 * um, n=1.5)

u2 = u1 * t1
u2.draw(kind='phase')
u3 = u2.RS(z=2.5 * mm, new_field=True)

u4 = u2.RS(z=5 * mm, new_field=True)

u5 = u2.RS(z=7.5 * mm, new_field=True)

draw_several_fields((u3,u4, u5), titulos=('2.5 mm', '5 mm', '7.5 mm'), logarithm=True)


# ## Laguerre spiral

# In[39]:


num_pixels = 512

length = 250 * um
x0 = np.linspace(-length / 2, length / 2, num_pixels)
y0 = np.linspace(-length / 2, length / 2, num_pixels)
wavelength = 0.6238 * um

u1 = Scalar_source_XY(x=x0, y=y0, wavelength=wavelength)
u1.plane_wave(A=1, theta=0 * degrees, phi=0 * degrees)

t1 = Scalar_mask_XY(x=x0, y=y0, wavelength=wavelength)
t1.laguerre_gauss_spiral(
    kind='intensity', l=4, r0=(0 * um, 0 * um), w0=20 * um, z=0.01 * um)

u2 = u1 * t1
u3 = u2.RS(z=5 * mm, new_field=True)

u4 = u2.RS(z=20 * mm, new_field=True)


draw_several_fields((u2, u3,u4), titulos=('mask', '2.5 mm', '20 mm'), logarithm=True)


# ## forked grating

# In[40]:


period= 20*um
num_pixels = 1024

length = 250 * um
x0 = np.linspace(-length / 2, length / 2, num_pixels)
y0 = np.linspace(-length / 2, length / 2, num_pixels)
wavelength = 0.6238 * um

u1 = Scalar_source_XY(x=x0, y=y0, wavelength=wavelength)
u1.plane_wave(A=1, theta=0 * degrees, phi=0 * degrees)

t1 = Scalar_mask_XY(x=x0, y=y0, wavelength=wavelength)
t1.forked_grating(kind='amplitude',
    r0=(0 * um, 0 * um), period=period, l=3, alpha=2, angle=0 * degrees)

zt = 2 * period**2 / wavelength

u2 = u1 * t1

u4 = u2.RS(z=.5 * zt, new_field=True)

u5 = u2.RS(z=2 * zt, new_field=True)
   

draw_several_fields((u2,u4, u5), titulos=('mask', '.5 zt', '2 zt'), logarithm=True)


# ## Roughness and speckle

# In[41]:


num_pixels = 512

length = 250 * um
x0 = np.linspace(-length / 2, length / 2, num_pixels)
y0 = np.linspace(-length / 2, length / 2, num_pixels)
wavelength = 0.6238 * um

u1 = Scalar_source_XY(x=x0, y=y0, wavelength=wavelength)
u1.plane_wave(A=1, theta=0 * degrees, phi=0 * degrees)

t1 = Scalar_mask_XY(x=x0, y=y0, wavelength=wavelength)
t1.roughness(t=(20 * um, 20 * um), s=1 * um)

u2 = u1 * t1
u2.draw(kind='phase')

u3 = u2.RS(z=0.01 * mm, new_field=True)

u4 = u2.RS(z=5 * mm, new_field=True)

u5 = u2.RS(z=10 * mm, new_field=True)

draw_several_fields((u3,u4, u5), titulos=('1 mm', '5 mm', '10 mm'), logarithm=True);





num_pixels = 1024

length = 250 * um
x0 = np.linspace(-length / 2, length / 2, num_pixels)
y0 = np.linspace(-length / 2, length / 2, num_pixels)
wavelength = 0.6238 * um

u1 = Scalar_source_XY(x=x0, y=y0, wavelength=wavelength)
u1.gauss_beam(A=1, r0=(0,0), w0=(10,10),theta=0 * degrees, phi=0 * degrees)

t1 = Scalar_mask_XY(x=x0, y=y0, wavelength=wavelength)
t1.blazed_grating(
    period=20 * um,
    height=1 * um,
    index=1.5,
    x0=0 * um,
    angle=45 * degrees)

t1.draw('phase')

u2 = u1 * t1

u3 = u2.RS(z=1*mm, new_field=True)

u4 = u2.RS(z=2*mm, new_field=True)

u5 = u2.RS(z=3*mm, new_field=True)

draw_several_fields((u3,u4, u5), titulos=('1 mm', '2 mm', '3 mm'), logarithm=True);



