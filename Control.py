#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Control.py
#  

class Control():
    
    def __init__(self):
        self.script_manager = None
        self._hosted = False # Is added to Form
        self._script = "" #Javascript code (Used before added to Form)
        self.TagName = "" # Tagname of COntrol = Control type
        self.Id = "" #Used By Form to identify control   Dont change 
        self._script += "var Control = document.createElement(\""+self.TagName+"\");" 
        self.events = []
        self.event_handlers = []
        pass
    
    #Below function is only used by Form !
    def initialize(self, script_manager):
        self.script_manager = script_manager
        return self._script
    
    @property
    def id(self):
        return self.Id
        
    def send(self, message):
        """This will change script(Javascript) """
        if self._hosted == True:#check if control is added to Form
             self.script_manager.run("document.getElementById(\""+self.Id+"\")."+message)
        else:
            self._script += "Control."
            self._script += message
        
    @property
    def innerHTML(self, Html):
        """The innerHTML property sets or returns the HTML content (inner HTML) of an element."""
        if Html == None: # TODO: should return  
            pass
        else:
            self.send("innerHTML=\""+HTML+"\";")
    
    @classmethod    
    def setAttribute(self, attributename, attributevalue):
        """The setAttribute() method adds the specified attribute to an element,
        and gives it the specified value."""
        self.send("setAttribute(\""+attributename+"\", \""+attributevalue+"\");")
        
    @classmethod
    def addEventListener(self, event, function, useCapture):
        """The addEventListener() method attaches an event handler to the specified element."""
        self.events.append(str(event))
        self.event_handlers.append(function)
        self.send("addEventListener(\""+event+"\", notify_server, "+ str(useCapture)+");")
        
        
    
