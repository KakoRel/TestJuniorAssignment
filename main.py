import argparse
import csv
import sys
from tabulate import tabulate
from reports import REPORTS

def read_csv_files(file_paths):
    """Читает все CSV-файлы и возвращает список строк (dict)."""
    data = []
    for path in file_paths:
        try:
            with open(path, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    data.append(row)
        except FileNotFoundError:
            print(f"Файл не найден: {path}", file=sys.stderr)
            sys.exit(1)
    return data


def main():
    parser = argparse.ArgumentParser(description="Скрипт для анализа рейтингов брендов")
    parser.add_argument("--files", nargs="+", required=True, help="пути к CSV файлам")
    parser.add_argument("--report", required=True, help="название отчета (например, average-rating)")
    args = parser.parse_args()

    if args.report not in REPORTS:
        print("Неизвестный отчёт. Доступные:", ", ".join(REPORTS.keys()))
        sys.exit(1)

    rows = read_csv_files(args.files)
    report_func = REPORTS[args.report]
    result = report_func(rows)

    if not result:
        print("Нет данных для отчёта.")
        return

    print(tabulate(result, headers=["brand", "rating"], tablefmt="grid"))


if __name__ == "__main__":
    main()
