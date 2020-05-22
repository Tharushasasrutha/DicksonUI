#!/usr/bin/python
# -*- coding: utf-8 -*-

#
#  Controls.py
#

from .Control import *


class Text(Control):

    """Control class wrapper for Text Controls"""

    def __init__(self, Type):
        super().__init__(Type)

    def Text(self, html):
        self.send('innerHTML="' + html.replace('\n', '<br>'
                  ).replace('\r', '') + '";')


class Heading(Text):

    """Control for Headings"""

    def __init__(self, Size):
        super().__init__('h' + str(Size))


 # Heading Sizes

class h1(Heading):

    def __init__(self):
        super().__init__(1)


class h2(Heading):

    def __init__(self):
        super().__init__(2)


class h3(Heading):

    def __init__(self):
        super().__init__(3)


class h4(Heading):

    def __init__(self):
        super().__init__(4)


class h5(Heading):

    def __init__(self):
        super().__init__(5)


class h6(Heading):

    def __init__(self):
        super().__init__(6)


class Paragraph(Text):

    """Control for Pharagraphs"""

    def __init__(self):
        super().__init__('p')


class p(Paragraph):

    """Paragraph class wrapper"""


class Anchor(Text):

    """Anchor Element"""

    def __init__(self):
        super().__init__('a')

    def href(self, link):
        """The link's destination is specified in the href"""

        self.send('href="' + link + '";')


class a(Anchor):

    """class for a tag"""


class Link(Anchor):

    """class for Link Cont"""
