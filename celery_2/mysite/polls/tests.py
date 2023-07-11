import json
import pathlib

import pytest
import responses
from django.core.management import call_command
from freezegun import freeze_time

from .views import send_sms_view

root = pathlib.Path(__file__).parent


@pytest.fixture
def mocked():
    def inner(file_name):
        return json.load(open(root / "fixtures" / file_name))

    return inner


# Create your tests here.

@pytest.fixture
def test_send_sms_view(mocked):
    request = mocked.post('/send_sms/', {'phone_number': '123456789', 'message': 'Test message'})
    response = send_sms_view(request)

    assert response.status_code == 200
    assert response.template_name == 'success.html'


def test_send_sms_view_get(mocked):
    request = mocked.get('/send_sms/')
    response = send_sms_view(request)

    assert response.status_code == 200
    assert response.template_name == 'form.html'
