#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  setup.py
#  
from setuptools import setup
import os
package_dir = os.path.dirname(__file__)

README = open(package_dir + "README.md").read()

setup(
    name="DicksonUI",
    version="1.0.0.0",
    description="Lightweight And Full Featured Browser Based UI/GUI (Graphical User Interface Library",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Ksengine/DicksonUI",
    author="KavinduSanthusa",
    author_email="kavindusanthusa@rgmail.com",
    keywords="lightweight  full featured browser based ui gui user\
interface graphical user interface library powerful\
html css javascript js css3 html5 chrome firefox edge \
bootstrap jquery angular angularjs",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["dicksonui"],
    include_package_data=True,
)
