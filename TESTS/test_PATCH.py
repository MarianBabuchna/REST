import unittest
from PROJECT import record_func


class TestPATCH(unittest.TestCase):

    def test_patch(self):
        uuid = "b2bd3384-5a66-4a28-a8bf-9eda7ca26583"
        record_func.record_uuid_patch(uuid)
        result = record_func.record_uuid_get(uuid)
        result_updated_part = result.split("created")
        self.assertRaisesRegex(ValueError,
            "{\"recordId\": \"b2bd3384-5a66-4a28-a8bf-9eda7ca26583\", "
            "\"info\": {\"recordStatus\": \"UPDATED\", "
            "\"created\": \"2019-05-14T19:52:37.715824\+02:00\".*",
            int, result)
        self.assertRaisesRegex(ValueError,
            ".*\"updated\": "
            "\"(2019-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}\+\d{2}:\d{2},?){1,}\", "
            "\"deleted\": \"\", "
            "\"recordData\": \"\"}}",
            int, result_updated_part[1])

if __name__ == '__main__':
    unittest.main()
