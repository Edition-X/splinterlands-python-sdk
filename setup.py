#/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name='SplinterlandsSDK',  # name of the package
    version='0.1.0',  # version of the package
    packages=find_packages(),  # list of packages to include in the package
    py_modules=['SplinterlandsSDK'],
    install_requires=['requests'],  # list of dependencies
    author='Daniel J Kelly',  # your name
    author_email='danielkelly89@gmail.com',  # your email
    description='A Python library for interacting with the Splinterlands API',  # a short description of the package
    url='https://github.com/Edition-X/splinterlands-python-sdk',  # the URL of the package's repository
)
