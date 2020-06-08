#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  setup.py
#  
from setuptools import setup
import os
package_dir = os.path.dirname(__file__)

README = open(package_dir + "README.md","r").read()
art ="""

██████╗░██╗░█████╗░██╗░░██╗░██████╗░█████╗░███╗░░██╗██╗░░░██╗██╗
██╔══██╗██║██╔══██╗██║░██╔╝██╔════╝██╔══██╗████╗░██║██║░░░██║██║
██║░░██║██║██║░░╚═╝█████═╝░╚█████╗░██║░░██║██╔██╗██║██║░░░██║██║
██║░░██║██║██║░░██╗██╔═██╗░░╚═══██╗██║░░██║██║╚████║██║░░░██║██║
██████╔╝██║╚█████╔╝██║░╚██╗██████╔╝╚█████╔╝██║░╚███║╚██████╔╝██║
╚═════╝░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚══╝░╚═════╝░╚═╝
"""
print(art)
setup(
    name="DicksonUI",
    version="1.1.1",
    description="Lightweight And Full Featured Browser Based UI / GUI (Graphical User Interface Library)",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Ksengine/DicksonUI",
    author="KavinduSanthusa",
    author_email="kavindusanthusa@rgmail.com",
    keywords="""python gui html css js javascript css3 html5 ui 
user-interface graphical-user-interface lightweight full-featured 
browser browser-based portable server chrome firefox edge""",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["dicksonui"],
    include_package_data=True,
)
