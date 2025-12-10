import pytest
# from abcdef import views as abcdef_views   # noqa: F403, F401
# from abcdef import models as abcdef_models
from abcdef import tasks


pytestmark = pytest.mark.django_db()


class TestAbcdefTasks:
    def test_create_any_task(self, celery_app, celery_worker):
        @celery_app.task
        def mul(x, y):
            return x * y

        celery_worker.reload()
        assert mul.delay(4, 4).get(timeout=10) == 16
