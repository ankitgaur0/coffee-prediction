from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str) ->List[str] :
    '''
         this function iterate the packages from the Requirements.txxt file
         and return to the setup function to execute in list format .
    '''
    Requirements=[]
    with open(file_path) as file_obj:
        Requirements=file_obj.readlines()
        #use list compresension for replace the \n to blank space ""
        Requirements=[req.replace("\n", "") for req in Requirements]

        if HYPEN_E_DOT in Requirements:
            Requirements.remove(HYPEN_E_DOT)

    return Requirements



setup(
    name="coffee_prediction",
    version='0.0.01',
    author="ankit1",
    author_email="ankitparashar000@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('Requirements.txt')
)