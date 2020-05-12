#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  server.py
#  

from utiles import *
import os
try:
    from http.server import HTTPServer, BaseHTTPRequestHandler
    from socketserver import ThreadingMixIn
except ImportError:
    from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
    from SocketServer import ThreadingMixIn
    
import threading

package_directory = os.path.dirname(os.path.abspath(__file__))#get package directory for get relative path
PORT = None#localhost port for server
EVENT_POSTED = None#event manager of form class
CMD_HANDLER = None#scripr(Javascript)/command manager of form class
ICON = None#icon(favicon.ico) of Form

def read_json(request_headers, request_file):
    """json(event object) to dict"""
    n_bytes = int(request_headers['content-length'])
    content_bytes = request_file.read(n_bytes)
    content_string = content_bytes.decode('ascii')
    return json.loads(content_string)


class RequestHandler(BaseHTTPRequestHandler):
    """Handler for client requests."""
    def do_GET(self):
        """handle GET requests"""
        if self.path == "/":
            self.send_headers()
            path = os.path.join(package_directory, "index.html")
            self.wfile.write(bytes(open(path).read(), "utf-8"))
        elif self.path == "/favicon.ico":
            self.send_headers()
            try:#handle if icon is None
                self.wfile.write(ICON)
            except:
                print("No Icon")
        elif self.path == "/script.js":# requested a bit of javascript to run
            self.send_headers()
            self.wfile.write(bytes(CMD_HANDLER.script(), "utf-8"))
        elif self.path == "/DicksonUI.js":
            self.send_headers()
            path = os.path.join(package_directory, "DicksonUI.js")
            self.wfile.write(bytes(open(path).read(), "utf-8"))
        elif self.path == "/command":# requested a command
            try:
                self.send_headers()
                msg = CMD_HANDLER.fire()
                self.wfile.write(bytes(msg, "utf-8"))
                CMD_HANDLER.end()
            except socket.error:
                # The client stopped listening while we were waiting.
                pass
        else:
            self.send_response(404)# 404 = (status code) NOT_FOUND
            self.end_headers()
            
    def do_POST(self):
        """handle POST requests for get if event fired"""
        if self.path == "/event":
            self.post_event()
        
    def send_headers(self):
        self.send_response(200) # 200 = (status code) OK
        """Add headers to the response telling the client to not cache anything."""
        # Source: http://stackoverflow.com/questions/49547/making-sure-a-web-page-is-not-cached-across-all-browsers
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.end_headers()
        
    def post_event(self):
        self.send_response(200)
        self.end_headers()
        data = read_json(self.headers, self.rfile)
        EVENT_POSTED(data)#fire event handlers through event manager

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Server that responds to each request in a separate thread."""
    pass

class server():
    def __init__(self, event_manager, command_manager, icon):
        EVENT_POSTED = event_manager
        CMD_HANDLER = command_manager
        ICON = icon
        pass
    def start(self):
        """ Create a web server and define the handler to manage the incoming request"""
        PORT = find_free_port()# utiles.find_free_port
        print("server is sterted at http://localhost:" + str(PORT))
        self.server = ThreadedHTTPServer(('localhost', PORT), RequestHandler)
        self.sth = threading.Thread(target=self.serve_forever)
        self.sth.daemon = False
        self.sth.start()
    def serve_forever(self):
        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            pass
    def stop(self):
        self.server.shutdown()
        self.server.socket.close()
        self.server = None
