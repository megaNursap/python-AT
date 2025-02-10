import requests
from utils.config import Config

def test_get_users():
    response = requests.get(f"{Config.API_URL}/users")
    assert response.status_code == 200
    assert len(response.json()) > 0
