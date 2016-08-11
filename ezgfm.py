import BaseHTTPServer
import cStringIO
import os
from SimpleHTTPServer import SimpleHTTPRequestHandler
import sys

import markdown
import mdx_partial_gfm


##------------------------
##  Settings

_HTML_TEMPLATE = '''
<!doctype html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1">
    <meta charset="{charset}">
    <title>{title}</title>
    <link rel="stylesheet" href="/style.css">
  </head>
  <body>
{body}
  </body>
</html>
'''

_CHARSET = 'utf-8'

_EXTENSIONS = [
    mdx_partial_gfm.PartialGithubFlavoredMarkdownExtension(),
]


##------------------------
##  Code

class EzgfmHandler(SimpleHTTPRequestHandler):
    def _render_markdown(self):
        path = self.translate_path(self.path)

        if path.endswith('.md'):
            pass
        elif path.endswith('/'):
            path = path + 'index.md'
        else:
            return None

        try:
            with open(path, 'r') as fp:
                source = fp.read()
                fs = os.fstat(fp.fileno())
        except IOError:
            return None

        output = markdown.markdown(source.decode(_CHARSET),
                                   extensions=_EXTENSIONS)
        html = _HTML_TEMPLATE.format(title=os.path.basename(path),
                                     charset=_CHARSET,
                                     body=output.encode(_CHARSET))
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=' + _CHARSET)
        self.send_header('Content-Length', len(html))
        self.send_header('Last-Modified', self.date_time_string(fs.st_mtime))
        self.end_headers()
        return cStringIO.StringIO(html)

    def send_head(self):
        markdown = self._render_markdown()
        if markdown:
            return markdown
        return SimpleHTTPRequestHandler.send_head(self)


if __name__ == '__main__':
    BaseHTTPServer.test(HandlerClass=EzgfmHandler)
