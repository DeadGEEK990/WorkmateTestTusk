import argparse
import os
import json
from datetime import datetime
from parser.employee_parser import parse_csv
from reports.payout import PayoutReport

REPORTS = {
    'payout': PayoutReport,
}
RESULTS_DIRECTORY = 'results/'


def main():
    parser = argparse.ArgumentParser(description="Employee Report Generator")
    parser.add_argument('files', nargs='+', help='CSV files with employee data')
    parser.add_argument('--report', required=True, choices=REPORTS.keys())

    try:
        args = parser.parse_args()

        files = args.files
        if not files:
            raise ValueError("Не указаны входные файлы.")

        try:
            data = parse_csv(files)
        except Exception as e:
            print(f"Ошибка при чтении CSV файлов: {e}")
            return

        report_class = REPORTS.get(args.report)
        if not report_class:
            raise ValueError(f"Отчет '{args.report}' не поддерживается.")

        report = report_class()

        try:
            report_result = report.create_report(data)
        except Exception as e:
            print(f"Ошибка при формировании отчета: {e}")
            return

        os.makedirs(RESULTS_DIRECTORY, exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        result_filename = f'{RESULTS_DIRECTORY}{args.report}_{timestamp}.json'

        try:
            with open(result_filename, 'w', encoding='utf-8') as f:
                json.dump(report_result, f, indent=2, ensure_ascii=False)
            print(f"Отчёт успешно сохранён в: {result_filename}")
        except Exception as e:
            print(f"Ошибка при сохранении отчёта: {e}")

    except Exception as e:
        print(f"Критическая ошибка: {e}")


if __name__ == "__main__":
    main()