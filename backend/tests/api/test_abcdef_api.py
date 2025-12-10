import json
import pytest
from rest_framework.reverse import reverse
# from abcdef import models as abcdef_models


pytestmark = pytest.mark.django_db()


class TestAbcdefApi():
    endpoint_abcdef = reverse('-list')

    @pytest.mark.parametrize(
        "phone_str, http_status",
        [
            ('', 201),
            ('', 400),
        ]
    )
    def test_phone_search(self, api_client, phone_str, http_status):
        url = reverse('phone-search', kwargs={'query': phone_str})
        response = api_client().get(url)
        assert response.status_code == http_status
        # fact = json.loads(response.content)
        # assert len(fact) > 0

    def test_phone_retrieve(self, api_client):
        response = api_client().get(self.endpoint_abcdef)
        assert response.status_code == 200
