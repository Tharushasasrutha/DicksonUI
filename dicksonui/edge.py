#!/usr/bin/python
# -*- coding: utf-8 -*-
import os as sps

name = 'Edge'


class edge:

    def __init__(self):
        pass

    def run(
        self,
        _path,
        options,
        url,
        ):
        cmd = 'start microsoft-edge:{}'.format(url)
        sps.Popen(cmd)
