# ezgfm

ezgfm is a simple extension of [SimpleHTTPServer] that renders GitHub-flavored
Markdown documents (`*.md`) as HTML.

[SimpleHTTPServer]: https://docs.python.org/2.7/library/simplehttpserver.html


## Prerequisites

ezgfm runs on Python 2.x and requires the following packages:

~~~~shell
$ pip install markdown py-gfm pygments
~~~~

Note: `pygments` is optional although recommended.


## Usage

It's basically the same as SimpleHTTPServer:

~~~~shell
$ python ezgfm.py [PORT]
~~~~

Then access http://localhost:8000/ (or the port of your choice) on your browser.

If you place `style.css` in the document root, ezgfm utilizes it.


## License

3-clause BSD License. See [LICENSE.md](LICENSE.md) for the full statement.
