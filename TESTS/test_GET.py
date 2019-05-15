import unittest
from PROJECT import record_func


class TestGET(unittest.TestCase):

    def test_get(self):
        uuid = "c2bd3384-5a66-4a28-a8bf-9eda7ca26583"
        result = record_func.record_uuid_get(uuid)
        self.assertEqual(result,
            '{\"recordId\": \"c2bd3384-5a66-4a28-a8bf-9eda7ca26583\", '
            '\"info\": {\"recordStatus\": \"NEW\", '
            '\"created\": \"2019-05-14T19:52:37.715824+02:00\", '
            '\"updated\": \"\", '
            '\"deleted\": \"\", '
            '\"recordData\": \"\"}}')

if __name__ == '__main__':
    unittest.main()
