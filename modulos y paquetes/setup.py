from setuptools import setup

setup(
    name='Mensajes',
    version='1.1',
    description='Un paquete para saludar y despedir',
    author='Luis Emmanuel Estrada Rodriguez',
    author_email='luiseer09@gmail.com',
    url='https://luisdev.com',
    packages=['mensajes', 'mensajes.hola', 'mensajes.adios'],
    scripts=['test.py']
)

