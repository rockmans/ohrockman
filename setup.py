import sys
from setuptools import setup, find_packages

import ohrockman

kw = {}
if sys.version_info >= (3,):
    kw['use_2to3'] = True

setup(name=ohrockman.__name__,
      version=ohrockman.__version__,
      description=ohrockman.__description__,
      long_description=open('README.md').read(),
      keywords='',
      author=ohrockman.__author__,
      author_email=ohrockman.__author_email__,
      url=ohrockman.__url__,
      license=open('LICENSE').read(),
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      zip_safe=False,
      test_suite='nose.collector',
      install_requires=open('requirements.txt').read().splitlines(),
      setup_requires=[],
      tests_require=open('test_requirements.txt').read().splitlines(),
      namespace_packages=[],
      **kw)   
