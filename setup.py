from typing import List

from setuptools import find_packages, setup
Hyphe_e_dot = "-e ."



def get_requirements()-> List[str]:
    requirements_list:List[str]=[]
    with open('requirements.txt', 'r') as f:
        requirements_list = [line.rstrip() for line in f]
        if Hyphe_e_dot in requirements_list:
            requirements_list.remove(Hyphe_e_dot)
        
    return requirements_list
        

setup(
    name="sensor",
    version="0.0.1",
    author="Manoj",
    author_email="manojbahuguna1979@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
    )



     