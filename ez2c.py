import SimpleHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import sys

import markdown
import mdx_partial_gfm


##------------------------
##  Settings

_DEFAULT_PORT = 8000

_HTML_TEMPLATE = '''
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>{title}</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
{body}
  </body>
</html>
'''

_EXTENSIONS = [
    mdx_partial_gfm.PartialGithubFlavoredMarkdownExtension(),
]


##------------------------
##  Code

class Ez2cHandler(SimpleHTTPRequestHandler):
    def _serve_markdown(self):
        if not self.path.endswith('.md'):
            return False

        try:
            with open('.' + self.path, 'r') as fp:
                source = fp.read()
        except IOError:
            return False

        rendered = markdown.markdown(source, extensions=_EXTENSIONS)
        html = _HTML_TEMPLATE.format(title=self.path, body=rendered)
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.wfile.write(html)

        return True

    def do_GET(self):
        self._serve_markdown() or SimpleHTTPRequestHandler.do_GET(self)


if __name__ == '__main__':
    SimpleHTTPServer.test(HandlerClass=Ez2cHandler)
