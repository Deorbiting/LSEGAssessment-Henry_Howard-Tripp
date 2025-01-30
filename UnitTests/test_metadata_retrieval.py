import unittest
from unittest.mock import patch, Mock
import json
from metadata_retrieval import get_token, get_metadata
import requests

class TestMetadataRetrieval(unittest.TestCase):
    
    @patch('requests.put')
    #Mocks successful token retrieval
    def test_get_token_success(self, mock_put):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text ='test-token-123'
        mock_put.return_value = mock_response
        #Called function and check the result
        token = get_token()
        self.assertEqual(token,'test-token-123')
        mock_put.assert_called_once_with(
            "http://169.254.169.254/latest/api/token",
            headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"},
            timeout=1
        )

    @patch('requests.get')
    def test_get_token_failure(self, mock_put):
        #Mocks token failure
        mock_put.side_effect = Exception("Connection error")
        result= get_token()
        self.assertIsNone(result)
        
  
    @patch('requests.Session')
    @patch('requests.get')
    def test_get_metadata_all(self, mock_get, mock_session):
        #Mocks successful metadata retrieval
        mock_list_response = Mock()
        mock_list_response.status_code = 200
        mock_list_response.text ='ami-id\ninstance-type'
        mock_get.return_value = mock_list_response

        session_instance = Mock()
        mock_session.return_value.__enter__.return_value = session_instance
        
        mock_item_response = Mock()
        mock_item_response.status_code = 200
        mock_item_response.text ='test-value'
        session_instance.get.return_value = mock_item_response

        result = get_metadata('test-token')
        expected = json.dumps({
            'ami-id': 'test-value',
            'instance-type': 'test-value'
        }, indent=1)

        self.assertEqual(result, expected)

    @patch('requests.Session')
    @patch('requests.get')
    def test_get_metadata_with_key(self, mock_get, mock_session):
        #Mocks successful metadata retrieval with a key
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = 'ami-id\ninstance-type'
        mock_get.return_value = mock_response

        session_instance = Mock()
        mock_session.return_value.__enter__.return_value = session_instance
        mock_item_response = Mock()
        mock_item_response.status_code = 200
        mock_item_response.text = 'test-value'
        session_instance.get.return_value = mock_item_response

        result = get_metadata('test-token', 'ami-id')
        expected = json.dumps({'ami-id': 'test-value'}, indent=1)

        self.assertEqual(result, expected)

    @patch('requests.get')
    def test_get_metadata_timeout(self, mock_get):
        #Mocks metadata retrieval timeout
        mock_get.side_effect = requests.exceptions.Timeout()
        result = get_metadata('test-token')
        self.assertIsNone(result)



if __name__ == "__main__":
    unittest.main()
