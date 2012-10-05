#!/usr/bin/env python

import os
from skimage._build import cython

base_path = os.path.abspath(os.path.dirname(__file__))


def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration, get_numpy_include_dirs

    config = Configuration('filter', parent_package, top_path)
    config.add_data_dir('tests')

    cython(['_ctmf.pyx'], working_path=base_path)
    cython(['_denoise.pyx'], working_path=base_path)

    config.add_extension('_ctmf', sources=['_ctmf.c'],
                         include_dirs=[get_numpy_include_dirs()])
    config.add_extension('_denoise', sources=['_denoise.c'],
                         include_dirs=[get_numpy_include_dirs(), '../_shared'])

    return config

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(maintainer='scikit-image Developers',
          author='scikit-image Developers',
          maintainer_email='scikit-image@googlegroups.com',
          description='Filters',
          url='https://github.com/scikit-image/scikit-image',
          license='SciPy License (BSD Style)',
          **(configuration(top_path='').todict())
          )
