import os
from setuptools import setup, find_packages

BASEDIR = os.path.dirname(os.path.abspath(__file__))
VERSION = "0.0.1"
REQUIREMENTS = []
DEPENDENCY_LINKS = []

os.chdir(os.path.normpath(BASEDIR))

with open(os.path.join(BASEDIR, 'requirements.txt')) as fp:
    lines = fp.readlines()
    for line in lines:
        line = line.strip()
        if ("http://" in line or "https://" in line or "ssh://" in line) and "#egg=" in line:
            parts = line.split("#egg=")
            REQUIREMENTS.append(parts[-1])
            DEPENDENCY_LINKS.append(line)
        elif len(line) and line[0] != "#" and line[0] != "-":
            REQUIREMENTS.append(line)

setup(
    name='AlphaPose',
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    description='AlphaPose pytorch branch',
    long_description='video event stream consumer',
    url='https://github.com/WildflowerSchools/AlphaPose/tree/wf-pytorch',
    install_requires=REQUIREMENTS,
    dependency_links=DEPENDENCY_LINKS
)
