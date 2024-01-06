import unittest
from my_app.listeners.post_stream_listener import PostStreamListener  # Replace 'your_module' with the actual module name
import io
from contextlib import redirect_stdout

class TestPostStreamListener(unittest.TestCase):

    def setUp(self):
        self.listener = PostStreamListener()

    def test_on_update(self):
        status_update1 = {
            "id": 1,
            "text": "This is the first status update.",
            "user": {
                "id": 123,
                "username": "user123"
            }
        }

        with io.StringIO() as buffer, redirect_stdout(buffer):
            self.listener.on_update(status_update1)
            output = buffer.getvalue()

        expected_output = "Received a new post:  {'id': 1, 'text': 'This is the first status update.', 'user': {'id': 123, 'username': 'user123'}}\n"
        self.assertEqual(output, expected_output)

    def test_on_status_update(self):
        status_update2 = {
            "id": 2,
            "text": "This is the second status update.",
            "user": {
                "id": 456,
                "username": "user456"
            }
        }

        with io.StringIO() as buffer, redirect_stdout(buffer):
            self.listener.on_status_update(status_update2)
            output = buffer.getvalue()

        # Assert that the expected output was printed
        expected_output = "Received a new update:  {'id': 2, 'text': 'This is the second status update.', 'user': {'id': 456, 'username': 'user456'}}\n"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
