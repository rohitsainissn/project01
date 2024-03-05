from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    try:
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.strip() for req in requirements]
    except FileNotFoundError:
        print(f"Error: Requirements file '{file_path}' not found.")
    return requirements

setup(
    name='Diamond',
    version='0.0.1',
    author='rohit',
    author_email='rohitsainidtu@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)
