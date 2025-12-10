import pytest
from abcdef import models as abcdef_models
from django.core.exceptions import ValidationError
from contextlib import nullcontext


pytestmark = pytest.mark.django_db()


# class TestAbcdefModel:
#     def test_disply_attrs(self):
#         obj = abcdef_models.Phone.objects.all().first()
#         assert str(obj) == f""
