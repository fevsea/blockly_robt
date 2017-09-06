from http.server import HTTPServer
import time, threading

from server import baseServer


print('starting server...')
# Server settings
server_address = ('127.0.0.1', 8081)
httpd = HTTPServer(server_address, baseServer)
print('running server...')
thread = threading.Thread(target = httpd.serve_forever)
try:
    thread.start()
except KeyboardInterrupt:
    print("Bye")
    httpd.shutdown()
    sys.exit(0)
