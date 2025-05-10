import pytest
from parser.employee_parser import parse_csv
import os


@pytest.fixture
def temporary_file():
    file_paths = ['tests/data/temp_file1.txt', 'tests/data/temp_file2.txt']

    data1 = """id,email,name,department,hours_worked,hourly_rate
1,alice@example.com,Alice Johnson,Marketing,160,50"""
    data2 = """department,id,email,name,hours_worked,rate
HR,101,grace@example.com,Grace Lee,160,45"""

    with open(file_paths[0], 'w') as f:
        f.write(data1)
    with open(file_paths[1], 'w') as f:
        f.write(data2)

    yield file_paths

    for file in file_paths:
        if os.path.exists(file):
            os.remove(file)


def test_parser(temporary_file):
    data = parse_csv(temporary_file)

    assert data[0]['id'] == 1
    assert data[0]['email'] == 'alice@example.com'
    assert data[0]['name'] == 'Alice Johnson'
    assert data[0]['department'] == 'Marketing'
    assert data[0]['hours'] == 160.0
    assert data[0]['rate'] == 50.0

    assert data[1]['id'] == 101
    assert data[1]['email'] == 'grace@example.com'
    assert data[1]['name'] == 'Grace Lee'
    assert data[1]['department'] == 'HR'
    assert data[1]['hours'] == 160.0
    assert data[1]['rate'] == 45.0