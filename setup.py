from setuptools import setup, find_packages
from typing import List

#Declaring variables for setup function
PROJECT_NAME="housing-predictor"
VERSION="0.0.5"
AUTHOR="Rudra Shankar"
DESCRIPTION="This is my first end-to-end ML project"

REQUIREMENT_FILE_NAME="requirements.txt"
SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL=True

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirements mentioned in 
    requirements.txt file

    return: This function is going to return a list which contains name of libraries mentioned 
    in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
install_requires=get_requirements_list()
)

