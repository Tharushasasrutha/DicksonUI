#!/usr/bin/python
# -*- coding: utf-8 -*-

#
#  utiles.py
#
#  Copyright 2020  <Kavindu Santhusa>
#

import socket


def find_free_port(port, max_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while port <= max_port:
        try:
            sock.bind(('', port))
            sock.close()
            return port
        except OSError:
            port += 1
    raise IOError('no free ports')
