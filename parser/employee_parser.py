from typing import List, Dict


RATE_FIELDS = {'hourly_rate', 'rate', 'salary'}


def parse_csv(files:List[str]) -> List[Dict]:
    data: List[Dict] = []
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            headers_ = lines[0].strip().split(',')
            headers = [headers_lower(header) for header in headers_]

            for line in lines[1:]:
                values = line.strip().split(',')
                record = dict(zip(headers, values))
                employee = {
                    'id': int(record['id']),
                    'email': record['email'],
                    'name': record['name'],
                    'department': record['department'],
                    'hours': float(record['hours_worked']),
                    'rate': float(get_rate_field(record))
                }
                data.append(employee)

    return data

def headers_lower(header: str) -> str:
    return header.strip().lower()


def get_rate_field(record: Dict[str, str]) -> str:
    for field in RATE_FIELDS:
        if field in record:
            return record[field]
    raise ValueError("No valid rate field found.")