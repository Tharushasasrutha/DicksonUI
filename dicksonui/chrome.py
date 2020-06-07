#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os

name = 'Google Chrome/Chromium'


class chrome:

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
        for option in options:
            cmd += ' '
            cmd += option
        cmd += ' --incognito'
        cmd += ' --new-window'
        cmd += ' --app='
        cmd += url
        os.popen(cmd)

    def version(self, path):
        try:
            v = os.popen(find_path() + ' --version').read()
            v2 = v[v.find(' ') + 1:]
            return int(v2[:v2.find('.')])
        except:
            return None

    def is_chromium(self, path):
        try:
            if os.popen(path + ' --version'
                        ).read().startswith('Chromium'):
                return True
            else:
                return False
        except:
            return None

    def find_path(self):
        if sys.platform in ['win32', 'win64']:
            return self._find_chrome_win()
        elif sys.platform == 'darwin':
            return self._find_chrome_mac()
        elif sys.platform.startswith('linux'):
            return self._find_chrome_linux()
        else:
            return None

    def _find_chrome_mac(self):
        paths = [
            '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
                ,
            '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
                ,
            '/Applications/Chromium.app/Contents/MacOS/Chromium',
            '/usr/bin/google-chrome-stable',
            '/usr/bin/google-chrome',
            '/usr/bin/chromium',
            '/usr/bin/chromium-browser',
            ]
        chrome_path = None
        for path in paths:
            if os.path.exists(path):
                chrome_path = path
        if chrome_path != None:
            return chrome_path
        else:
            for browser in ('google-chrome', 'chrome', 'chromium',
                            'chromium-browser'):
                a = os.popen('which ' + browser).read()
                if a == '':
                    pass
                else:
                    return a[:-1]
            return None

    def _find_chrome_linux(self):
        paths = ['/usr/bin/google-chrome-stable',
                 '/usr/bin/google-chrome', '/usr/bin/chromium',
                 '/usr/bin/chromium-browser', '/snap/bin/chromium']
        chrome_path = None
        for path in paths:
            if os.path.exists(path):
                chrome_path = path
        if chrome_path != None:
            return chrome_path
        else:
            for browser in ('google-chrome', 'chrome', 'chromium',
                            'chromium-browser'):
                a = os.popen('which ' + browser).read()
                if a == '':
                    pass
                else:
                    return a[:-1]
            return None

    def _find_chrome_win(self):
        import winreg as reg
        reg_path = \
            r'SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe'

        for install_type in (reg.HKEY_CURRENT_USER,
                             reg.HKEY_LOCAL_MACHINE):
            try:
                reg_key = reg.OpenKey(install_type, reg_path, 0,
                        reg.KEY_READ)
                chrome_path = reg.QueryValue(reg_key, None)
                reg_key.Close()
                if not os.path.isfile(chrome_path):
                    continue
            except WindowsError:
                chrome_path = None
            else:
                break
        for browser in ('google-chrome', 'chrome', 'chromium',
                        'chromium-browser'):
            a = os.popen('where ' + browser).read()
            if a == '':
                pass
            else:
                chrome_path = a[:-1]
        return chrome_path
