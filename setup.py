from setuptools import setup
from pyleo import constants
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name='pyleo',
    version=constants.PYLEO_VERSION,
    description='Unofficial Lingualeo API python library',
    author='Andrew Dorokhin',
    author_email='andrew@dorokhin.moscow',
    url='http://github.com/dorokhin/pyleo',
    packages=[
        'pyleo',
        'pyleo.abstractions',
        'pyleo.exceptions',
        'pyleo.cli',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=[],
    python_requires='>=3.4',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Software Development :: Libraries"],
    package_data={
        '': ['*.md', '*.txt', '*.json']
    },
    keywords='pyleo api client lingualeo english-learning',
    license='MIT',
    entry_points={
        'console_scripts': ['pyleo=pyleo.cli.command_line:main'],
    },
)
