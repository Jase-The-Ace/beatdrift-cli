from codecs import open
from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='beatdrift-cli',
    version='0.8.0',
    description='List all your AWS resources,regions, and services, save it as json, then compare with terraform state file to identify infrastructural drift.',
    long_description=long_description,
    url='https://github.com/Jase-The-Ace/beatdrift-cli',
    author='Jason O. Aboh',
    author_email='bigbossw107@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='aws boto3 listings resources region services',
    packages=['beatdrift-cli'],
    install_requires=['boto3>=1.16.57', 'app_json_file_cache>=0.2.2'],
    entry_points={
        'console_scripts': [
            'beatdrift_cli=beatdrift_cli.__main__:main',
            'beatdrift-cli=beatdrift_cli.__main__:main',
        ],
    },
    include_package_data=True,
)
