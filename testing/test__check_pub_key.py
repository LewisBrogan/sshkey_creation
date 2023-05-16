from unittest import TestCase, mock
from check_pub_key import CheckPubKey

import os

class TestCheckPubKey(TestCase):
    @mock.patch('os.path.exists')
    def test_pub_key_exists(self, mock_exists):
        directory = './test_directory'
        pub_key_path = os.path.join(directory, 'id_rsa')
        mock_exists.return_value = True

        with mock.patch('builtins.print') as mock_print:
            CheckPubKey(directory)

        mock_exists.assert_called_once_with(pub_key_path)
        mock_print.assert_called_once_with('File exists inside ssh directory.')

    @mock.patch('os.system')
    @mock.patch('os.path.exists')
    def test_pub_key_doesnt_exist_and_ssh_keygen_succeeds(self, mock_exists, mock_system):
        directory = './test_directory'
        pub_key_path = os.path.join(directory, 'id_rsa')
        mock_exists.return_value = False
        mock_system.return_value = 0

        with mock.patch('builtins.print') as mock_print:
            CheckPubKey(directory)

        mock_exists.assert_called_once_with(pub_key_path)
        mock_system.assert_called_once_with(f'ssh-keygen -t rsa -f {pub_key_path}')
        mock_print.assert_any_call('File does not exist inside ssh directory.')
        mock_print.assert_any_call('Generating RSA key pair...')
        mock_print.assert_any_call('RSA key pair generated successfully.')

    @mock.patch('os.system')
    @mock.patch('os.path.exists')
    def test_pub_key_doesnt_exist_and_ssh_keygen_fails(self, mock_exists, mock_system):
        directory = './test_directory'
        pub_key_path = os.path.join(directory, 'id_rsa')
        mock_exists.return_value = False
        mock_system.return_value = 1

        with mock.patch('builtins.print') as mock_print:
            CheckPubKey(directory)

        mock_exists.assert_called_once_with(pub_key_path)
        mock_system.assert_called_once_with(f'ssh-keygen -t rsa -f {pub_key_path}')
        mock_print.assert_any_call('File does not exist inside ssh directory.')
        mock_print.assert_any_call('Generating RSA key pair...')
        mock_print.assert_any_call('Error occurred during RSA key pair generation.')
