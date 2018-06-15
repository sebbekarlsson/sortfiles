from setuptools import setup, find_packages


setup(
    name='sortfiles',
    version='1.0',
    install_requires=[
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'sortfiles = sortfiles.bin:run'
        ]
    }
)
