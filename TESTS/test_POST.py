import unittest
from PROJECT import record_func


class TestPOST(unittest.TestCase):

    def test_post(self):
        uuid = "d2bd3384-5a66-4a28-a8bf-9eda7ca26583"
        record_func.record_write_new_json(
            "d2bd3384-5a66-4a28-a8bf-9eda7ca26583")
        result = record_func.record_uuid_get(uuid)
        result_updated_part = result.split("created")
        self.assertRaisesRegex(ValueError,
            "{\"recordId\": \"d2bd3384-5a66-4a28-a8bf-9eda7ca26583\", "
            "\"info\": {\"recordStatus\": \"NEW\", "
            "\"created\": "
            "\"2019-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}\+\d{2}:\d{2}\".*",
            int, result)
        self.assertRaisesRegex(ValueError,
            ".*\"updated\": \"\", "
            "\"deleted\": \"\", "
            "\"recordData\": \"\"}}",
            int, result_updated_part[1])

if __name__ == '__main__':
    unittest.main()
