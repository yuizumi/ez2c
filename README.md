# ez2c

ez2c (_easy to see_) is a simple extension of `SimpleHTTPServer` that renders
Markdown documents (`*.md`) as HTML.


## Prerequisites

~~~~shell
$ pip install markdown py-gfm pygments
~~~~

Note: `pygments` is recommended but optional.


## Usage

~~~~shell
$ python -m ez2c
~~~~

Then access http://localhost:8000/ (or the port number of your choice).


## License

3-clause BSD License. See [LICENSE.md](LICENSE.md) for the full statement.
