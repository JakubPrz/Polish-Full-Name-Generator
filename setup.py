from pathlib import Path
from setuptools import setup

setup(
    name='pfng',
    version='1.0.1',
    description='Polish full names generator',
    long_description=(Path(__file__).parent / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    author='Jakub Przepiórka',
    author_email='jakub.przepiorka.contact.me@gmail.com',
    license='MIT',
    url='https://github.com/JakubPrz/Polish-Full-Names-Generator',
    python_requires='>=3.10',
    platforms=['Windows'],
    packages=['pfng'],
    package_data={'pfng': ['data/*.csv']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'Natural Language :: English',
        'Topic :: Utilities',
        'Programming Language :: Python :: 3.10',
        'Operating System :: Microsoft :: Windows',
    ],
)
