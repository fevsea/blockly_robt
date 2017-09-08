from http.server import BaseHTTPRequestHandler
import urllib.parse as urlparse

from task import ExecutionManager

# HTTPRequestHandler class
class baseServer(BaseHTTPRequestHandler):
    task = ExecutionManager()

    # GET
    def do_GET(self):
        parsed_url = urlparse.urlsplit(self.path)
        print("Path: " + self.path)
        arguments = dict(urlparse.parse_qs(parsed_url.query))
        code = arguments.get('code', ["No code"])[0]
        #print(arguments)
        message = self.task.runF(code)

        # Send response status code
        self.send_response(200)
        # Send headers
        self.send_header('Content-type','text/plain')
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return
