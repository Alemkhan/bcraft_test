import pytest
from django import urls

from ..models import Statistics


@pytest.mark.django_db
@pytest.mark.dependency()
def test_statistics_create(client, dummy_statistics):
    create_url = urls.reverse('statistics_create')
    for stat in dummy_statistics:
        resp = client.post(create_url, stat)
        assert resp.status_code == 201
    assert Statistics.objects.count() == 3


@pytest.mark.django_db
@pytest.mark.dependency(depends=['test_statistics_create'])
def test_statistics_view(client, create_test_statistics):
    assert Statistics.objects.count() == 3
    get_url = urls.reverse('statistics_list')
    resp = client.get(get_url)
    assert resp.status_code == 200
    assert resp.content is not None


@pytest.mark.django_db
@pytest.mark.dependency(depends=['test_statistics_create'])
def test_statistics_delete(client, create_test_statistics):
    delete_url = urls.reverse('statistics_reset')
    assert Statistics.objects.count() == 3
    resp = client.delete(delete_url)
    assert resp.status_code == 200
    assert Statistics.objects.filter(is_deleted=False).count() == 0

