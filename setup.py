from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="anime_reccomendation_system",
    version="0.1",
    author="Sri Harshitha J",
    packages=find_packages(),
    install_requires = requirements,
)