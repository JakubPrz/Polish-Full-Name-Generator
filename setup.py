# -*- coding: utf-8 -*-

import sys
from re import sub
from os import system
from pathlib import Path
from shutil import rmtree
from setuptools import setup, Command


# Package meta-data
NAME            = 'pfng'
DESCRIPTION     = 'Full name generator powered by thousands of Polish names and surnames. Both male and female full names can be generated.'
URL             = 'https://github.com/JakubPrz/Polish-Full-Name-Generator'
EMAIL           = 'jakub.przepiorka.contact.me@gmail.com'
AUTHOR          = 'Jakub Przepiórka'
REQUIRES_PYTHON = '>=3.10'
VERSION         = '1.0.2'
LICENSE         = 'MIT'
PACKAGES        = ['pfng']
PACKAGE_DATA    = {'pfng': ['data/*.csv']}
PLATFORMS       = ['Windows']


# Required packages
REQUIRED = []


# Optional packages
EXTRAS = {}


# Current path
HERE = Path(__file__).parent


# Import the README and use it as the long description
try:
    with (HERE / "README.md").open(encoding="utf-8") as file:
        row_text = file.read()
        LONG_DESCRIPTION = sub(r'[\\*]', '', row_text)  # remove some characters
except FileNotFoundError:
    LONG_DESCRIPTION = DESCRIPTION


# Load the package's __version__.py as a dict
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(HERE / project_slug / '__version__.py') as file:
        exec(file.read(), about)
else:
    about['__version__'] = VERSION


class UploadCommand(Command):
    """Support for setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds...')
            rmtree(HERE / 'dist')
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution...')
        system(f'{sys.executable} setup.py sdist bdist_wheel')

        self.status('Uploading the package to PyPI via Twine...')
        system('twine upload dist/*')

        self.status('Pushing git tags...')
        system(f"git tag v{about['__version__']}")
        system('git push --tags')

        sys.exit()


setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=PACKAGES,
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    package_data=PACKAGE_DATA,
    license=LICENSE,
    platforms=PLATFORMS,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Education',
        'Topic :: Utilities',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.10',
    ],
    cmdclass={
        'upload': UploadCommand,
    },
)
