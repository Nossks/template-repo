from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as fo:
        requirements = fo.readlines()
        requirements = [r.replace('\n','') for r in requirements]
    if '-e .' in requirements:
        requirements.remove('-e .')
    return requirements

setup(
    name='mlops',
    version='0.0.1',
    author='Aryan',
    author_email='gairolaaryn@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)