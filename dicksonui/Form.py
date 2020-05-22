#!/usr/bin/python
# -*- coding: utf-8 -*-

#
#  Form.py
#


import time
import os
def read_json(request_headers, request_file):
  n_bytes = int(request_headers['content-length'])
  content_bytes = request_file.read(n_bytes)
  content_string = content_bytes.decode('ascii')
  return json.loads(content_string)
  


class Form:

    def __init__(self):
        self.script = ''
        self.control_counter = 0
        self.Controls = []
        self._name = None
        
    @property
    def Name(self):
        return self._name
        
    @Name.setter
    def Name(self, Name):
        self._name = Name

    def Add(self, control):
        a = control.initialize(str(self.control_counter), self.run)
        self.run(a + 'document.body.appendChild(Control);')
        self.Controls.append(control)
        self.control_counter += 1

    def EventHandler(self, s):
        data = read_json(self.headers, self.rfile)
        s.send_response(200)
        s.end_headers()
        for control in self.Controls:
            if control.Id == data['currentTarget']:
                control.fire_event(data)
                
    def RequestHandler(self, s):
        print("rhandler")
        if s.command == "GET":
            print("rhandler.get")
            if s.path.endswith("/command"):
                print("command")
                self.CommandHandler(s)
                
    def run(self, script):
        self.script += script

    def CommandHandler(self, s):
        try:
            while self.script == '':
                pass
            else:
                s.send_response(200)
                s.send_no_cache_headers()
                s.end_headers()
                s.wfile.write(bytes(self.script + "obey_forever();", "utf-8"))
                self.script = ''
        except:
              # The client stopped listening while we were waiting.
              pass

