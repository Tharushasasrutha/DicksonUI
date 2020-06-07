#!/usr/bin/python
# -*- coding: utf-8 -*-

#
#  Control.py
#


class Control:

    def __init__(self, TagName):
        self._hosted = False  # Is added to Form
        self._script = ''  # Javascript code (Used before added to Form)
        self._id = ''  # Used By Form to identify control   Dont change
        self._script += 'var Control = document.createElement("' \
            + TagName + '");'
        self.events = {}
        self.Controls = []
        pass

    # Below function is only used by Form !

    def initialize(self, Id, parent):
        self._id = Id
        self.parent = parent
        self._hosted = True
        return self._script + 'Control.id = "' + self._id + '";'

    def child_handler(self):
        for Control in self.Controls:
            self.parent.Add(Control)
            self.send('appendChild(document.getElementById("'
                      + Control.Id + '"));')

    @property
    def Id(self, Id=None):
        if self.Id == None:
            self.Id = Id
        return self.Id

    @Id.getter
    def Id(self):
        return self._id

    def send(self, message, evaluate=False):
        """This will change script(Javascript) """

        if self._hosted == True:  # check if control is added to Form
            if evaluate:
                return self.parent.evaluate('document.getElementById("'
                        + self._id + '").' + message)
            else:
                self.parent.run('document.getElementById("' + self._id
                                + '").' + message)
        else:
            self._script += 'Control.'
            self._script += message

    def run(self, script):
        self.send(script)

    def evaluate(self, script):
        self.send(script, True)

    def innerHTML(self, html):
        """The innerHTML property sets or returns the HTML content (inner HTML) of an element."""

        self.send('innerHTML;', True)

    def innerHTML(self, html):
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

        self.events[str(event)] = function
        self.send('addEventListener("' + event + '", notify_server, '
                  + str(useCapture).lower() + ');')

    def fire_event(self, EventData):
        for event in self.events:
            if event == EventData['type']:
                f = self.events[event]
                f(self, EventData)

    def Width(self, w):
        self.send('width="' + str(w) + '";')

    def Height(self, h):
        self.send('height="' + str(h) + '";')

    def Size(self, w, h):
        self.Width(w)
        self.Height(h)

    def appendChild(self, node):
        if self._hosted:
            self.parent.Add(node)
            self.send('appendChild(document.getElementById("' + node.Id
                      + '"));')
        else:
            self.Controls.append(node)

    def style(self, prop, style):
        self.send('style.' + prop + '="' + style + '";')

    def classList(self):

        def add(self, classname):
            self.send('classList.add("' + classname + '");')
