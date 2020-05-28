#!/usr/bin/python
# -*- coding: utf-8 -*-

#
#  Form.py
#

from .Control import Control
import json
import os
def read_json(request_headers, request_file):
  n_bytes = int(request_headers['content-length'])
  content_bytes = request_file.read(n_bytes)
  content_string = content_bytes.decode('ascii')
  return json.loads(content_string)


class document:

    def __init__(self):
        self.script = ''
        self._name = None
        self.eval_id = 0
        self.eval_list = {}
        
    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, name):
        self._name = name
  
    def body(self):
        self.run("document.body.innerHTML=\""+string+"\";")
    
    def getElementById(self, Id):
        
        return c        

    def EventHandler(self, s):
        data = read_json(s.headers, s.rfile)
        s.send_response(200)
        s.end_headers()
        for control in self.Controls:
            if control.Id == data['currentTarget']:
                control.fire_event(data)
                
    def RequestHandler(self, s):
        if s.command == "GET":
            if s.path.endswith("/command"):
                self.CommandHandler(s)
        if s.command == "POST":
            if s.path.endswith("/event"):
                self.EventHandler(s)
            if s.path.endswith("/data"):
                self.DataHandler(s)
    
    def evaluate(self, script):
        self.run("sd={};sd.data="+ script+"sd.target="+str(self.eval_id)+";notify_data(sd);")
        myid = self.eval_id
        self.eval_id += 1
        self.eval_list[myid] = ""
        while self.eval_list[myid] == "":
            pass
        else:
            rdata = self.eval_list[myid]
            del self.eval_list[myid]
            return rdata
                    
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
    
    def DataHandler(self,s):
        data = read_json(s.headers, s.rfile)
        s.send_response(200)
        s.end_headers()
        myid = int(data["target"])
        self.eval_list[myid] = data["data"]



