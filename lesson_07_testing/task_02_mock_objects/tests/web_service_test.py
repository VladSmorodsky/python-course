"""
Cover WebService class
"""

import unittest
from unittest.mock import patch, Mock

from lesson_07_testing.task_02_mock_objects.src.web_service import WebService


class WebServiceTest(unittest.TestCase):

    @patch('src.web_service.requests.get')
    def test_get_data_method(self, mocked_method):
        """
        Test get_data method with mocked response
        :param mocked_method:
        :return:
        """
        expected_result = {"id": 1, "name": "Mocked User"}
        mock_response = Mock()
        mock_response.json.return_value = expected_result
        mocked_method.return_value = mock_response
        web_service = WebService()
        result = web_service.get_data()
        self.assertEqual(expected_result, result)

    @patch('src.web_service.requests.get')
    def test_get_data_method_returns_not_found_result(self, mocked_method):
        """
        Test get_data method with response 404
        :param mocked_method:
        :return:
        """
        expected_result = {"error": "Post not found"}
        mock_response = Mock()
        mock_response.status_code = 404
        mocked_method.return_value = mock_response
        web_service = WebService()
        result = web_service.get_data()
        self.assertEqual(expected_result, result)
