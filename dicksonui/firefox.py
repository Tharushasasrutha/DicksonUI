#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess as sps
import sys
import os
name = 'Firefox'


class firefox:

    def __init__(self):
        pass

    def run(
        self,
        path,
        options,
        url,
        new_instance=False,
        width=None,
        height=None,
        ):
        cmd = path
        if new_instance:
            cmd += ' --new-instance'
        cmd += ' --profile ' + self.app_mode()
        if width:
            if height:
                cmd += ' --window-size ' + width + ',' + height
            else:
                cmd += ' --window-size ' + width
        for option in options:
            cmd += ' '
            cmd += option
        cmd += ' --private-window '
        cmd += url
        os.popen(cmd)

    def version(self, path):
        v = os.popen(path + ' -v').read()[16:-4]
        return int(v[:2])

    def app_mode(self):
        css = \
            """#TabsToolbar {visibility: collapse !important;}
    #sidebar-header {display: none;}
    #titlebar {display: none !important;}
    #titlebar-buttonbox-container {display: none !important;}
    #main-window {-moz-appearance: none !important;}
    #navigator-toolbox {visibility: collapse;}"""
        user = \
            """user_pref(\"toolkit.legacyUserProfileCustomizations.stylesheets\", true);"""
        """user_pref(\"browser.tabs.drawInTitlebar\", true);"""
        cwd = os.getcwd()
        if sys.platform in ['win32', 'win64']:
            try:
                os.mkdir(cwd + '\\userdata')
            except:
                pass
            try:
                os.mkdir(cwd + '\\userdata\\chrome')
            except:
                pass
            try:
                open(cwd + '\\userdata\\chrome\\userChrome.css', 'x')
            except:
                pass
            try:
                open(cwd + '\\userdata\\chrome\\userChrome.css', 'w'
                     ).write(css)
            except Exception as e:
                print(e)
            try:
                open(cwd + '\\userdata\\user.js', 'x')
            except:
                pass
            try:
                open(cwd + '\\userdata\\user.js', 'w').write(user)
                return cwd + '\\userdata'
            except Exception as e:
                print(e)
        else:
            try:
                os.mkdir(cwd + '/userdata')
            except:
                pass
            try:
                os.mkdir(cwd + '/userdata/chrome')
            except:
                pass
            try:
                open(cwd + '/userdata/chrome/userChrome.css', 'x')
            except:
                pass
            try:
                open(cwd + '/userdata/chrome/userChrome.css', 'w'
                     ).write(css)
            except Exception as e:
                print(e)
            try:
                open(cwd + '/userdata/user.js', 'x')
            except:
                pass
            try:
                open(cwd + '/userdata/user.js', 'w').write(user)
                return cwd + '/userdata'
            except Exception as e:
                print(e)

    def find_path(self):
        if sys.platform in ['win32', 'win64']:
            return self._find_firefox_win()
        elif sys.platform == 'darwin':
            return self._find_firefox_mac_linux()
        elif sys.platform.startswith('linux'):
            return self._find_firefox_mac_linux()
        else:
            return None

    def _find_firefox_mac_linux(self):
        for browser in (
            'firefox',
            'firefox-esr',
            'iceweasel',
            'iceape',
            'seamonkey',
            'mozilla-firefox',
            'mozilla-firebird',
            'firebird',
            'mozilla',
            ):
            a = os.popen('which ' + browser).read()
            if a == '':
                pass
            else:
                return a[:-1]
        return None

    def _find_firefox_win(self):
        for browser in (
            'firefox',
            'firefox-esr',
            'iceweasel',
            'iceape',
            'seamonkey',
            'mozilla-firefox',
            'mozilla-firebird',
            'firebird',
            'mozilla',
            ):
            a = os.popen('where ' + browser).read()
            if a == '':
                pass
            else:
                return a[:-1]
        return None
