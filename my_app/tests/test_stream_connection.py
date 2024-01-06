import unittest
from my_app.connections.streaming_api import establish_stream_connection
from flask import Flask

class TestEstablishStreamConnection(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config.from_object('my_app.Config')

    def test_establish_stream_connection(self):
        with self.app.test_request_context('/test-stream-connection'):
            establish_stream_connection(self.app)

if __name__ == '__main__':
    unittest.main()
