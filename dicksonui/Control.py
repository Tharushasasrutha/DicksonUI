#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#  Control.py
#


class Control:

    def __init__(self, TagName):
        self.script_manager = None
        self._hosted = False  # Is added to Form
        self._script = ''  # Javascript code (Used before added to Form)
        self.TagName = TagName  # Tagname of Control = Control type
        self.Id = ''  # Used By Form to identify control   Dont change
        self._script += 'var Control = document.createElement("' \
            + self.TagName + '");'
        self.events = []
        self.event_handlers = []
        pass

    # Below function is only used by Form !

    def initialize(self, Id, script_manager):
        self.Id = Id
        self.script_manager = script_manager
        self._hosted = True
        return self._script + 'Control.id = "' + self.Id + '";'

    def Id(self, Id=None):
        if self.Id == None:
            self.Id = Id
        return self.Id

    def send(self, message):
        """This will change script(Javascript) """

        if self._hosted == True:  # check if control is added to Form
            self.script_manager('document.getElementById("' + self.Id
                                + '").' + message)
        else:
            self._script += 'Control.'
            self._script += message

    def innerHTML(self, html):
        """The innerHTML property sets or returns the HTML content (inner HTML) of an element."""

        if html == None:  # TODO: should return
            pass
        else:
            self.send('innerHTML="' + html + '";')

    def setAttribute(self, attributename, attributevalue):
        """The setAttribute() method adds the specified attribute to an element,
        and gives it the specified value."""

        self.send('setAttribute("' + attributename + '", "'
                  + attributevalue + '");')

    def addEventListener(
        self,
        event,
        function,
        useCapture=False,
        ):
        """The addEventListener() method attaches an event handler to the specified element."""

        self.events.append(str(event))
        self.event_handlers.append(function)
        self.send('addEventListener("' + event + '", notify_server, '
                  + str(useCapture).lower() + ');')

    def fire_event(self, EventData):
        i = 0


        # for event in self.events:
        #    if event == EventType:
        #        self.event_handlers[i](EventData)
        #    i += 1
