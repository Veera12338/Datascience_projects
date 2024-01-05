from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''This function will return the list of requirements
    '''
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace("\n", "") for i in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements
setup(
    name='DS_KRISH_PROJECTS',
    version='0.0.1',
    author='veera',
    author_email='xyz@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)