"""
Web Service class
"""

from typing import Any

import requests


class WebService:
    """
    Service responsible for getting data
    """
    def get_data(self) -> Any:
        """
        Returns json response
        :return:
        """
        result = requests.get('https://jsonplaceholder.typicode.com/posts/1')
        if result.status_code == 404:
            return {"error": "Post not found"}
        return result.json()
