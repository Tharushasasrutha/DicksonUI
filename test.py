#!/usr/bin/python
# -*- coding: utf-8 -*-
from dicksonui import Application, Form, Controls
import webbrowser

label = Controls.h1()
label.Text = """Hi
Then"""
Myform = Form()
App = Application()
App.Add(Myform)
Myform.Add(label)
print("Navigate To - "+App.location)
webbrowser.open(App.location)
