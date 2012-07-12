import os
from distutils.core import setup

readme = open(os.path.join(os.path.dirname(__file__), 'README'))
README = readme.read()
readme.close()

version = '0.1'


setup(name='miniredis',
      version=version,
      description='A lightweight 20-lines redis client',
      long_description=README,
      author='Volodymyr Sergeyev',
      author_email='vova.sergeyev@gmail.com',
      maintainer='Volodymyr Sergeyev',
      maintainer_email='vova.sergeyev@gmail.com',
      packages = ['miniredis',],
      license = 'BSD',
      download_url ='http://github.com/vsergeyev/miniredis-python',
      url='http://github.com/vsergeyev/miniredis-python',
      classifiers=['Development Status :: 3 - Alpha',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: Utilities',],)