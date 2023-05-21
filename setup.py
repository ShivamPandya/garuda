from setuptools import setup, find_packages

setup(
    name='garuda',
    author='Shivam Pandya',
    url='https://github.com/shivampandya/garuda',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'garuda = garuda.garuda:main',
        ],
    },
)
