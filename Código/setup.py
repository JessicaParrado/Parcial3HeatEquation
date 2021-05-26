'''
*Universidad Sergio Arboleda
*Autores: Jessica Valentina Parrado Alfonso - Michael Steven Pinilla Mateus - Luis Alejandro Vejarano Gutierrez - Lady Geraldine Salazar Bayonao
Fecha:Mayo 2021
Computación Paralela y Distribuida
'''
from distutils.core import setup, Extension
from Cython.Build import cythonize

exts = (cythonize('heatCython.pyx'))

setup(ext_modules=exts)
