# What it is
Server-side code to store a list of my favorite movies, 
including box art imagery and a movie trailer URL. With python code
to generate a static web page allowing visitors to browse throw
my movies and watch trailers.

## Table of Contents
- [What it is](https://github.com/nicholasinatel/Udacity/blob/master/Projects/01-Movie-Website/README.md/#what-it-is)
- [QuickStart](https://github.com/nicholasinatel/Udacity/blob/master/Projects/01-Movie-Website/README.md/#quickstart)
- [How to execute](https://github.com/nicholasinatel/Udacity/blob/master/Projects/01-Movie-Website/README.md/#how-to-execute)
- [Configuration](https://github.com/nicholasinatel/Udacity/blob/master/Projects/01-Movie-Website/README.md/#configuration)
- [Advanced](https://github.com/nicholasinatel/Udacity/blob/master/Projects/01-Movie-Website/README.md/#advanced)
- [How it works](https://github.com/nicholasinatel/Udacity/blob/master/Projects/01-Movie-Website/README.md/#how-it-works)
- [Known Bugs](https://github.com/nicholasinatel/Udacity/blob/master/Projects/01-Movie-Website/README.md/#knownbugs)
- [Objective](https://github.com/nicholasinatel/Udacity/blob/master/Projects/01-Movie-Website/README.md/#objective)
- [Details](https://github.com/nicholasinatel/Udacity/blob/master/Projects/01-Movie-Website/README.md/#details)
- [License](https://github.com/nicholasinatel/Udacity/blob/master/Projects/01-Movie-Website/README.md/#license)

## QuickStart
Install - Only in Windows
- [Python 2.7.15](https://www.python.org/downloads/release/python-2715/)

## How to execute: 

Go to project Folder, Open Terminal, Type:
```
    python entertainment_center.py
```
Web Browser With Static HTML page should open.

## Configuration
The ```entertainment_center.py``` file, comes configured with 12 different instances that represent 12 distinct movies. You can add/remove instances and execute the code, it still will generate the proper HTML file as long as the syntax is strictly followed.
```
movie_example = media.Movie("Movie Title",
                        "URL to Online Image",
                        "URL to youtube trailer")
```

## Advanced
The Class and Method utilized, are declared at ```media.py```, and it is proper documented in the comment section following [PEP-8 site](https://www.python.org/dev/peps/pep-0008/) best practices.

## How it works
Once you execute the code, the ```entertainment_center.py``` file creates the instances by calling the constructor inside the **Movie Class** in the ```media.py``` file. When all instances gets created, the code generates a list and passes it to the ```fresh_tomatoes.py``` file, that renders the object attributes within the static HTML content creating the webpage.

## Known Bugs
I have not tested on MAC OS or LINUX, it should work though.

## Objective
- Learn how to write an application using OOP - Object Oriented Python.
- Learn how to make this application serve HTML via web browser.
- Estabilish a foundation in core programmin concepts using Python.
- Understand the role a simple web server has in receiving a request, executing a block of code and generating a response.

## Details
Creata Data Structure to Store favorite movies

- Movite Title
- box art URL || poster URL
- Movie Trailer URL

Create Multiple Instance of Movies in Python in a List

Use fresh_tomatoes.py
- fork the repository
- create own copy in github
- clone to work on the project locally
- open_movies_page
- Ensure the website renders correctly in a web browser
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
