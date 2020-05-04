from setuptools import setup, find_packages
from pathlib import Path

with open('requirements.txt', 'r') as f:
    dependencies = [l.strip() for l in f]

setup(
   name='remotenb',
   version='0.1.0',
   author='Utkarsh Giri',
   author_email='ugiri@perimeterinstitute.ca',
   packages=['remotenb'],
   scripts = [x.as_posix() for x in list(Path('remotenb').glob('*'))],
   description='Script to automate remote notebook run',
   install_requires=dependencies,
)
