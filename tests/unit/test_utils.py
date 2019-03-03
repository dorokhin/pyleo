from pyleo.utils import create_node
from unittest.mock import patch
import unittest


class TestUtils(unittest.TestCase):

    @patch('os.path.expanduser')
    @patch('os.path.exists')
    @patch('os.makedirs')
    @patch('os.mknod')
    def test_create_node_if_file_exist(self, mock_mknod, mock_makedirs, mock_exists, mock_expanduser):
        mock_expanduser.return_value = '/home/username/'
        expected = '/home/username/.pyleo/cookies.txt'
        result = create_node()
        self.assertEqual(expected, result)

    @patch('os.path.expanduser')
    @patch('os.path.exists')
    @patch('os.makedirs')
    @patch('os.mknod')
    def test_create_node_if_file_not_exist(self, mock_mknod, mock_makedirs, mock_exists, mock_expanduser):
        mock_expanduser.return_value = '/home/username/'
        mock_exists.return_value = False
        expected = '/home/username/.pyleo/cookies.txt'
        result = create_node()
        self.assertEqual(expected, result)
