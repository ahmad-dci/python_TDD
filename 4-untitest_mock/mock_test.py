from app import rm

import mock
import unittest

class RmTestCase(unittest.TestCase):
    
    @mock.patch('app.os')
    def test_rm(self, mock_os):
        rm("somefile1.txt")
        # test that rm called os.remove with the right parameters
        mock_os.remove.assert_called_with("somefile1.txt")

if __name__ == '__main__':
    unittest.main()