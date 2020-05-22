#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Controls.py
#  
from Control import *

class Heading(Control):
    def __init__(self, Size):
        super(self, "h" + str(Size))
        
class h1(Heading):
    def __init__(self):
        super(self, 1)
        
