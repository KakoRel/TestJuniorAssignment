import argparse
import csv
from tabulate import tabulate

def average_rating(files):
    brands = {}
    counts = {}
    
    for file in files:
        with open(file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                brand = row['brand']
                rating = row['rating']
                try:
                    rating = float(rating)
                except:
                    continue
                if brand in brands:
                    brands[brand] += rating
                    counts[brand] += 1
                else:
                    brands[brand] = rating
                    counts[brand] = 1
    result = []
    for b in brands:
        avg = round(brands[b] / counts[b], 2)
    result.append([b, avg])

    result.sort(key=lambda x: x[1], reverse=True)
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', nargs='+', required=True, help='пути к CSV файлам')
    parser.add_argument('--report', required=True, help='тип отчета (пока только average-rating)')
    args = parser.parse_args()
    
    if args.report != 'average-rating':
        print('Неизвестный отчёт. Поддерживается только average-rating')
        return

    data = average_rating(args.files)
    print(tabulate(data, headers=['brand', 'rating'], tablefmt='grid'))

if __name__ == '__main__':
    main()