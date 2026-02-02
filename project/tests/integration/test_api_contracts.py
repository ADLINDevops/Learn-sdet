import pytest
import requests

class TestAPIContracts:
    Base_URL="https://jsonplaceholder.typicode.com"
    def test_get_user_contract(self):
        response=requests.get(f"{self.Base_URL}/users/1")
        assert response.status_code==200
        assert response.headers["content-type"].startswith("application/json")
        user=response.json()
        assert "id" in user
        assert user["id"]==1
        assert isinstance(user["name"],str)
        assert "@" in user["email"]
        assert len(user["company"]["name"])>0
    @pytest.mark.parametrize("user_id",[1,2,3])
    def test_multiple_user(self,user_id):
        response=requests.get(f"{self.Base_URL}/users/{user_id}")
        assert response.status_code==200
        user=response.json()
        assert user["id"]==user_id