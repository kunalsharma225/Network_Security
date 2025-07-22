from setuptools import find_packages,setup
from typing import List 
HYPHEN_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","")for req in requirements]
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    name='Network_Security',
    version='0.0.1',
    author='Kunal',
    author_email='kunalsharma2220@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)