import sys, subprocess as sps, os
import threading

"""Google Chrome/Chromium"""
def run(url, options = []):
    chrome_path  = find_path()
    options.append('--new-window')
    sps.run([chrome_path, '--app=%s' % url] +
               options ,
               stdout=sps.PIPE, stderr=sps.PIPE, stdin=sps.PIPE)

def find_path():
    if sys.platform in ['win32', 'win64']:
        return _find_chrome_win()
    elif sys.platform == 'darwin':
        return _find_chrome_mac() or _find_chromium_mac()
    elif sys.platform.startswith('linux'):
        return _find_chrome_linux()
    else:
        return None


def _find_chrome_mac():
    chrome_paths = ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                    "/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary",
                    "/Applications/Chromium.app/Contents/MacOS/Chromium",
                    "/usr/bin/google-chrome-stable",
                    "/usr/bin/google-chrome",
                    "/usr/bin/chromium",
                    "/usr/bin/chromium-browser"]

    for path in chrome_paths:
        if os.path.exists(path):
            return path
    return None

def _find_chrome_linux():
    chrome_paths = ["/usr/bin/google-chrome-stable",
                    "/usr/bin/google-chrome",
                    "/usr/bin/chromium",
                    "/usr/bin/chromium-browser",
                    "/snap/bin/chromium"]

    for path in chrome_paths:
        if os.path.exists(path):
            return path
    return None


def _find_chrome_win():
    import winreg as reg
    reg_path = r'SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe'

    for install_type in reg.HKEY_CURRENT_USER, reg.HKEY_LOCAL_MACHINE:
        try:
            reg_key = reg.OpenKey(install_type, reg_path, 0, reg.KEY_READ)
            chrome_path = reg.QueryValue(reg_key, None)
            reg_key.Close()
            if not os.path.isfile(chrome_path):
                continue
        except WindowsError:
            chrome_path = None
        else:
            break

    return chrome_path

run("about:blank")
