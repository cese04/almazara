
from setuptools import setup, find_packages

setup(name='almazara',
      version=0.1,
      description='Feature extraction library for Python',
      author='Emiliano Solorzano Espindola',
      author_email='carlosemiliano04@gmail.com',
      license='MIT',
      packages=find_packages(exclude=['docs', 'tests']),
      install_requires=['numpy', 'scipy', 'scikit-learn']
      )