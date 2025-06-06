from setuptools import find_packages,setup

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->list[str]:
    '''
    This function will return the list of requirements.
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements
        

setup(
    name='MLOps',
    version='0.0.1',
    author='Ayush Jain',
    author_email='21bds008@iiitdwd.ac.in',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)