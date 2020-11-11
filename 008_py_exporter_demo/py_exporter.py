import prometheus_client
from prometheus_client import Gauge, start_http_server, Counter
import pycurl
import time
import threading
from io import BytesIO

url_http_code = Counter('url_http_code', 'request http_code of the host',
                        ['code', 'url'])
url_http_request_time = Counter('url_http_request_time',
                                'request http_request_time of the host',
                                ['le', 'url'])
http_request_total = Counter('http_request_total',
                             'request request total of the host', ['url'])


def test_website(url):
    buffer_curl = BytesIO()
    c = pycurl.Curl()


# https://github.com/prometheus/client_python