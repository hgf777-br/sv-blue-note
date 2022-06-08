import pytest
from django.urls import reverse

@pytest.fixture
def resp(client):
    return client.get(reverse('login'))

def test_login_page(resp):
    assert resp.status_code == 200