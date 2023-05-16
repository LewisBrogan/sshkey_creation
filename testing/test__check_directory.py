import os
import unittest
from check_directory import CheckDirectory

class TestCheckDirectory(unittest.TestCase):
    def test_directory_creation(self):
        test_dir = './test_directory'
        if os.path.exists(test_dir):
            os.rmdir(test_dir)
        check_dir = CheckDirectory(test_dir)
        self.assertTrue(os.path.exists(test_dir))
        os.rmdir(test_dir)

if __name__ == '__main__':
    unittest.main()
