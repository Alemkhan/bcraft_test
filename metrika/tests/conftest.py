import pytest
from ..models import Statistics

@pytest.fixture
def dummy_statistics():
    statistics = [
        {
            "date": "2021-12-19",
            "views": 2200,
            "clicks": 1300,
            "cost": "2500.00",
        },
        {
            "date": "2021-12-20",
        },
        {
            "date": "2021-12-19",
            "views": 3000,
            "clicks": 1000,
            "cost": "3000.00",
        }
    ]
    return statistics


@pytest.fixture
def create_test_statistics(dummy_statistics):
    test_data = []
    for stat in dummy_statistics:
        test_data.append(Statistics.objects.create(**stat))
    return test_data
