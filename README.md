<img src="https://i.ibb.co/5WjRjr1/logo.png" width="250">
<a href="https://teknowafel.github.io/statyc-py/">Demo Site</a>

## What is statyc-py?
statyc-py is a simple static site generator written in python, which generates a clean, minimalistic blog style website with seamless support for mobile and desktop devices alike.

## Why go statyc?
Unlike dynamically rendered websites which rely on the server to generate their html on the fly, static sites are prerendered to simple HTML files beforehand with a generator such as this one. Static sites are generally much faster than dynamic websites, with popular options being Hugo and Jekyll. These site generators are great, but statyc-py makes fast performance and ease of use, and easy customization its top priorities. Here's how:
1. Fewer external dependencies => requests => trackers
2. Simple, fast, and polished CSS and JS
3. An easy-to-use writing process to up your workflow
4. Meticulous attention to detail and daily tweaks/updates for the best experience

## How does statyc-py work?
statyc-py uses two simple sources for the information used to build the site.
1. statyc_settings.py
2. .md files from /in/posts  
Simply put, render.py gets information from settings such as the site title, subtitle, and author along with each post. After this, it parses your blog posts using [python-markdown2](https://github.com/trentm/python-markdown2) and wraps it all together in a somewhat readable HTML burrito.

## How do I install statyc-py?
statyc-py has been tested to work with python 3.8.3. Simply fork, clone, or download this repository to get started. Then, you can run `pip install -r requirements.txt` to install needed dependencies. 

## Quick Start Guide
Follow the directions in `statyc_settings.py` to set up things like your base URL, and you're almost done. You can make a new `.md` file inside of `/in/posts` to create a new post. To make sure that statyc-py properly reads the post, you can follow these guidelines, or use one of the default posts as a reference.
1. The name of the file should be a short version of the post title, with dashes (-) instead of spaces, and no capitalization.
2. The first line in the file should be the title of the post in plain text (capitalization allowed).
3. The second line of the file should be the name of the author.
4. The third line of the file should be the date, in whatever format you like (I recommend you keep date formatting consistent across posts for, you know, consistency).
5. Following lines of the file will be parsed as the contents of the blog post. Keep in mind that you can add a line break in the file after the date, and formatting will stay the same. This is because markdown only renders line breaks if you add two trailing spaces to a the line.
6. Congratulations! You're pretty much done. All you have to do now is run `render.py`, and the site will magically(disclaimer:no magic involved) be rendered to /docs/.

## Roadmap
Don't forget to checkout roadmap.md, or click [here](https://github.com/teknowafel/statyc-py/blob/master/roadmap.md) to learn more about the past, present, and future of statyc-py.  
