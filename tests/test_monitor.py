import unittest
from app.monitor import RansomwareMonitor

class TestRansomwareMonitor(unittest.TestCase):
    def test_on_created(self):
        monitor = RansomwareMonitor(["/dummy/path"])
        monitor.on_created(type('test', (object,), {'src_path': '/dummy/path/new_file.txt'}))
        self.assertTrue(True)  # Add assertions as needed

if __name__ == '__main__':
    unittest.main()
