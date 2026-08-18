'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
'''

import setuptools
import os
from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    reqirement_lst:List[str]=[]
    try:
        requirement_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'requirement.txt')
        with open(requirement_file,'r') as file:
            # read lines from the file
            lines = file.readlines()

            # Process each lines
            for line in lines:
                reqirement=line.strip()

                # ignore the empty lines and -e .

                if reqirement and reqirement != '-e .':
                    reqirement_lst.append(reqirement)
    except FileNotFoundError:
        print("my requirements file not found")

    return reqirement_lst

print(get_requirements())


setup(
    name = "Network Security",
    version = "0.0.0.1",
    author = "sameer vishwamitre",
    packages = find_packages(),
    install_requires = get_requirements()
)