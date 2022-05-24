import pytest
from django.urls import reverse

def test_status_code(client):
    resp = client.get(reverse('base:home'))
    assert resp.status_code == 200