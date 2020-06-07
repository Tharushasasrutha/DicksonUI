# DicksonUI - The Best GUI Library For Python

With DicksonUI, you can make Graphical User Interfaces with python with just few lines of code. DicksonUI is super easy to use and handles everything for you. Just write your code easily
or import any HTML code.

## Overview
The DicksonUI Python GUI Library was written with lightweight use in mind. It provides the following key features
- lightweight
- Cross-Platform(Windows, Linux, Mac)
- No Runtime Installer(Runtime is Browser)
- Low Ram Usage(less on your script, all used by browser)
- full featured(All features of html,css,js)
- browser based(Any device has s browser installed)
- powerful(power of bootstrap/AngularJS/React Coming Soon)
- Extensible(write your own plugin and share)
- HTML support - not just web pages - with js, css or any library(eg :-bootstap).
- The most common Controls  (Text, Links, Paragraphs or Headings(6 sizes)) are already implemented
- Events - with wide range of event data(all event is handling in own thread so no errors)

## Usage

In the following paragraphs, I am going to describe how you can get and use DicksonUI for your own projects.

###  Getting it
To download dicksonui, either fork this Github repo or simply use Pypi via pip.
DicksonUI is available on python 2 and 3 both. Dosen"t require Additional dependencies
```sh
$ pip install dicksonui
```
If you use easy_install,  `easy_install browsergui`.
If you don't like package managers, just download from Github and unzip   and put the  `browsergui`  folder anywhere on your Python path.

## Initialize a Window
First, let's create a new Application. 

```Python
from dicksonui import Form, Application
Myform = Form()
App = Aplication()
App.Add(Myform)
print(App.location)
```

#### Run!!! 
Run your code.
For Python 3
```sh
python3 myscript.py
```
Or, For Python 2
```sh
python myscript.py
```
This will print a link
`http://localhost:<port>`
 
Run your favorite browser
```sh
chromium-browser
```
And then navigate to above link.
😥😥😥 Nothing!!!but a blank page.

#### Add items to form 
Okay, now that we will learn about Controls

```Python
from dicksonui import Form, Application, Controls
MyHeading = Controls.heading(1)
Heading.innerHTML = """Hello world!
bye!"""
Myform = Form()
Myform.Add(MyHeading)
App = Aplication()
App.Add(Myform)
print(App.location)
```
Run it 
View wiki for more info

## alternatives?

-[RemI](https://github.com/dddomodossola/remi), which has exactly the same idea (build a GUI in Python, run it in a browser). Definitely worth a look.It is little heavy an use websockets. So it cannot run on older browsers. Instead we use Ajax long polling which is used by facebook.

-[tkinter](https://docs.python.org/3/library/tkinter.html#module-tkinter)  (standard library)

Advantages: it's well-known. Lots of people have written tutorials and documentation for it.

Disadvantages: it feels like a wrapper around Tk, because it is. This gives good performance and detailed control, but writing it feels unintuitive (to me). Also, I've had trouble getting it to work with multiple Python installations.
it isnt based on browsers and have limited features.

-[flexx](https://github.com/zoofIO/flexx) is very large and had more dependencies, it use tornado server. but we use our own few lines.limited features! and you can easily mix server-side and client-side

-eel is an alternative for Electron but it is based on bottle server. and it is not a pythonic way.

##Ok until next time, Bye! 
