from reports import Report
from typing import List, Dict


class PayoutReport(Report):
    def create_report(self, data: List[Dict]) -> List[Dict]:
        result: List[Dict] = []
        for row in data:
            employer_data: Dict = {
                'id' : row['id'],
                'name' : row['name'],
                'hours' : row['hours'],
                'rate' : row['rate'],
                'payout' : row['hours'] * row['rate']
            }
            result.append(employer_data)
        return result