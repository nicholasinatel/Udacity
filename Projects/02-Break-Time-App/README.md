# What it is
Developed code in Python for opening webbrowser with given URL after asserted time.

## Table of Contents
- What it is
- QuickStart
- How to execute
- Configuration
- Libraries
- How it works
- Known Bugs
- Suggested Future Work
- License

## QuickStart
Windows Install
- [Python 2.7.15](https://www.python.org/downloads/release/python-2715/)

### How to execute: 

Go to project Folder, Open Terminal, Type:
```
    python break_time.py
```
1. Enter with desired URL:
2. Print URL and open webbroser with typed url.

## Configuration
- Number of breaks at the variable ```total_breaks``` . 

- Assert time in the ```timer``` variable.

## Libraries
- [webbrowser](https://docs.python.org/2/library/webbrowser.html) 
- [time](https://docs.python.org/2/library/time.html)

## How it works
Once you execute the code, enter a Youtube URL from a video you like.
The code will open a webbrowser with the video and play for you to remember to stop working.

## Known Bugs
I have not tested on MAC OS or LINUX, it should work though.

## Suggested Future Work
Discover and implement a way to freeze the screen so the user really have to stop working and only unfreeze at a certain amount of time.

## License
MIT License

Copyright (c) [2018] [Nicholas Lobo]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
