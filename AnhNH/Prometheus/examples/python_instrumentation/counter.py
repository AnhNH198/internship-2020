import http.server
from prometheus_client import start_http_server, Counter
import random

APP_PORT = 8000
METRICS_PORT = 8003
REQUEST_COUNT = Counter('app_requests_count', 'count total request to web')
RANDOM_COUNT = Counter('random_request_count', 'increase random value when have new request')

class HandleRequests(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        REQUEST_COUNT.inc()
        # Increase 1 value each GET request
        random_value = random.random()+10
        RANDOM_COUNT.inc(random_value)
        # Increase random value each GET request
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>First Application</title></head><body style='color: #333; margin-top: 30px;'><center><h2>Welcome to our first Prometheus-Python application.</center></h2></body></html>", "utf-8"))
        self.wfile.close()

if __name__ == "__main__":
    start_http_server(METRICS_PORT)
    server = http.server.HTTPServer(('103.56.156.20', APP_PORT), HandleRequests)
    server.serve_forever() 