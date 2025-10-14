import csv
import pytest
from reports.average_rating import average_rating

def make_csv(tmp_path, name, rows):
    path = tmp_path / name
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "brand", "price", "rating"])
        writer.writerows(rows)
    return path


# ТЕСТЫ ДЛЯ average_rating #

def test_average_rating_basic(tmp_path):
    path = make_csv(tmp_path, "data.csv", [
        ["phone", "apple", "1000", "4.9"],
        ["tablet", "apple", "800", "4.7"],
        ["phone", "samsung", "900", "4.8"],
    ])
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    result = average_rating(rows)
    assert result[0][0] == "apple"
    assert result[0][1] == 4.8


def test_average_rating_ignores_invalid_rows(tmp_path):
    path = make_csv(tmp_path, "data.csv", [
        ["phone", "", "100", "4.5"],  # нет бренда !!!!!!
        ["phone", "apple", "100", "bad"],  # неверный рейтинг !!!!!!
        ["phone", "apple", "100", "4.0"],
    ])
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    result = average_rating(rows)
    assert result == [["apple", 4.0]]


def test_average_rating_sorting(tmp_path):
    path = make_csv(tmp_path, "data.csv", [
        ["p1", "apple", "1000", "4.6"],
        ["p2", "samsung", "1000", "4.8"],
        ["p3", "xiaomi", "1000", "4.5"],
    ])
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    result = average_rating(rows)
    assert [r[0] for r in result] == ["samsung", "apple", "xiaomi"]


def test_average_rating_handles_empty_file(tmp_path):
    path = make_csv(tmp_path, "empty.csv", [])
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    result = average_rating(rows)
    assert result == []
