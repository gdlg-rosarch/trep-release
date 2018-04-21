#!/usr/bin/python

try:
    from setuptools import setup, Extension, convert_path
except ImportError:
    from distutils.core import setup
    from distutils.util import convert_path
    from distutils.extension import Extension
import numpy


include_dirs = [numpy.get_include()]
cflags=[]
ldflags=[]
define_macros=[]
cmd_class = {}
cmd_options = {}


################################################################################

ext_modules = []

_trep = Extension('trep._trep',
                  include_dirs=include_dirs,
                  define_macros=define_macros,
                  extra_compile_args=cflags,
                  extra_link_args=ldflags,
                  sources = [
                      'trep/_trep/midpointvi.c',
                      'trep/_trep/system.c',
                      'trep/_trep/math-code.c',
                      'trep/_trep/frame.c',
                      'trep/_trep/_trep.c',
                      'trep/_trep/config.c',
                      'trep/_trep/potential.c',
                      'trep/_trep/force.c',
                      'trep/_trep/input.c',
                      'trep/_trep/constraint.c',
                      'trep/_trep/frametransform.c',
                      'trep/_trep/spline.c',
                      'trep/_trep/tapemeasure.c',
                      
                      # Constraints
                      'trep/_trep/constraints/distance.c',
                      'trep/_trep/constraints/plane.c',
                      'trep/_trep/constraints/point.c',
                      
                      # Potentials
                      'trep/_trep/potentials/gravity.c',
                      'trep/_trep/potentials/linearspring.c',
                      'trep/_trep/potentials/configspring.c',
                      'trep/_trep/potentials/nonlinear_config_spring.c',
                      
                      # Forces
                      'trep/_trep/forces/damping.c',
                      'trep/_trep/forces/lineardamper.c',
                      'trep/_trep/forces/configforce.c',
                      'trep/_trep/forces/bodywrench.c',
                      'trep/_trep/forces/hybridwrench.c', 
                      'trep/_trep/forces/spatialwrench.c',
                      'trep/_trep/forces/pistonexample.c',
                      ],
                  depends=[
                      'trep/_trep/trep.h',
                      'trep/_trep/c_api.h'
                      ])

ext_modules += [_trep]

_polyobject = Extension('trep.visual._polyobject',
                        extra_compile_args=[],
                        extra_link_args=['-lGL'],
                        sources = ['trep/visual/_polyobject.c'])
ext_modules += [_polyobject]


setup (name = 'trep',
       version = '1.0.3',
       description = 'trep is used to simulate mechanical systems.',
       long_description="Trep is a Python module for modeling articulated rigid body mechanical systems in \
generalized coordinates. Trep supports basic simulation but it is primarily designed to serve as a \
calculation engine for analysis and optimal control algorithms that require 1st and 2nd derivatives \
of the system's dynamics.",
       author = 'Elliot Johnson',
       author_email = 'elliot.r.johnson@gmail.com',
       url = 'http://nxr.northwestern.edu/trep',
       license='GPLv3',
       platforms='Linux, Mac, Windows',
       packages=['trep',
                 'trep.constraints',
                 'trep.potentials',
                 'trep.forces',
                 'trep.visual',
                 'trep.puppets',
                 'trep.discopt',
                 'trep.ros'
                 ],
       package_data={
           'trep.visual' : ['icons/*.svg'], 'trep' : ['_trep/*.h']
           },
       ext_modules=ext_modules,
       cmdclass=cmd_class,
       command_options=cmd_options,
       zip_safe=False,
       install_requires=[
           'numpy',
           'scipy',
       ],
       headers=[
           'trep/_trep/trep.h',
           'trep/_trep/c_api.h'
           ])
