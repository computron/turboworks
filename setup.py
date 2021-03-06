try:
    import os
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='turboworks',
      version='0.1',
      author = 'Alex Dunn',
      description = 'Machine learning integration with Fireworks workflows',
      packages=['turboworks', 'turboworks_examples'])