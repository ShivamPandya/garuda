from setuptools import setup, find_packages

setup(
    name='garuda',
    version='0.1.0',
    author='Shivam Pandya',
    url='https://github.com/shivampandya/garuda',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'garuda = garuda.garuda:main',
        ],
    },
)
