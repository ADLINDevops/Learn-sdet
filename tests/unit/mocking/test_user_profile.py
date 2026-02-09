import pytest
import requests
from unittest.mock import Mock,patch

class Userservice:
    """ Production scenario"""
    def get_user_profile(self,user_id):
        response=requests.get(f"https://api.example.com/users/{user_id}")
        return response.json()
class TestUserservice:
    @pytest.fixture
    def mock_requests_get(self):
        #mock External dependency
        with patch("requests.get") as mock_get:
            mock_response=Mock()
            mock_response.json.return_value={
                "id":1,
                "name":"John Doe",
                "email":"user@gmail.com"
            }
            mock_response.status_code=200
            mock_get.return_value=mock_response
            yield mock_get #ensures cleanup
    def test_user_service_mocked(self,mock_requests_get):
        service=Userservice()
        profile=service.get_user_profile(1)
        assert profile["id"]==1
        assert profile["name"]=="John Doe"
        assert "@" in profile["email"]
        mock_requests_get.assert_called_once_with("https://api.example.com/users/1")