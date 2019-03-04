from setuptools import setup
from pyleo import constants
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_desc_readme = f.read(),

setup(
    name='pyleo',
    version=constants.PYLEO_VERSION,
    description='',
    author='Andrew Dorokhin',
    author_email='andrew@dorokhin.moscow',
    url='http://github.com/dorokhin/pyleo',
    packages=['pyleo',
              'pyleo.abstractions'
              ],
    long_description=long_desc_readme,
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
      "Topic :: Software Development :: Libraries"],
    package_data={
        '': ['*.md', '*.txt', '*.json']
    },
    keywords='pyleo api client',
    license='MIT'
)
