#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Form.py
#  

from server import server

class Form():
    def __init__(self):
        server(self.EventManager, self.ScriptManager, None).start()
        
    def EventManager(self, EventData):
        for x in cars:
            print (x)
            for y in cars[x]:
                print (y,':',cars[x][y])
                
    def ScriptManager(self):pass

Form()
