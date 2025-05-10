import pytest
from reports.payout import PayoutReport


@pytest.fixture
def result_data():
    data = [
        {
            "id": 1,
            "name": "Alice Johnson",
            "hours": 160.0,
            "rate": 50.0,
            "payout": 8000.0
        }
    ]
    return data


@pytest.fixture
def start_data():
    data = [
        {
            "id": 1,
            "name": "Alice Johnson",
            "email": "alice@example.com",
            "department": "Marketing",
            "hours": 160.0,
            "rate": 50.0,
        }
    ]
    return data


def test_payout(start_data, result_data):
    report = PayoutReport()
    result = report.create_report(data=start_data)

    assert result[0]['id'] == 1
    assert result[0]['name'] == "Alice Johnson"
    assert result[0]['hours'] == 160.0
    assert result[0]['rate'] == 50.0
    assert result[0]['payout'] == 8000.0